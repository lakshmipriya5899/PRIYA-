import re

def validate(number):
    if(re.search(r'^\+?\d{3}-?\d{3}-?\d{4}$|^0?\d{3}-?\d{3}-?\d{4}$|^1-?\d{3}-?\d{3}-?\d{4}$|^0?\d{3}.?\d{3}.?\d{4}$',number)):  
        
        print("Valid Number")  
          
    else:  
        print("Invalid Number")
validate("2124567890")
validate("212-456-7890")
validate("(212)456-7890")
validate("(212)-456-7890")
validate("212.456.7890")
validate("212 456 7890")
validate("+12124567890")
validate("+12124567890")
validate("+1 212.456.7890")
validate("+212-456-7890")
validate("1-212-456-7890")
