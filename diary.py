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
 #   print("goodbye")  
  #!/usr/bin/env python3
"""
Personal Diary Application
---------------------------
A simple command-line diary app to write, view, search, edit, and delete
journal entries. Entries are stored locally in a JSON file, one per user.

Features:
- Add new diary entries (with automatic date/time stamping)
- View all entries or a specific entry by ID/date
- Search entries by keyword
- Edit existing entries
- Delete entries
- Optional simple password protection (basic obfuscation, not strong encryption)

Run:
    python personal_diary.py
"""

import json
import os
import base64
from datetime import datetime

DATA_FILE = "diary_entries.json"
PASSWORD_FILE = "diary_password.txt"


# ---------------------------------------------------------------------------
# Storage helpers
# ---------------------------------------------------------------------------

def load_entries():
    """Load diary entries from the JSON data file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_entries(entries):
    """Save diary entries to the JSON data file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=4, ensure_ascii=False)


def get_next_id(entries):
    """Determine the next available entry ID."""
    if not entries:
        return 1
    return max(entry["id"] for entry in entries) + 1


# ---------------------------------------------------------------------------
# Simple password protection (obfuscation only — not real security)
# ---------------------------------------------------------------------------

def _encode(text):
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def _decode(text):
    return base64.b64decode(text.encode("utf-8")).decode("utf-8")


def set_password():
    pwd = input("Set a new diary password: ").strip()
    if not pwd:
        print("Password cannot be empty. Skipping password protection.")
        return
    with open(PASSWORD_FILE, "w", encoding="utf-8") as f:
        f.write(_encode(pwd))
    print("Password set successfully.\n")


def check_password():
    """Prompt for the password if one has been set. Returns True if OK."""
    if not os.path.exists(PASSWORD_FILE):
        return True
    with open(PASSWORD_FILE, "r", encoding="utf-8") as f:
        stored = _decode(f.read().strip())
    for attempt in range(3):
        pwd = input("Enter diary password: ").strip()
        if pwd == stored:
            return True
        print(f"Incorrect password. {2 - attempt} attempt(s) left.")
    print("Too many failed attempts. Exiting.")
    return False


# ---------------------------------------------------------------------------
# Core diary operations
# ---------------------------------------------------------------------------

def add_entry():
    print("\n--- New Diary Entry ---")
    title = input("Title: ").strip()
    print("Write your entry (type 'END' on a new line when finished):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    content = "\n".join(lines)

    entries = load_entries()
    entry = {
        "id": get_next_id(entries),
        "title": title if title else "(Untitled)",
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": None,
    }
    entries.append(entry)
    save_entries(entries)
    print(f"\nEntry #{entry['id']} saved successfully.\n")


def view_entries():
    entries = load_entries()
    if not entries:
        print("\nNo diary entries found.\n")
        return

    print("\n--- All Diary Entries ---")
    for entry in sorted(entries, key=lambda e: e["created_at"]):
        print(f"[{entry['id']}] {entry['title']}  ({entry['created_at']})")
    print()

    choice = input("Enter an entry ID to view in full (or press Enter to skip): ").strip()
    if choice.isdigit():
        show_entry(int(choice), entries)


def show_entry(entry_id, entries=None):
    entries = entries if entries is not None else load_entries()
    entry = next((e for e in entries if e["id"] == entry_id), None)
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
    keyword = input("\nEnter keyword to search for: ").strip().lower()
    entries = load_entries()
    results = [
        e for e in entries
        if keyword in e["title"].lower() or keyword in e["content"].lower()
    ]
    if not results:
        print("No matching entries found.\n")
        return
    print(f"\nFound {len(results)} matching entr{'y' if len(results) == 1 else 'ies'}:")
    for entry in results:
        print(f"[{entry['id']}] {entry['title']}  ({entry['created_at']})")
    print()


def edit_entry():
    entries = load_entries()
    if not entries:
        print("\nNo entries to edit.\n")
        return
    entry_id = input("Enter the ID of the entry to edit: ").strip()
    if not entry_id.isdigit():
        print("Invalid ID.\n")
        return
    entry_id = int(entry_id)
    entry = next((e for e in entries if e["id"] == entry_id), None)
    if not entry:
        print(f"No entry found with ID {entry_id}.\n")
        return

    show_entry(entry_id, entries)
    print("Leave blank to keep the current value.")
    new_title = input(f"New title [{entry['title']}]: ").strip()
    print("New content (type 'END' on a new line when finished, or just 'END' to keep current):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    new_content = "\n".join(lines)

    if new_title:
        entry["title"] = new_title
    if new_content:
        entry["content"] = new_content
    entry["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_entries(entries)
    print(f"\nEntry #{entry_id} updated successfully.\n")


def delete_entry():
    entries = load_entries()
    if not entries:
        print("\nNo entries to delete.\n")
        return
    entry_id = input("Enter the ID of the entry to delete: ").strip()
    if not entry_id.isdigit():
        print("Invalid ID.\n")
        return
    entry_id = int(entry_id)
    entry = next((e for e in entries if e["id"] == entry_id), None)
    if not entry:
        print(f"No entry found with ID {entry_id}.\n")
        return

    confirm = input(f"Are you sure you want to delete '{entry['title']}'? (y/n): ").strip().lower()
    if confirm == "y":
        entries = [e for e in entries if e["id"] != entry_id]
        save_entries(entries)
        print("Entry deleted.\n")
    else:
        print("Deletion cancelled.\n")


# ---------------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------------

def print_menu():
    print("=" * 40)
    print("        PERSONAL DIARY")
    print("=" * 40)
    print("1. Add new entry")
    print("2. View all entries")
    print("3. Search entries")
    print("4. Edit an entry")
    print("5. Delete an entry")
    print("6. Set/change password")
    print("7. Exit")
    print("=" * 40)


def main():
    if not check_password():
        return

    while True:
        print_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            edit_entry()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            set_password()
        elif choice == "7":
            print("\nGoodbye! Keep writing. 📝")
            break
        else:
            print("Invalid option. Please choose 1-7.\n")


if __name__ == "__main__":
    main()  


    
