import time
import pytest 

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
    



#### FIXTURES #### 
@pytest.fixture
def valid_currencies():
    print('Setting up the allowed currencies')
    return set(['GBP', 'CFA', 'Dollar', 'Yen', 'Euro'])  
    
@pytest.fixture
def conn():
    print('Setting up the database connection')
    _conn = get_db_conn()
    
    yield _conn
    
    print('Terminating the database connection \n')
    del _conn 
    

#### TESTS ####      
def test_debit(conn):
    print('\t *** TESTING DEBIT ***')
    account_id = 1
    amount = '150 GBP'
    # account = conn.get_account(account_id)
    # balance = account.balance

    # Transaction.debit(account, amount)

    # self.assertEqual(balance - amount, account.balance)

def test_convert_to_pound(valid_currencies):
    print('\t *** TESTING CONVERT_TO_POUND ***')
    amount = '150 Dollar'
    _, currency = amount.split(' ')
    assert currency in valid_currencies

    new_amount = Transaction.convert_to_pound(amount)
    _, new_currency = new_amount.split(' ')
    assert new_currency == 'GBP'