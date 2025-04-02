from mesa import Agent

class SellerAgent(Agent):
    def __init__(self, unique_id, model, price, location):
        super().__init__(unique_id, model)
        self.price = price
        self.location = location
        self.listed = True
        self.active_weeks = 0

    def step(self):
        self.active_weeks += 1
        if self.active_weeks > 5:
            self.price *= 0.95  # Preisnachlass bei längerer Inaktivität
