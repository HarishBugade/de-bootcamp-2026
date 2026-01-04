import pandas as pd
from datetime import date

#---Cofiguration--#
project_id = "de-bootcamp-2026-483215"  
dataset_id = "bootcamp_dataset"
table_id = f"{dataset_id}.raw_transactions" #Creating a new Table

#---Extracting the Data---#
print(f"Extracting Data")
df = pd.read_csv("transactions.csv")

#---Adding an extra column into the file---#
df['Loaded_on'] = str(date.today())

#---Loading the data into BigQuery---#
df.to_gbq(
    destination_table = table_id,
    project_id = project_id,
    if_exists = 'replace',
    progress_bar = True
)

print(f"Mission Accomplished")