#password validation using regular expression.
import re
def validate_password(password):
    pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%&])[A-Za-z\d@$%&]{8,}$'
            # ^ starting , ?=.*-atleast                    match any chr from the set         chr 
            #8- min 8 char , $ - ending
    if re.search(pattern,password):
        return "Valid password"
    else:
        return("Invalid password")
password=input("Enter password")
print(validate_password(password))