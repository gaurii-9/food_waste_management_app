# restaurant.py
from database import connect_db

class Restaurant:
    def __init__(self, name):
        self.name = name

    def donate_food(self):
        conn = connect_db()
        cursor = conn.cursor()
        food_item = input("Enter food item: ")
        quantity = int(input("Enter quantity: "))
        cursor.execute("INSERT INTO donations (restaurant_name, food_item, quantity) VALUES (%s, %s, %s)",
                       (self.name, food_item, quantity))
        conn.commit()
        conn.close()
        print("✅ Donation added successfully!")

    def view_donations(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM donations WHERE restaurant_name=%s", (self.name,))
        data = cursor.fetchall()
        conn.close()

        if not data:
            print("No donations yet.")
            return

        print("\n--- Your Donations ---")
        for d in data:
            print(f"ID: {d[0]} | Food: {d[2]} | Qty: {d[3]} | Status: {d[4]}")

    def view_pending_requests(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM requests WHERE status='pending'")
        data = cursor.fetchall()
        conn.close()

        if not data:
            print("No pending requests.")
            return

        print("\n--- Pending NGO Requests ---")
        for r in data:
            print(f"ID: {r[0]} | NGO: {r[1]} | Food: {r[2]} | Qty: {r[3]}")

    def accept_request(self):
        self.view_pending_requests()
        request_id = int(input("Enter the ID of the request you want to accept: "))
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE requests SET status='fulfilled', fulfilled_by_restaurant=%s WHERE id=%s",
                       (self.name, request_id))
        conn.commit()
        conn.close()
        print("✅ Request accepted successfully!")
