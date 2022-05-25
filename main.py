import sqlite3

connection = sqlite3.connect('autoShow.db')

cursor = connection.cursor()


# Создание таблиц.
def create_tables():
    # Создаем таблицу моделей.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Model
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  color TEXT NOT NULL,
                  horsepower INT NOT NULL,
                  torque INT NOT NULL,
                  year INT NOT NULL,
                  price INT NOT NULL
                  )''')

    # Создаем таблицу машин.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Car
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  name TEXT NOT NULL,
                  id_Model INTEGER DEFAULT NULL,
                  FOREIGN KEY (id_Model) REFERENCES Model (id)
                  )''')

    # Создаем таблицу покупатели.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Buyers
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  contact TEXT NOT NULL, 
                  name TEXT NOT NULL,
                  surname TEXT NOT NULL,
                  patronymic TEXT NOT NULL,
                  passport TEXT NOT NULL
                  )''')

    # Создаем таблицу сотрудники.
    cursor.execute('''CREATE TABLE IF NOT EXISTS employee
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  contact TEXT NOT NULL, 
                  name TEXT NOT NULL,
                  surname TEXT NOT NULL,
                  patronymic TEXT NOT NULL,
                  passport TEXT NOT NULL
                  )''')

    # Создаем таблицу продажи.
    cursor.execute('''CREATE TABLE IF NOT EXISTS Sales  
                  (id INTEGER NOT NULL PRIMARY KEY, 
                  id_employee INTEGER NOT NULL, 
                  id_car INTEGER NOT NULL,
                  id_buyers INTEGER NOT NULL,
                  FOREIGN KEY (id_employee) REFERENCES Employee (id),
                  FOREIGN KEY (id_car) REFERENCES Car (id),
                  FOREIGN KEY (id_buyers) REFERENCES Buyers (id)
                  )''')

    connection.commit()
    connection.close()
