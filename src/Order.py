class Order:
    def __init__(self, order_id, table_id, waiter_id, items, priority, max_wait, pick_up_time):
        self.order_id = order_id
        self.table_id = table_id
        self.waiter_id = waiter_id
        self.items = items.copy()
        self.priority = priority
        self.max_wait = max_wait
        self.pick_up_time = pick_up_time
        self.cooking_time = 0
        self.cooking_details = []
        self.items_to_be_prepared = items

    def is_ready(self):
        return len(self.items_to_be_prepared) == 0

    def get(self):
        return {
            "order_id": self.order_id,
            "table_id": self.table_id,
            "waiter_id": self.waiter_id,
            "items": self.items,
            "priority": self.priority,
            "max_wait": self.max_wait,
            "pick_up_time": self.pick_up_time,
            "cooking_time": self.cooking_time,
            "cooking_details": self.cooking_details
        }
