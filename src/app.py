import os
from dotenv import load_dotenv

load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function
import psycopg2
conn = psycopg2.connect(database=os.getenv('database'),
                        user = os.getenv('user'),
                        password = os.getenv('password'),
                        host=os.getenv('host'),
                        port = os.getenv('port') )
cursor=conn.cursor()
# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
cursor.execute("CREATE TABLE IF NOT EXISTS movies(id VARCHAR(2) PRIMARY KEY, title VARCHAR(30), rating INT);")
conn.commit()
conn.close()
# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
""" import psycopg2
conn = psycopg2.connect(database=os.getenv('database'),
                        user = os.getenv('user'),
                        password = os.getenv('password'),
                        host=os.getenv('host'),
                        port = os.getenv('port') )
cursor=conn.cursor()
cursor.execute("INSERT INTO movies(id , title , rating ) VALUES ('1', 'LA ERA DE HIELO', 1 ), ('2', 'LA ERA DE HIELO 2', 1 ), ('3', 'LA ERA DE HIELO 3', 1 );")
conn.commit()
conn.close() """
#SQLPROGRES SENSIBLE A COMILLAS. LLEVA COMILLAS SIMPLE

# 4) Use pandas to print one of the tables as dataframes using read_sql function
""" import pandas as pd
import psycopg2
conn = psycopg2.connect(database=os.getenv('database'),
                        user = os.getenv('user'),
                        password = os.getenv('password'),
                        host=os.getenv('host'),
                        port = os.getenv('port') )
cursor=conn.cursor()
pd.read_sql("SELECT * FROM movies", conn)

conn.close() """

#git rm env.local -- (PARA SACAR EL .env si no ya lo push y luego lo queres sacar)
