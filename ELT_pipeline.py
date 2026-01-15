import pandas as pd
from datetime import date
from google.cloud import bigquery
from psutil import users
from datetime import date

#---Cofiguration--#
project_id = "de-bootcamp-2026-483215"  
dataset_id = "bootcamp_dataset"
table_id = f"{dataset_id}.raw_users" #Creating a new Table

#--connectting to BigQuery--#
client = bigquery.Client(project = project_id)


def load_to_bq(csv_name, table_name):
    #---Extracting and loading the Data---#
    print(f"Extracting Data")
    try:
        df = pd.read_csv("csv_name")
        print(f"Loaded {csv_name} wit {len(df)} rows")
    except FileNotFoundError:
        print("No csv found")
        return 
    
    #--Creating the path(Address to load the table)--#
    target_path = project_id + "." + dataset_id + "." + table_name

    #--Configuring the settings--#
    job_config = bigquery.LoadJobConfig(
        write_disposition = "WRITE_TRUNCATE",
        autodetect = True
    )


    #--Uploading--#
    print("Uploading " + table_name)
    job = client.load_data_from_dataframe(df, target_path, job_config = job_config)
    job.result()


load_to_bq("transactions.csv", "raw_transactions")
load_to_bq("users.csv", "raw_users")

# try:
#     df = pd.read_csv("users.csv")
#     print(f"Loaded {users.csv} with {len(df)} records")
# except:
#     print(f"No csv found")

# #---Adding an extra column into the file---#
# df['Loaded_on'] = str(date.today())

# #---Loading the data into BigQuery---#
# df.to_gbq(
#     destination_table = table_id,
#     project_id = project_id,
#     if_exists = 'replace',
#     progress_bar = True
# )

# print(f"Mission Accomplished")