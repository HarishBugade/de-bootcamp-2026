import pandas as pd
from datetime import date
from sqlalchemy import create_engine, text

# --- CONFIGURATION ---
# input_path = r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv"
# # This creates a database file named 'my_warehouse.db' in your folder
# db_engine = create_engine(r"sqlite:///C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\my_warehouse.db")

# # 1. EXTRACT
# print("Extracting data...")
# df = pd.read_csv(input_path)

# # 2. TRANSFORM
# print("Transforming data...")
# # The Clean One-Liner (with .copy()!)
# df_clean = df[pd.to_numeric(df['amount'], errors='coerce') > 0].copy()
# df_clean['ingestion_date'] = str(date.today())

# # 3. LOAD (The SQL Step)
# print("Loading to Database...")
# # Instead of to_csv, we use to_sql
# df_clean.to_sql(
#     name='clean_transactions', # The Table Name
#     con=db_engine,             # The Connection
#     if_exists='replace',       # If table exists, drop it and create new
#     index=False                # Don't save the row numbers
# )

# print("Success! Data is now inside a SQL Database.")

# # --- ANALYTICS VERIFICATION ---
# print("\n--- Running SQL Query ---")

# # We write actual SQL syntax here
# sql_query = "SELECT sum(amount) as Total_Revenue FROM clean_transactions"

# # Pandas runs the SQL for us and returns the answer
# result = pd.read_sql(sql_query, db_engine)

# print(result)


# input_path = r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv"
# # This creates a database file named 'mySQLite_warehouse.db' in your folder
# db_engine = create_engine(r"sqlite:///C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\mywarehouse.db")
# db_engine_dup = create_engine(r"sqlite:///C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\mySQLite_warehouse.db")
# df = pd.read_csv(input_path)
# df_clean = df[pd.to_numeric(df['amount'], errors = 'coerce') >0 ].copy()
# df_clean['ingestion_date'] = str(date.today())

# df_clean.to_sql(
#     name = 'clean_transactins',
#     con = db_engine,
#     if_exists = 'replace',
#     index = False)
# print(f"ELT successful and Data loaded into the SQL lite database")

# sql_query = "select sum(amount) as Total_Revenue from clean_transactions"
# result = pd.read_sql(sql_query, db_engine)
# print(result)

# with db_engine.begin() as conn:
#     conn.execute(text("DROP TABLE clean_transactins"))
#     conn.commit()
#     print("clean_transactins table dropped successfuly")


    