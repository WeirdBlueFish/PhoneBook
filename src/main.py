import sqlite3

conn = sqlite3.connect("PhoneBook.db")
cursor = conn.cursor()

create_table = '''

CREATE TABLE IF NOT EXISTS phonebook
(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
 name TEXT NOT NULL,
 lname TEXT NOT NULL,
 number TEXT NOT NULL)            
'''

cursor.execute(create_table)
conn.commit()

class PHONEBOOK:
    def __init__(self, name, lname, number, id = None):
        self.__id = id
        self.name = name
        self.lname = lname
        self.number = number

    def getName(self):
        return self.name
    def getLname(self):
        return self.lname
    def getNumber(self):
        return self.number
    
    def setName(self, k):
        self.name = k
     
    def setLname(self, k):
        self.lname = k

    def setNumber(self, k):
        self.number = k


    def add(self):
        cursor.execute("INSERT INTO phonebook(name, lname, number) VALUES (?,?,?)",
                       (self.getName(), self.getLname(), self.getNumber()))
        conn.commit()

    def delete(self, name):
        cursor.execute("DELETE FROM phonebook where name = ?", (name,))
        conn.commit()

    def readAll(self):
        cursor.execute("SELECT * FROM phonebook")
        output = cursor.fetchall()
        return output
    
    def readOne(self, name):
        cursor.execute("SELECT * FROM phonebook where name = ?", (name,))
        output = cursor.fetchall()
        return output
    
    def updateRec(self, id, name, lname, number):
        cursor.execute("UPDATE phonebook SET name = ? , lname = ? , number = ? WHERE id = ?",
                    (id, name, lname, number))
        conn.commit()


