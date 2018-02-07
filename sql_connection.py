from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
from settings import crypto_dict


cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1',database='my_connection')
cursor = cnx.cursor()

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
    "  PRIMARY KEY (`name`)")

add_crypto = ("INSERT INTO crypto_table "
              "(name, price) "
              "VALUES (%(name)s, %(price)s)")

nam = [
    crypto_dict['bitcoin'].naming,
    crypto_dict['ethereum'].naming,
    crypto_dict['ripple'].naming,
]

pric = [
    crypto_dict['bitcoin'].pricing,
    crypto_dict['ethereum'].pricing,
    crypto_dict['ripple'].pricing,
]

data_crypto = {
  'name': nam,
  'price': pric,
}

cursor.execute(add_crypto, data_crypto)
cnx.commit()
cursor.close()
cnx.close()