# zadanie 1

from collections import Counter
import csv

def count_unique_id_numbers_before_clean(data = 'personal_data_homework.csv' ):
    unique = list()
    with open (data) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter= ',')
        headers = next(csv_reader)
        for row in csv_reader:
            unique.append(row[2])
        
        uniq_lst = list()
        for id in unique:
            if id not in uniq_lst:
                uniq_lst.append(id)
        return len(uniq_lst)



assert count_unique_id_numbers_before_clean('personal_data_homework.csv') == 1588
