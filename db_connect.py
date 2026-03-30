import psycopg

# 1. Define how to find your database
# Use the credentials we set up earlier
DB_PARAMS = "dbname=aegis_vault user=shivansh password=aftermeth host=localhost"

def test_connection():
    try:
        # 2. 'with' ensures the connection closes even if the code crashes
        with psycopg.connect(DB_PARAMS) as conn:
            
            # 3. The Cursor is like your "hand" that sends the SQL
            with conn.cursor() as cur:
                print("--- Connection Successful! ---")
                
                # Let's ask the database for the current time as a test
                cur.execute("SELECT NOW();")
                db_time = cur.fetchone()
                print(f"PostgreSQL Server Time: {db_time[0]}")

    except Exception as e:
        print(f"❌ Connection failed: {e}")

if __name__ == "__main__":
    test_connection()