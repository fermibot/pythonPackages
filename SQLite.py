import sqlite3
import random
from functions import random_functions


connection = sqlite3.connect('example.db')
c = connection.cursor()

try:
    c.execute("DROP TABLE stocks")
    print("Dropped the table stocks")
except FileNotFoundError:
    print("There is not such table in the current database")

c.execute("CREATE TABLE stocks (date TEXT, trans TEXT, symbol TEXT, qty REAL, price REAL)")
c.execute("INSERT INTO stocks VALUES ('2016-1-05', 'Buy', 'RHAT', 100, 35.14)")


def random_date():
    month_input = random.randint(1, 12)
    year_input = random.randint(1900, 2070)
    if month_input in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month_input in [4, 6, 9, 11]:
        days = 30
    elif month_input == 2:
        if divmod(year_input, 4) == 0:
            days = 29
        else:
            days = 28
    return "'" + str(year_input) + "-" + str(month_input) + "-" + str(days) + "'"


def punctuation_remover(word_input):
    for punctuation in [",", "a", "e", "i", "o", "u", "\n"]:
        word_input = word_input.replace(punctuation, "")
    word_input = word_input.upper()
    return word_input


def buy_sell():
    return random.choice(["Buy", "Sell"])


lines = open('sample_data.txt', 'r').readlines()
words = open('sample_nouns.txt', 'r').readlines()

for i in range(0, len(lines)):
    try:
        c.execute("INSERT INTO stocks VALUES " + lines[i])
    except:
        print("Failed to insert row number " + str(i + 2) + " to the table stocks")


def database_count():
    for obj in c.execute("SELECT COUNT(*) FROM stocks"):
        return obj[0]


print("Processed a total number of " + str(database_count()) + "  records into the table 'stocks'.")

for word in words:
    c.execute(
        "INSERT INTO stocks VALUES (" + random_date() + ", " + word + punctuation_remover(word) + ", "
        + str(random.randint(1, 2500)) + ", " + str(round(random.uniform(1, 25000), 2)) + ")")

connection.commit()

