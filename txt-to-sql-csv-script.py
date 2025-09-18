# parse_menu.py
import sqlite3
import csv

# --- Step 1: Read and parse the text file ---
menu_items = []
with open('MenuItems.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by double newlines to separate each item
items = content.strip().split('\n\n\n\n')  # looks like there are 4 newlines between items

for item in items:
    lines = [line.strip() for line in item.split('\n') if line.strip()]
    data = {}
    for line in lines:
        if line.startswith("Name:"):
            data['name'] = line.replace("Name:", "").strip()
        elif line.startswith("Price:"):
            data['price'] = float(line.replace("Price:", "").strip())
        elif line.startswith("Description:"):
            data['description'] = line.replace("Description:", "").strip()
        else:
            # Append extra lines to description
            data['description'] += " " + line.strip()
    menu_items.append(data)

# --- Step 2: Save to SQLite ---
conn = sqlite3.connect('menu.db')
c = conn.cursor()

# Create table
c.execute('''
CREATE TABLE IF NOT EXISTS Menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    description TEXT
)
''')

# Insert data
for item in menu_items:
    c.execute('''
    INSERT INTO Menu(name, price, description)
    VALUES (?, ?, ?)
    ''', (item['name'], item['price'], item['description']))

conn.commit()
conn.close()

# --- Step 3: Save to CSV ---
with open('MenuItems.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'price', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in menu_items:
        writer.writerow(item)

print("Data saved to menu.db and MenuItems.csv successfully!")
