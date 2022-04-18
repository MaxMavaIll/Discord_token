#!/usr/bin/env python3


from manage_fun.add_fun import *
from manage_fun.del_fun import *
from manage_fun.output import *
import argparse
import os, sys



def get_args_cli(mass):

    parser = argparse.ArgumentParser(add_help=True)
    
    subparsers = parser.add_subparsers(help='List of commands')

    list_parser = subparsers.add_parser("ls", help="Get all list")
    list_parser.add_argument("-a", action="store_true", default=True, help="all list")
    list_parser.add_argument("-e", action="store_true", help="all list emails and passwords")
    list_parser.add_argument("-k", action="store_true", help="all list addresses")
    list_parser.add_argument("-u", action="store_true", help="all list urls")


    # A create command
    delete_parser = subparsers.add_parser('del', help='-- delete <addres with password> or <addres nestnet>')
    delete_parser.add_argument('value', action='store', help='Enter [ email || url || name ]')
    
    # A list command
    add_parser = subparsers.add_parser('add', help='-- add <address and password> or <addres nestnet>')
    add_parser.add_argument('-ml', action='store_true', help='Enter <email> <password> <url> <name_address>')
    add_parser.add_argument('-addr', action='store_true', help='Enter <name> <address>')
    add_parser.add_argument('-url', action='store_true', help='Enter <address>')
    add_parser.add_argument('email', action="store", default="illya")
    add_parser.add_argument('password', action="store", default="illya")
    add_parser.add_argument('url', action="store", default="illya")
    add_parser.add_argument('name', action="store", default="illya")

    print(parser.parse_args(mass))
    


def start_manager():
    get = sys.argv[1:]

    try:
        if get[0] == "add":
            if get[1] in "-ml":
                if check_email_password( *get[2:]):
                    add_INconf("data", *get[2:])
                    print("Email з паролем додані!")
                else:
                    print("Провірте правельність ведення, не вистачає password або email")
            
            elif get[1] in "-addr":
                add_INconf("address", *get[2:])
                print("Адрес доданий")
        
            elif get[1] in "-url":
                add_INconf("url", *get[2:])
                print("url-addr доданий")


        elif get[0] == "del":
            if get[1].find("@")+1:
                if wrc.check_is_volue(get[1], "data"):
                    delete_volue(get[1], "data")
                    print("Email з паролем видалені успішно!")
                else:
                    print("Email не знайдено...")
            elif get[1] == "-u":
                if wrc.check_is_volue(get[2], "url"):
                    delete_volue(get[2], "url")
                    print("Url видалені успішно!")
                else:
                    print("Name_url не знайдено...")
                
            elif get[1] == "-a":
                if wrc.check_is_volue(get[2], "address"):
                    delete_volue(get[2], "address")
                    print("Address видалений успішно!")
                else:
                    print("Name_addr не знайдено...")
                
            else:
                pass

        elif get[0] == "list":
            output_screen()

        elif get[0] == '-h' or get[0] == '--help':
            get_args_cli(["-h"])

        elif get[0] == "start":
            os.system(f"python3 time_start.py {get[1]}")
    except:
        print("Error! Choose with that.")
        get_args_cli(["-h"])
        
if __name__ == "__main__":
    start_manager()