from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from settings import crypto_dict, cnx, cursor
import datetime


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


TABLES = {}
TABLES['crypto_table'] = (
    "CREATE TABLE `crypto_table` ("
    "  `name` varchar(20) NOT NULL,"
    "  `price` double(50) NOT NULL,"
    "  `date` DATE NOT NULL,"   
    "  PRIMARY KEY (`name`)")

add_crypto = ("INSERT INTO crypto_table "
              "(name, price, date) "
              "VALUES (%(name)s, %(price)s, %(date)s)")

date_now = datetime.now().date()

name = [
    crypto_dict['bitcoin'].naming,
    crypto_dict['ethereum'].naming,
    crypto_dict['ripple'].naming,
]

price = [
    crypto_dict['bitcoin'].pricing,
    crypto_dict['ethereum'].pricing,
    crypto_dict['ripple'].pricing,
]

data_crypto = {
    'name': name,
    'price': price,
    'date': date_now
}

cursor.execute(add_crypto, data_crypto)
cnx.commit()
cursor.close()
cnx.close()