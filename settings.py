from config import CryptoCurrency
from schedule_create import PaintSchedule
import mysql.connector
import urllib.request

cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='my_connection')
cursor = cnx.cursor()

data = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=10")

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






