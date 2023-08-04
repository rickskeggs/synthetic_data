from pii_data.bank_details import BankDetails 
import unittest

class TestBankDetails(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBankDetails, self).__init__(*args, **kwargs)
        self.account = BankDetails()

    def test_bank_account(self):    
        self.assertEqual(len(self.account.bank_account()) > 2, True)
        
    def test_bank_name(self):
        self.assertEqual(len(self.account.bank_name()[0]) > 2, True)
        #self.assertEqual(len(self.account.bank_name()[1]) == 2, True)

    def test_bank_address(self):
        self.assertEqual(len(self.account.bank_address()) > 2, True)
        

    def test_card_number(self):
        self.assertEqual(len(self.account.card_number()) > 2, True)

if __name__ == '__main__':
    unittest.main()
    print('SUCCESS')
