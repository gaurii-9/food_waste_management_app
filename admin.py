# admin.py
from database import connect_db

class Admin:
    def __init__(self):
        pass

    def view_all_users(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, role FROM users")
        data = cursor.fetchall()
        conn.close()

        print("\n--- All Users ---")
        for user in data:
            print(f"ID: {user[0]} | Username: {user[1]} | Role: {user[2]}")

    def view_all_donations(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM donations")
        data = cursor.fetchall()
        conn.close()

        print("\n--- All Donations ---")
        for d in data:
            print(f"ID: {d[0]} | Restaurant: {d[1]} | Food: {d[2]} | Qty: {d[3]} | Status: {d[4]}")

    def view_all_requests(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requests")
        data = cursor.fetchall()
        conn.close()

        print("\n--- All Requests ---")
        for r in data:
            print(f"ID: {r[0]} | NGO: {r[1]} | Food: {r[2]} | Qty: {r[3]} | Status: {r[4]}")
