import random
from faker import Faker



class BankDetails:

    def __init__(self):
        self.fake = Faker('en_GB')

    def __number_generator(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return str(random.randint(range_start, range_end))

    def bank_account(self):
        return str(self.__number_generator(9))

    def sort_code(self, code=0):
        if code == 0:
            return str(self.__number_generator(6))
        else:
            return str(code) + str(self.__number_generator(4))

    def bank_name(self):
        bank_code=[]
        bank_name = []

        with open('pii_data/bank_name.txt') as f:
            for line in f:
                name, code = line.split(',')
                bank_name.append(name)
                bank_code.append(code.rstrip())
        
        index = random.randint(0,5)

        return bank_name[index], bank_code[index]

    def bank_address(self):
        return self.fake.address()

    def card_number(self):
        return self.fake.credit_card_number()