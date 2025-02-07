import sqlite3
x=sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
c=x.cursor()
c.execute(''' CREATE TABLE IF NOT EXISTS user
          (name text,username text,password text,age int,gender text)''')
c.execute('''CREATE TABLE IF NOT EXISTS sentiment_scores (
                 
                 username TEXT,
                 timestamp TEXT,
                 score INTEGER,
                 FOREIGN KEY(username) REFERENCES user(username))''')
x.commit()
x.commit()
x.close()
import sqlite3

def add_column_to_table():
    conn = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
    c = conn.cursor()

    # Add a new column to the 'user' table (if it doesn't already exist)
    c.execute("ALTER TABLE user ADD COLUMN button_progress TEXT")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
conn = sqlite3.connect(r"C:\Users\AMirMAhdi\Desktop\main project data base.db")
c = conn.cursor()

# Add a new column to the 'user' table (if it doesn't already exist)
c.execute("ALTER TABLE user ADD COLUMN button_active TEXT")

# Commit the changes and close the connection
conn.commit()
conn.close()
# Example usage

