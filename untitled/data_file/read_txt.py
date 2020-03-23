#读取文件
with(open("C:\\Users\\Administrator\\PycharmProjects\\untitled\\data_file\\user_info.txt","r")) as user_file:
    data=user_file.readlines()

#格式化处理
users= []
for line in data:
    user =line[:-1].split(":")
    users.append(user)
#打印user二维数组
print(users)