name = input ("请输入您的姓名： ")
print ("你好，" + name + '!')

innumber = input("请输入1到100之间的数字：")
number = int(innumber)
if 1 <= number <= 100 :
    print("答对啦")
else:
    print("回答错误")
