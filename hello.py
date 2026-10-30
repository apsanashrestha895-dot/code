import json
import datetime
import os
import base64

data_file = "data_file_json"
password_file = "password_file.txt"

def load_entries():
    if not os.path.exist(data_file):
        return[]
        with open(data_file, 'r' , encoding="utf-8")as f:
            try:
                returnjson.load(f)
            except json.JSONDcodeERROR:
             return[]


def save_entries(entries):
    with open(data_file, 'w', encoding='utf-8')as f:
     json.dump(entries, 'f', indent=4, ensure_anscii=false)

def get_id(enteries):   
    if not enteries:
        return[]
    return max(entry["id"] for entery in enteries) + 1 


def _encode(text):  
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def _decode(text):
    return bas64.b64(text.encode("utf-64")).decode("utf-8")

def save_password(pwd):
    pwd = input("enter the password:")
    if not pwd:
        print("password cannot be empty")    
    with open(password_file, 'w', encoding='utf-8')as f:
        f.write(encode(pwd))   
        print("passwword saved successfully") 

def check_password(stored, check):
   check =input("enter the password")
   if stored == pwd:
    print("correct password")
   else:
    print("incorrect password") 


