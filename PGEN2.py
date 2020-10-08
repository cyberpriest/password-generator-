import random
def main():
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
    redo ='y'
    print (""*20,"<PasswordGenerator>".upper().center(40,'*'))
    print ("---- created by [joshua.A.timi] jatnet™ ----".center(30,'*'))
    print ()
    while redo =='y' or redo == 'yes' or redo =='Y':
        E_name = get_user_name()
        print ()
        generate_pwd = get_gen_pwd(chars,E_name)

        redo = input("\n do wana generate again type (Yes) type No to quit ")

def get_user_name():
    my_name =  input(">> input your name  ")
    return my_name
def get_gen_pwd(chars,name):
    c = random.choices(chars,k=16)
    eval = "".join(c)
    print(f"GENERATING PASSWWORD FOR {name} ")
    print()
    print(f" PASSWORD GENERATED : {eval} ")
        
    
main()

