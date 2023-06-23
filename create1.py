import sqlite3

SUBTOPICS = [
    ('Reading', 'Read assigned chapters from the literature textbook', '9:00 AM', True),
    ('Research', 'Find scholarly articles related to the term paper topic', '11:00 AM', False),
    ('Writing', 'Write a draft of the introduction for the term paper', '1:00 PM', False),
    ('Practice', 'Solve math problems from the textbook', '3:00 PM', True),
    ('Review', 'Review class notes for upcoming quiz', '5:00 PM', False),
]

# Create a connection to the database
conn = sqlite3.connect('data/Study_Plan.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table to store the data
c.execute('''CREATE TABLE tasks
             (subtopic TEXT,
              description TEXT,
              time TEXT,
              completed BOOLEAN)''')

# Insert datas into table
c.executemany("INSERT INTO tasks VALUES (?,?,?,?)", SUBTOPICS)

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
