import random
import string 

def main():
    redo = 'y'

    print("<PasswordGenerator>".upper().center(50, '*'))
    print("---- created by [joshua.A.timi] jatnet™ ----".center(50, '*') + "")
    
    while redo.lower() in ["y", "yes"]:
        try:
            pwd_len = int(input("Please enter a length for your password (recommended +13 characters): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        generated_pwd = get_gen_pwd(pwd_len)
        print(f"\nPASSWORD GENERATED: {generated_pwd}")

        redo = input("\nDo you want to generate another password (y/n)? ")

def get_gen_pwd(pwd_len):
    """
    Generates a random password of a given length combining alphanumeric and special characters.
    """
    alphanumeric = string.ascii_letters + string.digits
    special_characters = "`~!@#$%^&*()-_=+[]{\\}\\|;:'\",<.>/?"
    char_list = alphanumeric + special_characters

    return "".join(random.choices(char_list, k=pwd_len))

if __name__ == "__main__":
    main()