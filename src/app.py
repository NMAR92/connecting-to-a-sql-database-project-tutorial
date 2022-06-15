

# 1) Connect to the database here using the SQLAlchemy's create_engine function
""" import psycopg2
conn = psycopg2.connect(database='dfdg4dhv111r3g',
                        user = 'ucawjmunifkppy',
                        password = '4df662170dc50a9eddffdf52e365decd2fe47deac8a82314bb1676ac375bc3ee',
                        host='ec2-54-157-16-196.compute-1.amazonaws.com',
                        port = 5432 )
cursor=conn.cursor()
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
cursor.execute("CREATE TABLE movies(id VARCHAR(2) PRIMARY KEY, title VARCHAR(30), rating INT);")
conn.commit()
conn.close() """
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
""" import psycopg2
conn = psycopg2.connect(database='dfdg4dhv111r3g',
                        user = 'ucawjmunifkppy',
                        password = '4df662170dc50a9eddffdf52e365decd2fe47deac8a82314bb1676ac375bc3ee',
                        host='ec2-54-157-16-196.compute-1.amazonaws.com',
                        port = 5432 )
cursor=conn.cursor()
cursor.execute("INSERT INTO movies(id , title , rating ) VALUES ('1', 'LA ERA DE HIELO', 1 ), ('2', 'LA ERA DE HIELO 2', 1 ), ('3', 'LA ERA DE HIELO 3', 1 );")
conn.commit()
conn.close() """
#PROGRES SENSIBLE A COMILLAS. LLEVA SIMPLE
# 4) Use pandas to print one of the tables as dataframes using read_sql function
import pandas as pd
import psycopg2
conn = psycopg2.connect(database='dfdg4dhv111r3g',
                        user = 'ucawjmunifkppy',
                        password = '4df662170dc50a9eddffdf52e365decd2fe47deac8a82314bb1676ac375bc3ee',
                        host='ec2-54-157-16-196.compute-1.amazonaws.com',
                        port = 5432 )
cursor=conn.cursor()
pd.read_sql("SELECT * FROM movies", conn)

conn.close()
