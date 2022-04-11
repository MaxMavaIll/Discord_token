#!/usr/bin/env python


from manage_fun.add_fun import *

while 1:
    get_user = input(">>> ")   
    get = get_user.split(" ")
    if get[0] == "add":
        if get[1] in "addr":
            if check_email_password( *get[2:]):
                add_INconf(*get[2:])
                print("Email з паролем додані!")
            else:
                print("Провірте правельність ведення, не вистачає password або email")
        elif get[1] in "taddr":
            add_INconf_tnet(*get[2:])
            print("Адрес доданий")



    elif get[0] == "del" or get[0] == "delete":
        if get[1].find("@")+1:
            if wrc.check_email(get[1]):
                delete_email(get[1])
                print("Email з паролем видалені успішно!")
            else:
                print("Email не знайдено...")
        else:
            delete_addr_testnet(get[1])
            print("Address видалений успішно!")

    elif get[0] == "list":
        output_screen()
    elif get_user in "-h" or "-help":
        print(" add addr [email] [password]     -додавання адресу\n add taddr [name] [address]\
      -адрес з testneta\n list all                          -весь список\n delete [address]\
      -видалення imail i password")
    else:
        print(" add addr [email] [password]     -додавання адресу\n add taddr [address]\
            -адрес з testneta\n list     -весь список\n del [address]     -видалення imail i password або адреса_testnet")
