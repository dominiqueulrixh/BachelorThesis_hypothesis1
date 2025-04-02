from mesa import Agent
import random

class BuyerAgent(Agent):
    def __init__(self, unique_id, model, budget, preferred_location):
        super().__init__(unique_id, model)
        self.budget = budget
        self.preferred_location = preferred_location
        self.active = False
        self.successful = False

    def step(self):
        self.active = random.random() < 0.4
        if self.active:
            suitable_listings = self.model.get_listings(location=self.preferred_location, max_price=self.budget)
            if suitable_listings:
                chosen = self.random.choice(suitable_listings)
                self.model.broker.mediate_transaction(self, chosen)
