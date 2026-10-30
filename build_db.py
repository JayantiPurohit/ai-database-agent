import sqlite3

# 1. Open the vault (this creates the file if it doesn't exist)
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# 2. Create the Employees Table (Define the columns)
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
''')

# 3. Add the HR data
employees = [
    (1, "Jayanti", "Engineering", 85000),
    (2, "Golu", "Data Science", 78000),
    (3, "Amit", "Marketing", 60000),
    (4, "Priya", "Engineering", 92000)
]

# Insert the data into the table safely
cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?)", employees)

# 4. Lock the vault and save
conn.commit()
conn.close()

print("Database 'company.db' built successfully!")