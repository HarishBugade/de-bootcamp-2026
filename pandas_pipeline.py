# import pandas as pd
# from datetime import date

# # 1. EXTRACT: Read the CSV (Pandas automatically handles headers and types!)
# input_path = r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv"
# df = pd.read_csv(input_path)

# # 2. TRANSFORM: Filter for positive amounts AND add the date column
# # This one line replaces your entire loop + try/except block
# df_clean = df[pd.to_numeric(df['amount'], errors='coerce') > 0].copy()
# df_clean['ingestion_date'] = str(date.today())

# # 3. LOAD: Save to a new CSV
# output_path = r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\pandas_transactions.csv"
# df_clean.to_csv(output_path, index=False)

# print("Pandas ETL Complete! That was easy.")

import pandas as pd
data = ({"Salary": [500, 600, 100]})
df = pd.DataFrame(data)
df_copy = df.copy()
df_copy["Salary"] = 111
print(df_copy)
print(df)