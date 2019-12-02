class HongKongTaxi:

    def __init__(self, customers=[]):
        self.customers = customers 

    def pick(self, name):
        self.customers.append(name) 

    def drop(self, name):
        self.customers.remove(name)

taxi1 = HongKongTaxi(['Alpha', 'Beta'])
taxi1.customers
taxi1.pick('Charlie')
taxi1.drop('Alpha')
taxi1.customers
taxi2 = HongKongTaxi()
taxi2.pick('Carrie')
taxi2.customers
taxi3 = HongKongTaxi()
print(taxi3.customers)
taxi3.pick('Delta')


class HongKongTaxi2:

    def __init__(self, customers):
        self.customers = customers

    def pick(self, name):
        self.customers.append(name)

    def drop(self, name):
        self.customers.remove(name)

taxi1 = HongKongTaxi2(['Alpha', 'Beta'])
taxi1.customers
taxi1.pick('Charlie')
taxi1.drop('Alpha')
taxi1.customers
taxi2 = HongKongTaxi2([])
taxi2.pick('Carrie')
print(taxi2.customers)
taxi2.customers
taxi3 = HongKongTaxi2([])
print(taxi3.customers)
taxi3.pick('Delta')
