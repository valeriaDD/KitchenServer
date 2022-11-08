class Order:
    def __init__(self, order_id, client_id, items, priority, max_wait):
        self.order_id = order_id
        self.client_id = client_id
        self.items = items.copy()
        self.priority = priority
        self.max_wait = max_wait
        self.cooking_time = 0
        self.cooking_details = []
        self.items_to_be_prepared = items

    def is_ready(self):
        return len(self.items_to_be_prepared) == 0

    def get(self):
        return {
            "order_id": self.order_id,
            "client_id": self.client_id,
            "items": self.items,
            "priority": self.priority,
            "max_wait": self.max_wait,
            "cooking_time": self.cooking_time,
            "cooking_details": self.cooking_details
        }
