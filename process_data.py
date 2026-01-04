# file = open(r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv", "r")
# with file as f:
#     for line in f:
#         print(f"{line}")

file = r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv"
output_file = r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\cleaned_transactions.csv"
# def clean_data(file, output_file):
#     cleaned_data = []
#     with open(file, "r") as f:
#         header = next(f)
#         for line in f:
#             line = line.strip()
#             split_line = line.split(",")
#             try:
#                 int_line = int(split_line[1])

#             except ValueError:
#                 print(f"Sipping the garbage line:{line}")
#                 continue

#             if int_line > 0:
#                 cleaned_data.append(split_line)

#     with open(output_file, "w") as f_out:
#         f_out.write(header)
#         for row in cleaned_data:
#             f_out.write(",".join(row) + "\n")
        
#     print("Data cleaning complete.")

# clean_data(r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\transactions.csv", r"C:\Users\harsh\anaconda3\Lib\site-packages\jupyter_server\services\de_bootcamp\cleaned_transactions.csv")


def extract_data(file):
    raw_data = []
    with open(file, "r") as f:
       header = next(f)
       for line in f:
           line  = line.strip()
           raw_data.append(line.split(","))
    return header, raw_data

def transform_data(header, raw_data):
    from datetime import date
    trans = []
    for t in raw_data:
        try:
            if int(t[1]) > 0:
                today = str(date.today()) 
                t.append(today)
                trans.append(t)
        except ValueError:
            print(f"Skipping garbage line: {t}")
            continue
    return trans

def load_data(output_file, header, trans):
    with open(output_file, "w") as f_out:
        f_out.write(header.strip() + ",Batch_Date\n")
        for line in trans:
            f_out.write(",".join(line) + "\n")
    print(f"ETL process complete.")
                
header, raw_data = extract_data(file = file)
trans = transform_data(header, raw_data)
load_data(output_file = output_file, header = header, trans = trans)