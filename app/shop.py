from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_product_cost(self, customer):
        total_cost = 0
        for product, amount in customer.products_to_buy.items():
            total_cost += amount * self.products[product]
        return total_cost

    def purchase(self, customer):
        products_cost = round(self.calculate_product_cost(customer), 2)
        customer.money -= products_cost
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_date}\n"
              f"Thank's {customer.name} for purchase!\n"
              f"You have bought:\n")
        for product, amount in customer.products_to_buy.items():
            cost = amount * self.products[product]
            print(f"{amount} {product}s for {cost} dollars")
        print(f"Total cost is {products_cost} dollars\n"
              f"See you again\n")


def create_shops(shops: list):
    shops_list = []
    for shop in shops:
        shops_list.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))
    return shops_list



