# ngo.py
from database import connect_db

class NGO:
    def __init__(self, name):
        self.name = name

    def request_food(self):
        conn = connect_db()
        cursor = conn.cursor()
        food = input("Enter food item you need: ")
        qty = int(input("Enter quantity: "))
        cursor.execute("INSERT INTO requests (ngo_name, food_item, quantity) VALUES (%s, %s, %s)",
                       (self.name, food, qty))
        conn.commit()
        conn.close()
        print("✅ Food request sent!")

    def view_requests(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requests WHERE ngo_name=%s", (self.name,))
        data = cursor.fetchall()
        conn.close()

        if not data:
            print("No requests yet.")
            return

        print("\n--- Your Requests ---")
        for r in data:
            print(f"ID: {r[0]} | Food: {r[2]} | Qty: {r[3]} | Status: {r[4]}")

    def view_available_donations(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM donations WHERE status='available'")
        data = cursor.fetchall()
        conn.close()

        if not data:
            print("No available donations.")
            return

        print("\n--- Available Donations ---")
        for d in data:
            print(f"ID: {d[0]} | Restaurant: {d[1]} | Food: {d[2]} | Qty: {d[3]}")

    def claim_donation(self):
        self.view_available_donations()
        donation_id = int(input("Enter the ID of the donation you want to claim: "))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE donations SET status='claimed', claimed_by_ngo=%s WHERE id=%s",
                       (self.name, donation_id))
        conn.commit()
        conn.close()
        print("✅ Donation claimed successfully!")
