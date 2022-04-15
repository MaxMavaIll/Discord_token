from .add_fun import wrc


def delete_volue(name_volue, name_key):
    data = wrc.get_all() 
    del data[name_key][wrc.find_index(data, name_volue, name_key)]
    wrc.save(data)

