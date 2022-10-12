class CookingAparatus:
    def __init__(self, type):
        self.type = type
        self.isAvailable = True

    def get(self):
        return {'type': self.type, 'isAvailable': self.isAvailable}