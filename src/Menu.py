import random
import json


class Menu:
    def __init__(self):
        self.menu = [{
            "id": 1,
            "name": "pizza",
            "preparation-time": 20,
            "complexity": 2,
            "cooking-apparatus": "oven"
        },
            {
                "id": 2,
                "name": "salad",
                "preparation-time": 10,
                "complexity": 1,
                "cooking-apparatus": None
            },
            {
                "id": 3,
                "name": "zeama",
                "preparation-time": 7,
                "complexity": 1,
                "cooking-apparatus": "stove"
            },
            {
                "id": 4,
                "name": "Scallop Sashimi with Meyer Lemon Confit",
                "preparation-time": 32,
                "complexity": 3,
                "cooking-apparatus": None
            },
            {
                "id": 5,
                "name": "Island Duck with Mulberry Mustard",
                "preparation-time": 35,
                "complexity": 3,
                "cooking-apparatus": "oven"
            },
            {
                "id": 6,
                "name": "Waffles",
                "preparation-time": 10,
                "complexity": 1,
                "cooking-apparatus": "stove"
            },
            {
                "id": 7,
                "name": "Aubergine",
                "preparation-time": 20,
                "complexity": 2,
                "cooking-apparatus": "oven"
            },
            {
                "id": 8,
                "name": "Lasagna",
                "preparation-time": 30,
                "complexity": 2,
                "cooking-apparatus": "oven"
            },
            {
                "id": 9,
                "name": "Burger",
                "preparation-time": 15,
                "complexity": 1,
                "cooking-apparatus": "stove"
            },
            {
                "id": 10,
                "name": "Gyros",
                "preparation-time": 15,
                "complexity": 1,
                "cooking-apparatus": None
            },
            {
                "id": 11,
                "name": "Kebab",
                "preparation-time": 15,
                "complexity": 1,
                "cooking-apparatus": None
            },
            {
                "id": 12,
                "name": "Unagi Maki",
                "preparation-time": 20,
                "complexity": 2,
                "cooking-apparatus": None
            },
            {
                "id": 13,
                "name": "Tobacco Chicken",
                "preparation-time": 30,
                "complexity": 2,
                "cooking-apparatus": "oven"
            }]

    def get_menu_item(self, item_id):
        return self.menu[item_id - 1]
