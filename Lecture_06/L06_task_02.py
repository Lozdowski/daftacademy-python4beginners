# zadanie 2

import re


def validate_id_number(id_number):
      department = {'ZA', 'IT', 'KS', 'KA', 'LO', 'SP', 'MA', 'CZ', 'OC'}
      strr = re.compile('^([A-Z]{2}/\d{6}/\d{4})$')
      if( isinstance(id_number, str) and strr.match(id_number)
            and id_number[:id_number.find('/')] in department
            and 1900 <= int(id_number[-4:]) <= 2018
        ):
          return True
      else:
          return False


assert validate_id_number("SP/987543/2000") is True
assert validate_id_number("ZA/434503/2005") is True
assert validate_id_number("ZA/434503/2005 ") is False
assert validate_id_number("ble ble") is False
assert validate_id_number("ZA/43450/2005") is False
assert validate_id_number("XX/987654/2011") is False
assert validate_id_number("IT/34343/1800") is False
