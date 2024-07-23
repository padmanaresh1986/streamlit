import bcrypt
passwords = ["admin","user"]
hashed_passwords = [bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() for password in passwords]
print(hashed_passwords)

