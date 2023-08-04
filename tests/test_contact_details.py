from pii_data.contact_details import ContactDetails 
import unittest
import datetime

class TestContactDetails(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestContactDetails, self).__init__(*args, **kwargs)
        self.contacts = ContactDetails()
        self.contacts.set_full_name()
        self.contacts.set_address()

    def test_phone_number(self):
        self.assertEqual(len(self.contacts.phone_number()) > 2, True)

    def test_mobile_number(self):
        self.assertEqual(len(self.contacts.mobile_number()) > 3, True)


    def test_email(self):
        self.assertEqual(len(self.contacts.email('Bill Gates')) > 3, True)
        self.assertEqual(len(self.contacts.email('Bill_Gates')) > 3, True)
    

    def test_date_of_birth(self):
        #self.assertEqual(len(self.contacts.date_of_birth(18, 99)) > 3, True)
        self.assertEqual(isinstance(self.contacts.date_of_birth(18, 99), datetime.date), True)        
      
    def test_full_name(self):
        self.assertEqual(len(self.contacts.get_full_name()) > 1, True)

    def test_prefix(self):
        self.assertEqual(len(self.contacts.get_prefix()) > 1, True)
    
    def test_first_name(self):
        self.assertEqual(len(self.contacts.get_first_name()) > 3, True)
    
    def test_last_name(self):
        self.assertEqual(len(self.contacts.get_last_name()) > 3, True)

    def test_address(self):
        self.assertEqual(len(self.contacts.get_address()) > 3, True)
    
    def test_street_address(self):
        self.assertEqual(len(self.contacts.get_street_address()) > 3, True)
   
    def test_city(self):
        self.assertEqual(len(self.contacts.get_city()) > 3, True)
    
    def test_county(self):
        self.assertEqual(len(self.contacts.get_county()) > 3, True)

    def test_postcode(self):
        self.assertEqual(len(self.contacts.get_postcode()) > 3, True)
    
    
if __name__ == '__main__':
    unittest.main()
    print('SUCCESS')
