import sys
from us_visa.logger import logging

from us_visa.exception import USVisaException


try:
    a = 1 / 0
    print(a)
except Exception as ex:
    raise USVisaException(str(ex), sys)    
