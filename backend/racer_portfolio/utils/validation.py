import re

def validate_email(email):
    email_form = re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    return email_form.match(email) != None

def validate_password(password):
    password_length = len(password)
    count = 0
    if re.compile("[a-zA-Z]").search(password):
        count += 1
    if re.compile("[0-9]").search(password):
        count += 1
    if re.compile("[\W]").search(password):
        count += 1

    if count == 2 and password_length >= 10:
        return True
    elif count == 3 and password_length >= 8:
        return True
    
    return False

def validate_name(name):
    return re.compile("[^a-zA-Zㄱ-ㅎㅏ-ㅣ가-힣]").search(name) == None and len(name) > 0 and name != None
