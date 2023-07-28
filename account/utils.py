import hashlib
import re

def hash_password(password:str):
    sha256  = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password


def check_phone(phone:str):
    pattern = '^[+]998[0-9]{9}$'
    checked_phone = re.match(pattern, phone)
    return bool(checked_phone)

def check_date(data:str):
    pattern = '^[0-9]{4}\-{1}[0-9]{2}\-{1}[0-9]{2}$'
    checked_date = re.match(pattern,data)
    return bool(checked_date)
