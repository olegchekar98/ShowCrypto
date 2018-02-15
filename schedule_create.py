import matplotlib.pyplot as plt
import mysql.connector
from settings import schedule_val

cnx = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='my_connection')
cursor = cnx.cursor()

class PaintSchedule():
    def __init__(self, name_numb):
        self.name_numb = name_numb
        self.query = ("SELECT price, date FROM my_connection "
                      "WHERE name = %s")

    def creating_schedule(self):
        cursor.execute(self.query, (self.name_numb))
        X = []
        Y = []
        for (price, date) in cursor:
            X.append({}.format(price))
            Y.append({}.format(date))

        plt.plot(X,Y, label = self.name_numb)

schedule_val['bitc'].creating_schedule()
schedule_val['eth'].creating_schedule()
schedule_val['rip'].creating_schedule()

plt.legend(loc=2)
plt.title('Crypto Currency')
plt.xlabel('Date')
plt.ylabel('Currency')
plt.show()

cursor.close()
cnx.close()