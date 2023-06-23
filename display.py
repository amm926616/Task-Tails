import sqlite3

# Connect to the database and create a cursor object
conn = sqlite3.connect('data/data0.db')
c = conn.cursor()

# Retrieve the main topic from the maintopic table
c.execute("SELECT * FROM maintopic")
maintopic = c.fetchone()[0]

# Retrieve the tasks from the tasks table
c.execute("SELECT * FROM tasks")
tasks = c.fetchall()

# Print the main topic
print(maintopic)
print("=" * len(maintopic))

# Print the tasks
for task in tasks:
    print(f"{task[0]} \n {task[1]} \n {task[2]} \n {task[3]} \n")

# Close the connection
conn.close()
