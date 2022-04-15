#!/usr/bin/env python

from json import dumps,loads


class Write_Read_config:
    """Class for work with congfig.py"""
    def get_all(self):
        with open("config.py", "r") as file:
            read = file.read()
            data = loads(read)
            return data

    def get_elem(self):
        pass

    def save(self, data):
        with open("config.py", "w") as file:
            x = dumps( data, indent=1 )
            file.write(x)

    def check_is_volue(self, name_volue, name_key):
        dt = self.get_all()
        for i in range(len(dt[name_key])):
            if dt[name_key][i][0] == name_volue:
                return 1
        return 0

    def find_index(self, dt, arg, key) -> int:
        for i in range(len(dt[key])):
            if dt[key][i][0] == arg:
                return i
        return None
  
wrc = Write_Read_config()



#additional function

def check_email_password( *get ):
    if len(get)%2 != 1 and len(get) != 1:
        return 1
    else:
        return 0

def chack_addr_testnet( *get ):
    pass

# def add_INconf_tnet( *args ):
#     data = wrc.get_all()
#     pol_args = len(args)/2
#     for i in range( int(pol_args) ):
#         mass = []
#         for j in range(2):
#             mass.append(args[2*i+j])
#         data["address"].append(mass)
#     wrc.save(data)

def add_INconf( name_key, *args ):
    data = wrc.get_all()
    if name_key == "data":
        number_elem = 4
        pol_args = int(len(args)/number_elem)
        for i in range( pol_args ):
            mass = []
            for j in range(number_elem):
                mass.append(args[number_elem*i+j])
            
            data[name_key].append(mass)
        wrc.save(data)
    else:
        number_elem = 2
        pol_args = len(args)/number_elem
        for i in range( int(pol_args) ):
            mass = []
            for j in range(number_elem):
                mass.append(args[number_elem*i+j])
            
            data[name_key].append(mass)
        wrc.save(data)
    