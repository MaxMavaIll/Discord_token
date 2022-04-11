#!/usr/bin/env python

from json import dumps,loads


class Write_Read_config:
    def get_all(self):
        with open("config.py", "r") as file:
            read = file.read()
            date = loads(read)
            return date

    def get_elem(self):
        pass

    def save(self, date):
        with open("config.py", "w") as file:
            x = dumps( date, indent=1 )
            file.write(x)

    def check_email(self, email_name):
        dt = self.get_all()
        for i in range(len(dt["date"])):
            if dt["date"][i][0] == email_name:
                return 1
        return 0

    def find_index(self, dt, arg, key) -> int:
        for i in range(len(dt[key])):
            if dt[key][i][0] == arg:
                return i
        return None

    
wrc = Write_Read_config()

def check_email_password( *get ):
    if len(get)%2 != 1 and len(get) != 1:
        return 1
    else:
        return 0

def chack_addr_testnet( *get ):
    pass

def add_INconf_tnet( *args ):
    date = wrc.get_all()
    pol_args = len(args)/2
    for i in range( int(pol_args) ):
        mass = []
        for j in range(2):
            mass.append(args[2*i+j])
        date["address"].append(mass)
    wrc.save(date)

def add_INconf( *args ):
    date = wrc.get_all()
    pol_args = len(args)/2
    for i in range( int(pol_args) ):
        mass = []
        for j in range(2):
            mass.append(args[2*i+j])
        
        date["date"].append(mass)
    wrc.save(date)

def delete_email(email_name):
    date = wrc.get_all()
    del date["date"][wrc.find_index(date, email_name, "date")]
    wrc.save(date)

def delete_addr_testnet(name):
    date = wrc.get_all()
    del date["address"][wrc.find_index(date, name, "address")]
    wrc.save(date)
    
def output_screen():
    date = wrc.get_all()
    if date["date"] != []:
        print("%15s %20s" %("--Email--", "--password--"))
        for i in date["date"]:
            print("%s    %s" %(i[0], i[1]))
    else:
        print("\nEmail none...\n")

    if date["address"] != []:
        print("%25s" %"--Address--")
        for i in date["address"]:
            print("%s : %s " %(i[0], i[1]))
    else:
        print("\nAddress none...")