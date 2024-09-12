ban = [0] * 8  # tạo danh sanh vỡi 8 số [0]

# in ra 8 cái danh sách "bàn"
for i in range(len(ban)):
    ban[i] = ["_"] * 8    


def banco(ban): # Hàm bàn cờ
    # tạo ra hàng cột
    #enumuerate() lấy 1 phần tử trong danh sách và gán cho nó một vị trí
    # i cho là vị trí của phần tử
    for i , cot in enumerate(ban):
        # làm hàng đém cột 
        print(8 - i, end =" ")
        # in ra một bàn 8 x 8 và mỗi dòng là 1 danh sách gán cho nó vị trí tướng ứng
        for j , ngang in enumerate(cot):
            # in ra hàng ngang với kết thúc là "space"
            print(ngang, end = " ")
        # khi tạo xong 1 hàng ngang sẽ xuống dòng xin 1 hàng mới
        print()
    # tạo hàng đếm ngang với bản chữ cái
    print(" "* 2 + "a" + " " + "b" + " " + "c" + " " + "d" + " " + "e" + " " + "f" + " " + "g" + " " + "h")

# biển đổi chữ cái hàng ngang thành số
def hangngang():

    "a" == 1
    "b" == 2
    "c" == 3
    "d" == 4
    "e" == 5
    "f" == 6
    "g" == 7
    "h" == 8

#vị trí quân trắng
def  quan_trang():
    #tốt trắng
    tT = [(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)]
    #xe trắng
    XT = [(7,0),(7,7)]
    #mã trắng
    MT = [(7,1),(7,6)]
    #tượng trắng
    TT = [(7,2),(7,5)]
    #Hậu trắng
    HT = [(7,3)]
    #Vua trắng
    VT = [(7,4)]


#vị trí quân đen
def  quan_den():
    #tốt đen
    tT = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
    #xe đen
    XT = [(0,0),(0,7)]
    #mã đen
    MT = [(0,1),(0,6)]
    #tượng đen
    TT = [(0,2),(0,5)]
    #Hậu đen
    HT = [(0,3)]
    #Vua đen
    VT = [(0,4)]

#đặt quan lên bàn cờ
def dat_quan(ban):
    pass


if __name__ == "__main__":
    banco(ban)