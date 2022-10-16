def nhaplieu(a):
    b=''
    for i in a:
        if i!=' ':
            b=b+i

        #cắt chuỗi b thành list
    global mylist
    mylist = b.split(',')

        #xoá phần tử rỗng trong list
    for i in mylist:
        if i=='':
            mylist.remove(i)

    co=1
    for i in mylist:
        if kiemtra(i)==0:
            co=0
    return co
            


def kiemtra(x):
    if x.isdigit():
        return 1
    else:
        return 0


a=input('nhập dữ liệu vào ')
while a=='':
    a=input('nhập lại dữ liệu vào ')

while nhaplieu(a)==0:
    a=input('nhập lại dữ liệu vào ')

print(mylist)