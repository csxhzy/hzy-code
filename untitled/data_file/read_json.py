import json
with open("C:\\Users\\Administrator\\PycharmProjects\\untitled\\data_file\\user_info.json","r")as f:
    data=f.read()
user_list=json.loads(data)
print(user_list)