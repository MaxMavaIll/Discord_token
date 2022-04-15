from manage_fun.add_fun import wrc


def output_screen():
    data = wrc.get_all()
    if data["data"] != []:
        j = 1
        print("\n%15s %32s %22s %20s" %("--Email--", "--password--", "--Name_url--", "--Name_addr--"), end="\n\n")
        for i in data["data"]:
            print(" {0}. {1:30s}{2:25s}{3:20s}{4:20s}".format(j, i[0], i[1], i[2], i[3]))
            j += 1
        print()
    else:
        print("\nEmail none...\n")

    if data["address"] != []:
        j = 1
        print("\n%40s" %"--Address--",end="\n\n")
        for i in data["address"]:
            print(" %d. %s : %s " %(j, i[0], i[1]))
            j += 1
    else:
        print("\nAddress none...\n")

    if data["url"] != []:
        j = 1
        print("\n%40s" %"--URLS--", end='\n\n')
        for i in data["url"]:
            print(" %d. %s : %s " %(j, i[0], i[1]))
            j += 1
    else:
        print("\nUrl none...\n")