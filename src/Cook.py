import json
import threading
import time
from queue import Queue
from src.Menu import Menu
from pipenv.patched.pip._vendor import requests

DINING_HALL_URL = "http://dining-hall:5001"


class Cook(threading.Thread):
    menu = Menu()

    def __init__(self, cook_id, rank, proficiency, order_q: Queue):
        super(Cook, self).__init__()
        self.id = cook_id
        self.rank = rank
        self.proficiency = proficiency
        self.order_q = order_q

    def run(self, *args):
        while True:
            if not self.order_q.empty():
                order = self.order_q.get()
                order_items = order["order"]['order_items']
                print(order_items)
                while order_items:
                    item = order_items.pop(0)
                    print(item)
                    item_id = item["id"]
                    self.cook(item_id)
                requests.post(f"{DINING_HALL_URL}/order-from-kitchen", json=json.dumps(order))
            else:
                time.sleep(3)

    def cook(self, item_id):
        menu_item = self.menu.get_menu_item(item_id)
        menu_item_preparation_time = menu_item["preparation-time"]
        print(f"Cook {self.id} started preparation of {item_id}")
        time.sleep(menu_item_preparation_time)
