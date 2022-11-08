import json
import logging
import threading
import time

from src.Kitchen import Kitchen
from src.Menu import Menu

from pipenv.patched.pip._vendor import requests

FOOD_ORDERING_SERVICE = "http://food-ordering:5003"

logger = logging.getLogger(__name__)


class Cook(threading.Thread):
    menu = Menu()

    def __init__(self, cook_id, rank, proeficiency, name, kitchen: Kitchen):
        super(Cook, self).__init__()
        self.id = cook_id
        self.rank = rank
        self.proeficiency = proeficiency
        self.name = name
        self.kitchen = kitchen

    def run(self, *args):
        for i in range(self.proeficiency):
            task_thread = threading.Thread(target=self.cook)
            task_thread.daemon = True
            task_thread.start()

    def cook(self):
        while True:
            self.kitchen.order_q_mutex.acquire()
            dish, order = self.find_food_item()
            self.kitchen.order_q_mutex.release()
            if dish is not None:
                print(f"Cook {self.id} started preparation of {dish['id']} from order {order.order_id} using {dish['cooking-apparatus']} ")
                time.sleep(dish['preparation-time'])
                if dish['cooking-apparatus'] is not None:
                    self.kitchen.release_aparatus(dish["cooking-apparatus"])
                if order.is_ready():
                    self.kitchen.order_q_mutex.acquire()
                    if order in self.kitchen.order_q:
                        self.kitchen.order_q.remove(order)
                    now = time.time()
                    order.cooking_time = now
                    requests.post(f"{FOOD_ORDERING_SERVICE}/distribution", json=json.dumps(order.get()))
                    self.kitchen.order_q_mutex.release()
                else:
                    continue

    def find_food_item(self):
        dish, order = self.find_dish_to_prepare()

        if dish is not None:
            order.cooking_details.append({
                "food_id": dish["id"],
                "cook_id": self.id,
            })

        return dish, order

    def find_dish_to_prepare(self):
        for order in self.kitchen.order_q:
            for items_to_be_prepared in order.items_to_be_prepared:
                item = Menu().get_menu_item(items_to_be_prepared)
                if self.rank == item["complexity"] or self.rank == int(item["complexity"]) - 1:
                    if item["cooking-apparatus"] is None or self.kitchen.has_available_aparatus(item["cooking-apparatus"]):
                        print(f"items: {order.items} to prepate: {order.items_to_be_prepared} order_id: {order.order_id}")
                        order.items_to_be_prepared.remove(item["id"])
                        print(f"items: {order.items} to prepate: {order.items_to_be_prepared}")
                        return item, order
                    else:
                        continue
                else:
                    continue
        return None, None
