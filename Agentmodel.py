# Agentenmodell für Hypothese 1 (Mesa Framework)
# Ziel: Nachweis, dass ein Multi-Agentensystem Marktverhalten modellieren kann

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random

# --- Agentendefinitionen ---

class BuyerAgent(Agent):
    def __init__(self, unique_id, model, budget, preferred_location):
        super().__init__(unique_id, model)
        self.budget = budget
        self.preferred_location = preferred_location
        self.active = False

    def step(self):
        # Aktivierung basierend auf Suchtrends (hier zufällig)
        self.active = random.random() < 0.4
        if self.active:
            # Käufer sucht nach passendem Objekt
            listings = [a for a in self.model.schedule.agents if isinstance(a, SellerAgent)]
            affordable = [l for l in listings if l.price <= self.budget and l.location == self.preferred_location]
            if affordable:
                chosen = self.random.choice(affordable)
                self.model.register_sale(self, chosen)


class SellerAgent(Agent):
    def __init__(self, unique_id, model, price, location):
        super().__init__(unique_id, model)
        self.price = price
        self.location = location
        self.listed = True

    def step(self):
        # Seller bleibt zunächst passiv – könnte später dynamisch werden
        pass


class BrokerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Makler könnte Transaktionen verwalten oder Statistiken sammeln
        pass


# --- Modell ---

class HousingMarketModel(Model):
    def __init__(self, N_buyers=10, N_sellers=5):
        self.num_agents = N_buyers + N_sellers + 1
        self.schedule = RandomActivation(self)
        self.sales = []

        # Buyer agents
        for i in range(N_buyers):
            budget = random.randint(500_000, 1_000_000)
            location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
            a = BuyerAgent(i, self, budget, location)
            self.schedule.add(a)

        # Seller agents
        for i in range(N_buyers, N_buyers + N_sellers):
            price = random.randint(400_000, 1_100_000)
            location = random.choice(["Zentrum", "Kreis 4", "Seefeld"])
            a = SellerAgent(i, self, price, location)
            self.schedule.add(a)

        # Broker agent
        broker = BrokerAgent(self.num_agents - 1, self)
        self.schedule.add(broker)

        self.datacollector = DataCollector(
            model_reporters={"Completed Sales": lambda m: len(m.sales)}
        )

    def register_sale(self, buyer, seller):
        self.sales.append((buyer.unique_id, seller.unique_id))
        seller.listed = False
        self.schedule.remove(seller)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()


# --- Beispielausführung ---

if __name__ == "__main__":
    model = HousingMarketModel()
    for i in range(20):
        model.step()

    print("Anzahl abgeschlossener Verkäufe:", len(model.sales))
