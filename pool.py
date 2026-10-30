
correct_username = "apsu"
correct_password = "apsana"
attempts = 0

while attempts <= 3:
 username =input("enter your name:")
 password =input("enter your password:")
 attempts = attempts + 1
 if correct_username == username and correct_password == password:
    print("you can enter")
    break
 else:
    print("you cannot enter")


