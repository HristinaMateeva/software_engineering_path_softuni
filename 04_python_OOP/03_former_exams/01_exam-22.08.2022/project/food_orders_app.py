from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    receipt_id = 0
    def __init__(self):
        self.menu = []
        self.clients_list = []

    def _find_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def _check_if_the_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def _check_if_meal_is_in_menu(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return True

    def _find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def _check_for_order(self, current_client):
        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

    def register_client(self, client_phone_number: str):
        client = self._find_client(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")
        current_client = Client(client_phone_number)
        self.clients_list.append(current_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        self._check_if_the_menu_is_ready()

        details_of_meals_in_menu = []
        for meal in self.menu:
            details_of_meals_in_menu.append(meal.details())
        return '\n'.join(details_of_meals_in_menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self._check_if_the_menu_is_ready()

        if not self._find_client(client_phone_number):
            self.register_client(client_phone_number)

        current_client = self._find_client(client_phone_number)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if not self._check_if_meal_is_in_menu(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = self._find_meal(meal_name)
            if current_meal.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {current_meal.name}!")

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            current_meal = self._find_meal(meal_name)
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * meal_quantity
            current_meal.quantity -= meal_quantity
            current_client.ordered_quantities[current_meal.name] =  meal_quantity

        ordered_meal_names = []
        for ordered_meal in current_client.shopping_cart:
            ordered_meal_names.append(ordered_meal.name)

        return f"Client {current_client.phone_number} successfully ordered " \
               f"{', '.join(ordered_meal_names)} for {current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client = self._find_client(client_phone_number)
        self._check_for_order(current_client)
        for meal_name, meal_quantity in current_client.ordered_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += meal_quantity

        current_client.shopping_cart = []
        current_client.ordered_quantities = {}
        current_client.bill = 0.0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client = self._find_client(client_phone_number)
        self._check_for_order(current_client)
        bill_to_be_paid = current_client.bill

        current_client.shopping_cart = []
        current_client.ordered_quantities = {}
        current_client.bill = 0.0

        FoodOrdersApp.receipt_id +=1
        return f"Receipt #{FoodOrdersApp.receipt_id} with total amount of " \
               f"{bill_to_be_paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
