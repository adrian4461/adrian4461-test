#记录喜欢的数字
import json

userNumber = input("你喜欢什么数字？")
filename = r'data/userLike.json'
with open(filename,'w') as f_obj:
    json.dump(userNumber,f_obj)
    print("我会记住你喜欢的数字：" + userNumber + "!")
