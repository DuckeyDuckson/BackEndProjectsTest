import sqlite3
import SignUp

def create_new_user(username, password):
    # 1. Connect to (or create) a database file
    conn = sqlite3.connect('accounts.db')
    cursor = conn.cursor()

    # 2. Create a table (if it doesn't already exist)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE CHECK (username <> ''),
            password_hash TEXT NOT NULL CHECK (password_hash <> '')
        
        )
    ''')

    # 3. Insert data safely (using ? placeholders to prevent SQL injection)
    try:
        new_user = (username, password)
        
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", new_user)
        # 4. Save (commit) the changes
        conn.commit()
        SignUp.MessageBox(True)
        
        
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed" in str(e):
            print(f"Error: The username '{username}' is already taken.")
        SignUp.MessageBox(False)
    # 5. Fetch data
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()  # Returns a list of tuples
    print(all_users)

    # 6. Close the connection
    conn.close()