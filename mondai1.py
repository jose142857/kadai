# ３条件付きで入力
# ミスしたらまたは何も入力されてない場合再入力させる




# a =input('文字列を入力\n')
# if(a ==''):
#     a =input('再入力\n')

# for i in range(len(a)):
#    if (a[i].isnumeric()==False):
#        if (a[i]!=','):
#            if(a[i]!=' '):
#                a =input('再入力\n') 

             
# mylist = a.split(',') 
# for x in mylist:
#     print(x)              
a=input('nhập dữ liệu vào ')
while a=='':
    a=input('nhập lại dữ liệu vào ')
co=1
while co==1:
    for i in a:
        if i!=',' and i!=' ' and not(i.isdigit()):
            co=0
            break
    if co==1:
        break
    elif co==0:
        a=input('nhập lại dữ liệu vào ')
  
    
        # print (len(a))
        # 昇順で並べる
        # カンマで区切る