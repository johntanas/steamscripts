#generate one time totp code for steam guard
import json
from steampy.guard import generate_confirmation_key, generate_one_time_code
x=input("name of account? ")
path="./steamguard/"+x+".txt"
f= open(path)
a =json.load(f)
one_time_authentication_code = generate_one_time_code(a["shared_secret"])
print(one_time_authentication_code)
