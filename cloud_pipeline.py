import pandas as pd
from datetime import date
import os

project_id = "de-bootcamp-2026-483215"
table_id = "bootcamp_dataset.clean_transactions"

print ("Extracting  Data...")
df = pd.read_csv(r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv")

print ("Transforming Data...")
df_clean = df[pd.to_numeric(df['amount'], errors = 'coerce') > 0].copy()
df_clean['ingestion_Date'] = str(date.today())

print ("Loading into BigQuery...")
df_clean.to_gbq(
    destination_table = table_id,
    project_id = project_id,
    progress_bar = True,
    if_exists = 'replace'
)

print("ELT successfull and the date is finally in BigQuery")