import sqlite3

class Databs:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS DATABASE (
            id INTEGER PRIMARY KEY,
            lname TEXT,
            fname TEXT,
            age INTEGER,
            CIN TEXT UNIQUE,
            job TEXT,
            city TEXT,
            mobile TEXT,
            Email TEXT
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, lname, fname, age, CIN, job, city, mobile, Email):
        self.cur.execute("INSERT INTO DATABASE (lname, fname, age, CIN, job, city, mobile, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                         (lname, fname, age, CIN, job, city, mobile, Email))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM DATABASE")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM DATABASE WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, lname, fname, age, CIN, job, city, mobile, Email):
        self.cur.execute("UPDATE DATABASE SET lname=?, fname=?, age=?, CIN=?, job=?, city=?, mobile=?, Email=? WHERE id=?",
                         (lname, fname, age, CIN, job, city, mobile, Email, id))
        self.con.commit()

    def Searchh(self, CIN):
        self.cur.execute("SELECT * FROM DATABASE WHERE CIN=?", (CIN,))
        return self.cur.fetchall()  # Return the fetched rows

    def close(self):
        self.con.close()  # Close the database connection
