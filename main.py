import csv


class Item:
    pay_rate = .8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run Validations to received arguments
        assert price >= 0, f"Price {price} is not grater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not grater than or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Property Decorator = Read-Only Attribute
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = (self.__price * increment_value) + self.__price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('itemslist.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # Count ou floats with .0, i.e: 5.0
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):

        # Super Function to attributes/methods
        super().__init__(name, price, quantity)

        # Run Validations to received arguments
        assert broken_phone >= 0, f"Broken Phone {broken_phone} is not grater than or equal to zero!"

        # Assign to self object
        self.broke_phone = broken_phone


item1 = Item("MyItem", 750)

# Setting an attributte
item1.name = "Other Item"

# Getting an attribute
print(item1.name)

item1.apply_increment(0.2)
item1.apply_discount()

phone1 = Phone("jscPhonev10", 500, 5, 1)
print(Item.all)
print(Phone.all)

print(item1.price)

