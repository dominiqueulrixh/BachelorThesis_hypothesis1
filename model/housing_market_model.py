from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random

from agenten.buyer_agent import BuyerAgent
from agenten.seller_agent import SellerAgent
from agenten.broker_agent import BrokerAgent

class HousingMarketModel(Model):
    def __init__(self, N_buyers=10, N_sellers=5, start_week=1):
        self.num_agents = N_buyers + N_sellers + 1
        self.schedule = RandomActivation(self)
        self.sales = []
        self.current_week = start_week  # Beginn bei KW 1


        for i in range(N_buyers):
            budget = random.randint(500_000, 1_000_000)
            location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
            a = BuyerAgent(i, self, budget, location)
            self.schedule.add(a)

        for i in range(N_buyers, N_buyers + N_sellers):
            price = random.randint(400_000, 1_100_000)
            location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
            a = SellerAgent(i, self, price, location)
            self.schedule.add(a)

        broker = BrokerAgent(self.num_agents - 1, self)
        self.schedule.add(broker)
        self.broker = broker

        self.datacollector = DataCollector(
            model_reporters={
                "Kalenderwoche": lambda m: m.current_week,
                "Completed Sales": lambda m: len(m.sales),
                "Broker Sales": lambda m: m.broker.completed_sales,
                "Active Buyers": lambda m: sum(1 for a in m.schedule.agents if isinstance(a, BuyerAgent) and a.active),
                "Listed Properties": lambda m: sum(
                    1 for a in m.schedule.agents if isinstance(a, SellerAgent) and a.listed),
            }
        )

    def get_listings(self, location=None, max_price=None):
        listings = [a for a in self.schedule.agents if isinstance(a, SellerAgent) and a.listed]
        if location:
            listings = [l for l in listings if l.location == location]
        if max_price:
            listings = [l for l in listings if l.price <= max_price]
        return listings

    def register_sale(self, buyer, seller):
        self.sales.append((buyer.unique_id, seller.unique_id))
        seller.listed = False
        buyer.successful = True
        self.schedule.remove(seller)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_week += 1

        # Nachfrage-Angebot-Verhältnis prüfen
        active_buyers = sum(1 for a in self.schedule.agents if isinstance(a, BuyerAgent) and a.active)
        listings = sum(1 for a in self.schedule.agents if isinstance(a, SellerAgent) and a.listed)

        # Wenn Nachfrage deutlich > Angebot: neue Immobilien kommen auf den Markt
        if active_buyers > listings and self.current_week % 2 == 0:
            for _ in range(1):  # zwei neue Objekte hinzufügen
                price = random.randint(500_000, 1_100_000)
                location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
                new_seller = SellerAgent(self.num_agents, self, price, location)
                self.schedule.add(new_seller)
                self.num_agents += 1
