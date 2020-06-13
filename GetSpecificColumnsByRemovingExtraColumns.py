import csv


cols_to_remove = [3] # Column indexes to be removed (starts at 0)

cols_to_remove = sorted(cols_to_remove, reverse=True) # Reverse so we remove from the end first
row_count = 0 # Current amount of rows processed
with open("D:/FYP/newsnet/dataset/politifact_real.csv", "r",encoding="utf-8") as source:
    reader = csv.reader(source)
    with open("I:/done/bt.csv", "a", newline='',encoding="utf-8") as result:
        writer = csv.writer(result)
        for row in reader:
            row_count += 1
            print('\r{0}'.format(row_count), end='') # Print rows processed
            for col_index in cols_to_remove:
                del row[col_index]
            writer.writerow(row)
