from mesa import Agent

class BrokerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.completed_sales = 0

    def step(self):
        pass  # Logik wird von Käufern ausgelöst

    def mediate_transaction(self, buyer, seller):
        if buyer.budget >= seller.price:
            self.model.register_sale(buyer, seller)
            self.completed_sales += 1
