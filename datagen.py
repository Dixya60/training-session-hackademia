import os
import csv
import json
import random
from datetime import datetime, timedelta

BASE_DIR = "assignment_data"

def ensure(path):
    os.makedirs(path, exist_ok=True)

# -------------------------------------------------
# 1. LOG FILES
# -------------------------------------------------
def generate_logs():
    log_dir = os.path.join(BASE_DIR, "logs")
    ensure(log_dir)

    levels = ["INFO", "WARNING", "ERROR"]
    messages = [
        "Database connection failed",
        "User logged in",
        "Disk space low",
        "Invalid credentials",
        "Service started",
    ]

    start = datetime.now()

    for i in range(1, 3):
        with open(f"{log_dir}/app{i}.log", "w") as f:
            for _ in range(40):
                if random.random() < 0.1:
                    f.write("MALFORMED LINE WITHOUT FORMAT\n")
                    continue
                ts = (start + timedelta(seconds=random.randint(0, 5000))).strftime("%Y-%m-%d %H:%M:%S")
                level = random.choice(levels)
                msg = random.choice(messages)
                f.write(f"{ts} [{level}] {msg}\n")

# -------------------------------------------------
# 2. CONTACTS TEXT FILE
# -------------------------------------------------
def generate_contacts():
    lines = [
        "Alice, alice@gmail.com, 123-456-7890",
        "Bob, bob[at]mail.com, 999999",
        "Charlie, charlie@yahoo.com, (555) 123-4567",
        "Invalid random text line",
        "Daisy, daisy@mail.com, 111-222-3333",
        "Alice, alice@gmail.com, 123-456-7890",
    ]
    with open(f"{BASE_DIR}/contacts.txt", "w") as f:
        f.write("\n".join(lines))

# -------------------------------------------------
# 3. MESSY CSV
# -------------------------------------------------
def generate_messy_csv():
    rows = [
        ["id", "name", "marks"],
        ["1", "Alice", "85"],
        ["2", "Bob", ""],
        ["3", "Charlie", "ninety"],
        ["4", "Daisy", "72"],
        ["5", "Evan", ""],
    ]
    with open(f"{BASE_DIR}/students_raw.csv", "w", newline="") as f:
        csv.writer(f).writerows(rows)

# -------------------------------------------------
# 4. NESTED JSON
# -------------------------------------------------
def generate_nested_json():
    users = []
    for uid in range(1, 10):
        users.append({
            "user_id": uid,
            "profile": {
                "name": f"user{uid}",
                "activity": [
                    {"action": random.choice(["login", "logout", "purchase"]), "count": random.randint(1, 20)}
                    for _ in range(10)
                ]
            }
        })
    with open(f"{BASE_DIR}/users.json", "w") as f:
        json.dump(users, f, indent=2)

# -------------------------------------------------
# 5. CREDENTIALS CSV
# -------------------------------------------------
def generate_credentials():
    rows = [
        ["username", "password", "email"],
        ["alice1", "Password@123", "alice@gmail.com"],
        ["1bob", "short", "bob@mail"],
        ["charlie_", "ValidPass#99", "charlie@yahoo.com"],
        ["Daisy", "NoSpecial123", "daisy@mail.com"],
    ]
    with open(f"{BASE_DIR}/credentials.csv", "w", newline="") as f:
        csv.writer(f).writerows(rows)

# -------------------------------------------------
# 6. INVENTORY SNAPSHOTS
# -------------------------------------------------
def generate_inventory():
    t1 = [["item", "quantity"], ["apple", "50"], ["banana", "30"], ["orange", "20"]]
    t2 = [["item", "quantity"], ["apple", "45"], ["banana", "30"], ["grape", "15"]]

    with open(f"{BASE_DIR}/inventory_t1.csv", "w", newline="") as f:
        csv.writer(f).writerows(t1)

    with open(f"{BASE_DIR}/inventory_t2.csv", "w", newline="") as f:
        csv.writer(f).writerows(t2)

# -------------------------------------------------
# 7. DIRECTORY STRUCTURE
# -------------------------------------------------
def generate_directory():
    base = f"{BASE_DIR}/sample_dir"
    ensure(f"{base}/subdir")

    files = [
        f"{base}/a.txt",
        f"{base}/b.log",
        f"{base}/subdir/c.csv",
    ]

    for path in files:
        with open(path, "w") as f:
            f.write("dummy content in which differnt operations will b performed for the tasks\n")

# -------------------------------------------------
# 8. TEXT FILES
# -------------------------------------------------
def generate_texts():
    text_dir = f"{BASE_DIR}/texts"
    ensure(text_dir)

    texts = [
        "Python is great and Python is fast. Python uses interpretor and code is parsed line by line",
        "Data science uses Python and statistics",
    ]

    for i, t in enumerate(texts, 1):
        with open(f"{text_dir}/doc{i}.txt", "w") as f:
            f.write(t)

# -------------------------------------------------
# 9. JSON DATA FILES
# -------------------------------------------------
def generate_json_data():
    json_dir = f"{BASE_DIR}/json_data"
    ensure(json_dir)

    data = [
        {"id": 1, "name": "Alice", "email": "alice@mail.com"},
        {"id": 2, "username": "bob", "age": 25},
    ]

    for i, obj in enumerate(data, 1):
        with open(f"{json_dir}/data{i}.json", "w") as f:
            json.dump(obj, f, indent=2)

# -------------------------------------------------
# 10. UNSTRUCTURED TEXT
# -------------------------------------------------
def generate_unstructured():
    text = """
Contact admin at admin@example.com or support@mail.org
Server at 192.168.1.1 failed on 2024-10-05
Random garbage line
Another IP 10.0.0.25 logged on 05/12/2023
"""
    with open(f"{BASE_DIR}/raw_dump.txt", "w") as f:
        f.write(text)

# -------------------------------------------------
# MAIN
# -------------------------------------------------
def main():
    ensure(BASE_DIR)

    generate_logs()
    generate_contacts()
    generate_messy_csv()
    generate_nested_json()
    generate_credentials()
    generate_inventory()
    generate_directory()
    generate_texts()
    generate_json_data()
    generate_unstructured()

    print("✅ All assignment data generated successfully.")

if __name__ == "__main__":
    main()
