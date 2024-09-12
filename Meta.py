

# defind list 8 symple "_"
table_o = ["_"] * 8
# defind list 8 symple "abc"
table_name = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def DisplayTableChess(table):
    for i in range (len(table), 0, -1):
        print(i, end = " ")
        for j in table:
            print(j, end = " ")
        print()
    for z in table_name:
        print(z, end = " ")


if __name__ == "__main__":
    DisplayTableChess(table_o)