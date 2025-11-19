# Food Waste Management System

A command-line application to facilitate food donations from restaurants to NGOs, helping to reduce food waste and feed those in need.

## Features

- **User Authentication:** Secure sign-up and sign-in for different user roles.
- **Three User Roles:**
    - **Restaurant:** Donate surplus food, view donation history, and fulfill NGO requests.
    - **NGO:** Request specific food items, view request history, and claim available donations.
    - **Admin:** Monitor all system activity, including users, donations, and requests.
- **Real-time Updates:** Donation and request statuses are updated in real-time.

## Tech Stack

- **Backend:** Python
- **Database:** MySQL

## Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/DSA_project.git
    cd DSA_project
    ```

2.  **Install dependencies:**
    ```bash
    pip install mysql-connector-python
    ```

3.  **Set up the database:**
    - Make sure your MySQL server is running.
    - Open `database.py` and replace the placeholder credentials in the `connect_db` function with your MySQL details:
        ```python
        def connect_db():
            return mysql.connector.connect(
                host="YOUR_MYSQL_HOST",
                port="YOUR_MYSQL_PORT",
                user="YOUR_MYSQL_USER",
                password="YOUR_MYSQL_PASSWORD",
                database="YOUR_MYSQL_DATABASE"
            )
        ```
    - The application will automatically create the necessary tables (`users`, `donations`, `requests`) when it first runs.

## Usage

Run the main application from your terminal:

```bash
python main.py
```

You will be presented with a menu to either sign up or sign in.

### As a Restaurant:
- Donate food items and specify quantities.
- View a list of your past and current donations.
- Accept pending requests from NGOs.

### As an NGO:
- Request specific food items needed by your organization.
- View a list of your past and current requests.
- Browse and claim available donations from restaurants.

### As an Admin:
- Get a complete overview of all registered users, donations, and requests within the system.

## File Structure

```
.
├── admin.py          # Contains the Admin class and its methods
├── database.py       # Handles database connection and table setup
├── main.py           # Main entry point of the application
├── ngo.py            # Contains the NGO class and its methods
├── restaurant.py     # Contains the Restaurant class and its methods
└── user.py           # Contains the User class
```
