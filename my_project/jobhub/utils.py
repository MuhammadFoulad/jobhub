import hashlib
import random
import string

from jobhub.models import *


def generate_random_string(k):
    random_string=''.join(random.choices(string.ascii_letters,k=k))
    return random_string

def encript_password(password):
    password=hashlib.md5(password.encode('utf-8')).hexdigest()
    return password
def save_user(name,password,email,phone,login_id):
    user=Users()
    user.name=name
    user.password=password
    user.email=email
    user.phone=phone
    user.type="user"
    user.login_id=login_id
    user.save()
    
def save_login(email,password,salt,phone):
    login=Login()
    login.email=email
    login.password=password
    login.salt=salt
    login.type="user"
    login.phone=phone
    login.save()
    return login.id
