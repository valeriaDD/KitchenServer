import json
import logging

from flask import Flask, request

from src.Cook import Cook
from src.Kitchen import Kitchen

NUMBER_OF_COOKS = 4

app = Flask(__name__)

DINING_HALL_URL = "http://dining-hall:5001"

logger = logging.getLogger(__name__)


@app.route("/")
def home():
    return "Hello from kitchen server"


@app.route('/order', methods=['POST'])
def receive_order():
    data = request.json
    order_dict = json.loads(data)
    logger.info("Order is here")
    app.logger.info("Order is here")
    kitchen.add_order(order_dict)

    return "Ok"


if __name__ == '__main__':
    cooks = json.load(open('./src/cooks.json'))
    oven_number = 2
    stove_number = 1
    kitchen = Kitchen(oven_number, stove_number)


    for cook in cooks:
        cook_thread = Cook(cook["id"], cook["rank"], cook["proeficiency"], cook["name"], kitchen)
        cook_thread.daemon = True
        cook_thread.start()

    app.run(debug=True, port=5000, host="0.0.0.0")
