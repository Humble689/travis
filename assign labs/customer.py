# customer.py
class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'Customer name: {self.name}\nAddress: {self.address}'