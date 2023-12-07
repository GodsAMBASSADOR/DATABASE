import sqlite3 as sql
from sqlite3 import Error

conn = sql.connect("skillbridge.db")
cur = conn.cursor()


def main():
    def User():
        query = '''CREATE TABLE IF NOT EXISTS User(
            User_id INT PRIMARY KEY NOT NULL, 
            first_name VARCHAR(20) not null,
            last_name VARCHAR(20) not null,
            skills VARCHAR(30) not null,
            prefrences text(100) not null); '''
        
        cur.execute(query)
        conn.commit()
     

    def Skill():
        query = '''CREATE TABLE IF NOT EXISTS Skill(
        Skill_id INT PRIMARY KEY NOT NULL,
        name VARCHAR(20) not null,
        category VARCHAR(30) not null,
        description VARCHAR(100) NOT NULL
        );'''
        cur.execute(query)
        conn.commit() 
        

    def Listing():
        query = '''CREATE TABLE IF NOT EXISTS Listings(
        skill VARCHAR(20) not null,
        user VARCHAR(30) not null,
        additional_info VARCHAR(100) NOT NULL,
        User_id INT NOT NULL,
        FOREIGN KEY (User_id) REFERENCES User(User_id)
        );'''
        cur.execute(query)
        conn.commit()
        

    def Request():
        query = '''CREATE TABLE IF NOT EXISTS Request(
        requested_skill VARCHAR(20) not null,
        user VARCHAR(30) not null,
        requirements VARCHAR(100) not null,
        User_id INT NOT NULL,
        FOREIGN KEY (User_id) REFERENCES User(User_id)
        );'''
        cur.execute(query)
        conn.commit()
        

    def Transact():
        query = '''CREATE TABLE IF NOT EXISTS Transact(
        user_1 VARCHAR(20) not null,
        user_2 VARCHAR(20) not null,
        skills_exchanged VARCHAR(100) not null,
        feedback text(100) not null,
        User_id INT NOT NULL,
        Skill_id INT NOT NULL,
        FOREIGN KEY (User_id) REFERENCES User(User_id),
        FOREIGN KEY (Skill_id) REFERENCES Skill(Skill_id)
        );'''
        cur.execute(query)
        conn.commit()
        

    def Rating():
        query = '''CREATE TABLE IF NOT EXISTS Rating(
        
        User_giving_rating VARCHAR(20) not null,
        User_recieving_rating VARCHAR(20) not null,
        rating_value VARCHAR(100) NOT NULL,
        User_id INT NOT NULL,
        FOREIGN KEY (User_id) REFERENCES User(User_id)
        );'''
        cur.execute(query)
        conn.commit()
        conn.close()

    return User(), Skill(), Listing(), Request(), Transact(), Rating()

if __name__ == "__main__":
    main()






