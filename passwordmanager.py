from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) 
        '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


masterpass = input("Input your MASTER PASSWORD: ")
key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Email / Username: ", user, " Password: ", str(fer.decrypt(passw.encode())))
            

def add():
    username = input("Account Username / Email: ")
    password = input("Account Password: ")

    with open('password.txt', 'a') as f:
        f.write(username + "|" + str(fer.encrypt(password.encode())) + "\n")
    

while True:
    mode = input("""ADD New Password or VIEW Existing ones? (view/add)
    Press 'q' if you want to quit
    """)

    if mode == 'q':
        break

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Enter the right MODE")
        continue


