# main.py
from database import setup_database, connect_db
from restaurant import Restaurant
from ngo import NGO
from admin import Admin

def sign_up():
    conn = connect_db()
    cursor = conn.cursor()
    print("\n--- SIGN UP ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (restaurant/ngo/admin): ").lower()

    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    if cursor.fetchone():
        print("⚠️ Username already exists!")
        conn.close()
        return

    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                   (username, password, role))
    conn.commit()
    conn.close()
    print("✅ Account created successfully!")

def sign_in():
    conn = connect_db()
    cursor = conn.cursor()
    print("\n--- SIGN IN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT role FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        role = user[0]
        print(f"✅ Login successful! Welcome, {username} ({role})")
        if role == "restaurant":
            restaurant_menu(Restaurant(username))
        elif role == "ngo":
            ngo_menu(NGO(username))
        elif role == "admin":
            admin_menu(Admin())
    else:
        print("❌ Invalid credentials.")

def restaurant_menu(restaurant):
    while True:
        print("\n--- RESTAURANT MENU ---")
        print("1. Donate Food")
        print("2. View My Donations")
        print("3. Accept NGO Request")
        print("4. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            restaurant.donate_food()
        elif choice == "2":
            restaurant.view_donations()
        elif choice == "3":
            restaurant.accept_request()
        else:
            break

def ngo_menu(ngo):
    while True:
        print("\n--- NGO MENU ---")
        print("1. Request Food")
        print("2. View My Requests")
        print("3. Claim Donation")
        print("4. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            ngo.request_food()
        elif choice == "2":
            ngo.view_requests()
        elif choice == "3":
            ngo.claim_donation()
        else:
            break

def admin_menu(admin):
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. View All Users")
        print("2. View All Donations")
        print("3. View All Requests")
        print("4. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            admin.view_all_users()
        elif choice == "2":
            admin.view_all_donations()
        elif choice == "3":
            admin.view_all_requests()
        else:
            break

# Main loop
if __name__ == "__main__":
    setup_database()

    while True:
        print("\n==== FOOD WASTE MANAGEMENT SYSTEM ====")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            sign_up()
        elif choice == "2":
            sign_in()
        else:
            print("👋 Exiting program. Goodbye!")
            break
