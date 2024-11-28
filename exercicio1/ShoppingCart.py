from Item import Item

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def clear_cart(self):
        self.items.clear()

    def get_item_count(self) -> int:
        return len(self.items)

    def get_total_price(self) -> float:
        return sum(item.get_price() for item in self.items)

    def get_items(self) -> list:
        return self.items
