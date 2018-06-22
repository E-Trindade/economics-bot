import psycopg2
import config

def get_connection():
    conn = psycopg2.connect("dbname='"+ config.database +"' user='" + config.user + "' host='" + config.host + "' password='" + config.password + "'")
    conn.autocommit = True
    return conn

#setup database
def setup_database():
    db = get_connection()
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS chat_table(id SERIAL PRIMARY KEY, root_word VARCHAR(40), subject VARCHAR(40), verb VARCHAR(40), sentence VARCHAR(200))")
    cur.execute("CREATE TABLE IF NOT EXISTS statement_table(id SERIAL PRIMARY KEY, root_word VARCHAR(40), subject VARCHAR(40), verb VARCHAR(40), sentence VARCHAR(200))")
    cur.execute("CREATE TABLE IF NOT EXISTS question_table(id SERIAL PRIMARY KEY, root_word VARCHAR(40), subject VARCHAR(40), verb VARCHAR(40), sentence VARCHAR(200))")
    cur.execute("CREATE TABLE IF NOT EXISTS directions_table(id SERIAL PRIMARY KEY, origin_location VARCHAR(100), destination_location VARCHAR(100))")
