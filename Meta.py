

# defind list 8 symple "_"
table_o = ["__"] * 8
# defind list 8 symple "abc"
table_name = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# defind list "quân chốt"
list_quan_chot_T = ["CT"] * 8
list_quan_chot_D = ["CD"] * 8

# defind list "Quân cờ"
list_quan_T = ["xe", "ma", "tu", "vu", "ha", "tu", "ma", "xe"]
list_quan_D = ["xe", "ma", "tu", "vu", "ha", "tu", "ma", "xe"]

def DisplayTableChess(table):
    for i in range (len(table), 0, -1):
        print(i, end = " ")
        if i == 8:
            for j in list_quan_T:
                print(j, end = " ")
        elif i == 7:
            for j in list_quan_chot_T:
                print(j, end = " ")
        elif i == 2:
            for j in list_quan_chot_D:
                print(j, end = " ")
        elif i == 1:
            for j in list_quan_D:
                print(j, end = " ")
        else:
            for j in table:
                print(j, end = " ")
        print()
    for z in table_name:
        print(z, end = "  ")




if __name__ == "__main__":
    DisplayTableChess(table_o)