# zadanie 4

from collections import OrderedDict
from collections import defaultdict
from statistics import median
import csv
from datetime import date
from decimal import Decimal
from _sqlite3 import Row

in_filename = 'personal_data_homework.csv'
out_filename = 'clean_personal_data.csv'

def get_csv_lines(filename):
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter = ',')
        for row in reader:
            yield row

def save_csv(data):
    first_row = next(data)
    field_names = first_row.keys()
    with open(out_filename,'w',newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=field_names)
        csv_writer.writeheader()
        csv_writer.writerow(first_row)
        for row in data:
            csv_writer.writerow(row)
            
class PersonalDataCleaner:
    
    def clean(self,rows):
        for row in rows:
            clean_row = self._clean_all_items(row)
            
    
            clean_row['department'] = self._clean_department(clean_row['department'])

            clean_row['monthly_salary'] = self.clean_monthly_salary(clean_row['monthly_salary'])

            yield clean_row

    def _clean_all_items(self,row):
        clean_row = OrderedDict()
        for key, value in row.items():
            clean_value = value.strip()
            clean_value = clean_value or None
            clean_row[key] = clean_value
        return clean_row

    def _clean_department(self,department):
        if department is None:
          return None
        department = department[:2]
  
        return department
    def clean_monthly_salary(self,monthly_salary):
        if monthly_salary is None:
          return None
        monthly_salary = monthly_salary.replace(' ', '')
        monthly_salary = monthly_salary.replace(',', '.')
        for letter in 'plnPLNZŁzłotych':
          monthly_salary = monthly_salary.replace(letter, '')
        float(monthly_salary)
        return Decimal(monthly_salary).quantize(Decimal('0.01'))
               

def median_of_top_five(filename, department_name):
  
  rows = get_csv_lines(filename)
  cleaner = PersonalDataCleaner()
  people = cleaner.clean(rows)

  dep_salaries = defaultdict(list)
  for person in people:
    salary = person['monthly_salary']
    department = person['department']
    if department:
      dep_salaries[person['department']].append(salary)
    a = sorted(dep_salaries[department_name],reverse = True)[:5]
    
  return median(a).quantize(Decimal('0.01'))



assert median_of_top_five('personal_data_homework.csv', 'IT') == Decimal("9160.25")
assert median_of_top_five('personal_data_homework.csv', 'ZA') == Decimal("90640.00")
assert median_of_top_five('personal_data_homework.csv', 'LO') == Decimal("5104.84")
