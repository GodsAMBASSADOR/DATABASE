import sqlite3 as sql
from sqlite3 import Error

conn = sql.connect("skillbridge.db")
cur = conn.cursor()


def main():
    def User():
        query = '''CREATE TABLE IF NOT EXISTS User(
            id INT NOT NULL PRIMARY KEY, 
            first_name VARCHAR(20) not null,
            last_name VARCHAR(20) not null,
            skills VARCHAR(30) not null,
            prefrences text(100) not null); '''
        
        cur.execute(query)

        update = input("Are you a New User (y/n)").lower()
        if update == 'n':
            pass
        else:
            first = input("Enter First name: ")
            last = input("Enter Last name: ")
            skills = input("Enter your current skillset(s)")
            prefrences = input("Enter your Prefrence: ")
            cur.execute("INSERT INTO User (first_name , last_name, skills , prefrences) VALUES (?, ?, ?, ?)", 
                    (first, last, skills, prefrences))
        
        conn.commit()
    

    def Skill():
        query = '''CREATE TABLE IF NOT EXISTS Skill(
        name VARCHAR(20) not null,
        category VARCHAR(30) not null,
        description VARCHAR(100) NOT NULL
        );'''
        cur.execute(query)

        update = input("Have you Updated details of your skillset (y/n)").lower()
        if update == 'y':
            pass
        else:
            print("Please do if you have not!")
            name = input("Enter the name of your Skill: ")
            category = input("Enter it's category e.g writing: ")
            description = input("Enter it's Description: ")
            cur.execute("INSERT INTO User (name , category , description) VALUES (?, ?, ?)", 
                        (name, category, description))
        conn.commit()
        

    def Listing():
        query = '''CREATE TABLE IF NOT EXISTS Listings(
        skill VARCHAR(20) not null,
        user VARCHAR(30) not null,
        additional_info VARCHAR(100) NOT NULL
        );'''
        cur.execute(query)
        conn.commit()
        

    def Request():
        query = '''CREATE TABLE IF NOT EXISTS Request(
        requested_skill VARCHAR(20) not null,
        user VARCHAR(30) not null,
        requirements VARCHAR(100) not null
        );'''
        cur.execute(query)
        conn.commit()
        

    def Transaction():
        query = '''CREATE TABLE IF NOT EXISTS Transaction(
        User1 VARCHAR(20) not null,
        User2 VARCHAR(20) not null,
        skills_exchanged VARCHAR(100) not null
        feedback text(150) not null
        );'''
        cur.execute(query)
        conn.commit()
        

    def Rating():
        query = '''CREATE TABLE IF NOT EXISTS Rating(
        User_giving_rating VARCHAR(20) not null,
        User_recieving_rating VARCHAR(20) not null,
        rating_value VARCHAR(100) NOT NULL
        );'''
        cur.execute(query)
        conn.commit()
        conn.close()

    return User(), Skill(), Listing(), Request(), Transaction(), Rating()

if __name__ == "__main__":
    main()






