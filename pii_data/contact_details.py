import names
import random
from faker import Faker
import re
from datetime import datetime
from datetime import date

class ContactDetails:

    def __init__(self):
        self.fake = Faker('en_GB')
        self.prefix=''
        self.first_name=''
        self.last_name=''
        self.street_address=''
        self.city=''
        self.county=''
        self.postcode=''

    def set_full_name(self):
        gender = ['male', 'female']
        selected_gender = gender[random.randint(0,1)]
        prefix=''
        first_name = ''
        last_name = ''

        if selected_gender == 'male':
            prefix = self.fake.prefix_male() 
            first_name = self.fake.first_name_male()
            last_name = self.fake.last_name()
            self.set_prefix(prefix)
            self.set_first_name(first_name)
            self.set_last_name(last_name)
            
        else:
            prefix = self.fake.prefix_female() 
            first_name = self.fake.first_name_female()
            last_name = self.fake.last_name()
            self.set_prefix(prefix)
            self.set_first_name(first_name)
            self.set_last_name(last_name)
            
        return prefix + ' ' + first_name + ' ' + last_name
    

    def phone_number(self):
        return self.fake.phone_number()

    def mobile_number(self):
        n=9
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return '07' + str(random.randint(range_start, range_end))


    def email(self, name):
        return re.sub("\s+", '_', name.lower())+'@' + self.fake.domain_name()
    

    def date_of_birth(self, min_age, max_age):
        month=str(self.fake.month())
        day = str(random.randint(1, 28))
        year = str(random.randint(datetime.today().year - max_age, datetime.today().year - min_age))

        return datetime.strptime(day+'-'+month+'-'+year, '%d-%m-%Y').date()


    def set_prefix(self, prefix):
        self.prefix = prefix
    
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name (self, last_name):
        self.last_name = last_name
    
    def get_full_name(self):
        return self.prefix + ' ' + self.first_name + ' ' + self.last_name

    def get_prefix(self):
        return self.prefix
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def age(self, dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    def set_address(self):
        self.street_address=self.fake.street_address()
        self.city=self.fake.city()
        self.county=self.fake.city_suffix().capitalize()
        self.postcode=self.fake.postcode()

    def get_address(self):
        return self.street_address + ', ' + self.city + ', ' + self.county + ', ' + self.postcode

    def set_street_address(self):
        self.street_address=self.fake.street_address()
    
    def get_street_address(self):
        return self.street_address

    def set_city(self):
        self.city=self.fake.city()

    def get_city(self):
        return self.city

    def set_county(self):
        self.county=self.fake.city_suffix().capitalize()

    def get_county(self):
        return self.county#.capitalize()

    def set_postcode(self):
        self.postcode=self.fake.postcode()
    
    def get_postcode(self):
        return self.postcode




   
