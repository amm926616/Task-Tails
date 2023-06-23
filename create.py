import sqlite3

SUBTOPICS = [    ('Exercise', 'Go for a 30-minute run in the morning', '6:00 AM', True),   ('Work', 'Complete the sales report for Q1', '10:00 AM', False),    ('Groceries', 'Buy milk, bread, and eggs from the supermarket', '12:00 PM', False),    ('Study', 'Review notes for the upcoming exam', '2:00 PM', True),    ('Clean', 'Vacuum and dust the living room', '4:00 PM', False),    ('Exercise', 'Do 50 jumping jacks', '6:00 PM', False),    ('Work', 'Attend the team meeting', '10:00 AM', True),    ('Groceries', 'Buy fruits and vegetables from the farmer\'s market', '11:00 AM', True),    ('Study', 'Practice solving math problems', '3:00 PM', False),    ('Clean', 'Clean the bathroom', '5:00 PM', True),]

# Create a connection to the database
conn = sqlite3.connect('data/Daily_Schedule.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create a table to store the data
c.execute('''CREATE TABLE tasks
             (subtopic TEXT,
              description TEXT,
              time TEXT,
              completed BOOLEAN)''')

# Insert into table
c.executemany("INSERT INTO tasks VALUES (?,?,?,?)", SUBTOPICS)

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
