import queue
import json

from flask import Flask, request

from src.Cook import Cook

NUMBER_OF_COOKS = 4

app = Flask(__name__)

DINING_HALL_URL = "http://dining-hall:5001"

orderList = queue.Queue()

@app.route("/")
def home():
    return "Hello from kitchen server"


@app.route("/list")
def see_order_list():
    elements = list()
    for q_item in orderList.queue:
        elements.append(q_item)

    return f"{len(elements)}"

@app.route('/order', methods=['POST'])
def receive_order():
    data = request.json
    order_dict = json.loads(data)["order"]

    app.logger.info("A request from dining hall is here!")
    app.logger.info(json.dumps(f"Order id: {order_dict['id']}"))
    app.logger.info(json.dumps(f"Max wait: {order_dict['max_wait']}"))
    orderList.put(json.loads(data))

    # requests.post(f"{DINING_HALL_URL}/order-from-kitchen", json=data)
    return "Ok"


if __name__ == '__main__':

    for cook_id in range(0, NUMBER_OF_COOKS):
        cook = Cook(cook_id, 3, 3, orderList)
        cook.daemon = True
        cook.start()

    app.run(debug=True, port=5000, host="0.0.0.0")
