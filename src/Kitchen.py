import logging
import queue
import threading

from src.Order import Order

logger = logging.getLogger(__name__)


class Kitchen:
    def __init__(self):
        self.order_q = queue.Queue()
        self.order_q_mutex = threading.Lock()

    def add_order(self, order_dict):
        order = Order(order_dict["order_id"], order_dict["table_id"],
                      order_dict["waiter_id"], order_dict["order_items"],
                      order_dict["priority"], order_dict["max_wait"],
                      order_dict["pick_up_time"])
        self.order_q_mutex.acquire()
        self.order_q.put(order)
        self.order_q_mutex.release()

