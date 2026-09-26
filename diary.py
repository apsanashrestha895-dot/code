#print("-------------PERSONAL DIARY------------")
#print("1.write san entry")
#print("2.view entries")
#print("3.exit")
#choose = input("choose between 1,2,3")
#if choose == "1":
 #   entry = input("write an entry")
  #  print(entry)
#if choose == "2":
 #   print("welcome to the review")
#if choose == "3":
 #  print("goodbye")  

import json
import os
import base64
from datetime import datetime

data_file = "diary_entries_json"
password_file ="diarry_password.txt"

def load_entries():
  if not os.path.exists(data_file):
    return[]
  with open(data_file, "r", encoding ="utf-8")as f: 
    try: 
      returnjson.load(f)
    except json.JSONDecodeError:
     return[]

def save_entries(entries):
    with open(data_file, "w", encoding ="utf-8")as f:  
      json.dump(entries, f , indent=4, ensure_ascii=false)
def get_next_id(entries):
  if not entries:
    return[]
  return max(entry["id"] for entry in entries) + 1

def _encode(text):
  return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def _decode(text):
  return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def save_password():
     pwd =input("set a new password:")
     if not pwd:
      print("password cannot be empty")
      return
      with open(password_file , "w", encoding="utf-8")as f:
        f.write(encode(pwd))
        print("password saved successfully")

def check_password():
  if  not os.path.exits(password_file): 
    return True
  with open(password_file ,"r", encoding="utf-8")as f:
    stored = _decode(f.read())
  for attempts in range(3):
    pwd = input("enter your diary password")
    if stored == pwd:
     return True  
    prrint("incorrect password.{2 - attempt} attempt(s) left.")
    print("too many failed attempts")
    return False

def add_entry():
  print("\n--------- new diary entry------")
  title = input("title:").strip()
  print("write your entry(type 'end' on a new line when finished):")
  lines =[]
  while True: 
    line =input()
    if line.strip() == 'end':
      break
    lines.append(line)
    content =  "\n".join(lines)

  entries = load_entries()
  entry = {
    "id": get_next_id(entries),
    "title": title if title else "(untitled)",
    "content": content,
    "created_at": datetime.now().strftime("%y-%m-%d %H:%M:%S"),
    "udated_at": none,
  }
  entries.append(entry)
  save_entries(entries)
  print(f"\n entry #{entry['id']} saved successfully.\n")

def view_entry():
  entries =load_entries()
  if not entries:
    print("\n no entries found")
    return
    print("\n------all diaries entries--------")
    for entry in sorted(entries,key=lambda e: e['created_at']):
      print(f"[{entry['id']}] {entry['title']} ({entry['created_At']})")
      print()

    choice = input("enter any entry id to view in full(or press enter to skip):").strip()
    if choice.isdigit():
     show_entry(int(choice),entries)

def show_enteries(entry_id, entries = None):
  entries = entries if entries is not None else load_entries()
  entry = next((e for e in entries if e["id"] == entry_id),None)
  if not entry:
        print(f"\nNo entry found with ID {entry_id}.\n")
        return
  print("\n" + "=" * 50)
  print(f"Title: {entry['title']}")
  print(f"Created: {entry['created_at']}")
  if entry.get("updated_at"):
       print(f"Last updated: {entry['updated_at']}")
       print("-" * 50)
       print(entry["content"])
       print("=" * 50 + "\n")


def search_entries():
  keyword = input("\n enter keyword to search for:").strip().lower()
  entries = load_entries()
  results = [ e for e in entries] 



