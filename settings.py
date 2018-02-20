from config import CryptoCurrency
from schedule_create import PaintSchedule
import mysql.connector

cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='my_connection')
cursor = cnx.cursor()

crypto_dict = {
    'bitcoin' : CryptoCurrency(0),
    'ethereum' : CryptoCurrency(1),
    'ripple' : CryptoCurrency(2)
}

schedule_val = {
'bitc' : PaintSchedule('bitcoin'),
'eth' : PaintSchedule('ethereum'),
'rip' : PaintSchedule('ripple')
}






