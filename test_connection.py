import psycopg2

try:
    connection = psycopg2.connect(
        user="yosoypabloemilioescobargaviria1",
        password="Q2Z15776FGYzPS6UAzRR4hKSn8hKibW5",
        host="dpg-csp5tq0gph6c73dvqp4g-a.oregon-postgres.render.com",
        port="5432",
        database="flask_users"
    )
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    
    # Close the cursor and connection
    cursor.close()
    connection.close()
except Exception as e:
    print(f"Error: {e}")