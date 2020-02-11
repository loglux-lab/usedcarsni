# Keyring, getpass (to hide password from the screen)
import keyring
import getpass


def web_auth():
    print("Checking credentials")
#    global user_password, user_name
    user_name = keyring.get_password('UsedCarsNI', "username")
#    print(user_name)
    if not user_name:
        print("Type your username and password here:")
        user_name = input("Username: ")
        user_password = getpass.getpass("Password: ")
        print("You password doesn't match. Please, try again.")
        keyring.set_password('UsedCarsNI', "username", user_name)
        keyring.set_password('UsedCarsNI', "password", user_password)
    else:
        pass
    print("That's fine!")
    user_password = keyring.get_password('UsedCarsNI', "password")
    return user_name, user_password


if __name__ == "__main__":
    user_name, user_password = web_auth()
    print(user_name)
