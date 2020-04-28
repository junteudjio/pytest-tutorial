import time
import unittest

class Transaction():
    @staticmethod 
    def convert_to_pound(amount):
         return 'NEW_AMOUNT GBP'
    
    @staticmethod 
    def debit(account, amount):
        pass

def get_db_conn():
    time.sleep(2.5)
    return 'db-conn'
    

class TestTransaction(unittest.TestCase):
    def setUp(self):
        print('Setting up the database connection')
        self._conn = get_db_conn()
        
        print('Setting up the allowed currencies')
        self._valid_currencies = set(['GBP', 'CFA', 'Dollar', 'Yen', 'Euro'])

    def tearDown(self):
        print('Terminating the database connection \n')
        del self._conn
        
        
    def test_debit(self):
        print('\t *** TESTING DEBIT ***')
        account_id = 1
        amount = '150 GBP'
        # account = self._conn.get_account(account_id)
        # balance = account.balance
        
        # Transaction.debit(account, amount)
        
        # self.assertEqual(balance - amount, account.balance)
    
    def test_convert_to_pound(self):
        print('\t *** TESTING CONVERT_TO_POUND ***')
        amount = '150 Dollar'
        _, currency = amount.split(' ')
        self.assertTrue(currency in self._valid_currencies)

        new_amount = Transaction.convert_to_pound(amount)
        _, new_currency = new_amount.split(' ')
        self.assertEqual(new_currency, 'GBP')
        
        
if __name__ == '__main__':
    unittest.main()