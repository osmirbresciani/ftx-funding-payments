import csv

# CONVERT TO CSV
def statement_to_csv(statement, filename, additional_info=None):    
    headers = []
    for key in statement[0]:
        headers.append(key)
    if additional_info:
        filename = f'{filename}-{additional_info}'
    with open(f'{filename}.csv', 'w') as file:
        mycsv = csv.writer(file, quoting=csv.QUOTE_ALL)
        mycsv.writerow(headers)
        for entry in statement:
            row = []
            for key in headers:
                row.append(entry[key])
            mycsv.writerow(row)
        file.close()