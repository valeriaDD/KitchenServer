import logging
import queue
import threading

from src.CookingAparatus import CookingAparatus
from src.Order import Order

logger = logging.getLogger(__name__)


class Kitchen:
    def __init__(self, number_of_ovens, number_of_stoves):
        self.order_q = []
        self.order_q_mutex = threading.Lock()
        self.kitchen_apataratus_q = queue.Queue()

        for _ in range(number_of_ovens):
            self.kitchen_apataratus_q.put(CookingAparatus('oven'))

        for _ in range(number_of_stoves):
            self.kitchen_apataratus_q.put(CookingAparatus('stove'))

    def has_available_aparatus(self, aparatus_type):
        for aparatus in self.kitchen_apataratus_q.queue:
            if aparatus.type == aparatus_type and aparatus.isAvailable:
                aparatus.isAvailable = False
                print(f"aparatus taken: {aparatus_type}")
                self.__print_aparatus_queue()
                return True
            else:
                continue

    def release_aparatus(self, aparatus_type):
        for aparatus in self.kitchen_apataratus_q.queue:
            if aparatus.type == aparatus_type and not aparatus.isAvailable:
                print(f"aparatus released: {aparatus_type}")
                aparatus.isAvailable = True
                self.__print_aparatus_queue()

    def __print_aparatus_queue(self):
        for q_item in self.kitchen_apataratus_q.queue:
            print(q_item.get())

    def add_order(self, order_dict):
        order = Order(order_dict["order_id"], order_dict["client_id"],
                      order_dict["order_items"],
                      order_dict["priority"], order_dict["max_wait"])

        self.order_q_mutex.acquire()
        self.order_q.append(order)
        self.order_q_mutex.release()
