# 生活中有很多需要判断的事情，python 中的条件语句格式如下：
# if [条件]:  # 其中条件需为布尔值
# 你也可以用比较运算符来输出布尔值：
print (3 == 3)  # True
print("114514" == "1919810")  # False
print(3.14 != 0.618)  # True
print(3 > 4)  # False
print(2 * (1 / 2) >= 1)  # True

print("==========")

# 因此整个条件语句的完整格式为
# if [条件]:
#     [执行语句]
#     [执行语句]
# else:
#     [执行语句]
#     [执行语句]

# 来试着做一个简单的 Minecraft 生怪判断器吧！
light_level = int(input("请输入光照等级："))  # 用户输入光照等级并转化为整型
if light_level > 7:  # 判断光照等级是否允许敌对生物生成
    if light_level > 15:  # 判断是否输入错误的光照等级
        print("错误：光照等级不得高于 15")  # 抛出错误
    else:
        print("此处不会生成敌对怪物")  # 输出结论
else:
    if light_level < 0:  # 判断是否输入错误的光照等级
        print("错误：光照等级不得低于 0")  # 抛出错误
    else:
        print("此处会生成敌对怪物")  # 输出结论

print("==========")

# 如果你想简洁化下面这串玩意：
guess = int(input("猜猜我心里想的数字吧："))

if guess == 86:
    print("耶！你猜对了！")
else:
    if guess > 86:  # 再次判断大小并给出提示
        print("我想的数字比这个小")
    else:
        print("我想的数字比这个大")

print("==========")

# 你可以使用 elif 来简化这个金字塔一样的玩意
guess = int(input("猜猜我心里想的数字吧："))
if guess == 86:
    print("耶！你猜对了！")
elif guess > 86:  # elif=else if
    print("我想的数字比这个小")
else:
    print("我想的数字比这个大")

print("==========")

# 接下来我们来做一个 BMI 判断的程序，先把之前做的 BMI 计算代码抄过来
height = float(input("您的身高是（单位：米）："))  # 用户输入身高
weight = float(input("您的体重是（单位：千克）："))  # 用户输入体重
bmi = float(weight / (height ** 2))    # 计算用户 bmi，由于身高和体重可能出现小数，因此转换为浮点型进行运算，否则可能会报错
if bmi <= 18.5:
    print("您的 BMI 值为："+str(bmi)+"，属于偏瘦范围")
elif 18.5 < bmi <= 25:
    print("您的 BMI 值为：" + str(bmi) + "，属于正常范围")
elif 25 < bmi <= 30:
    print("您的 BMI 值为：" + str(bmi) + "，属于偏胖范围")
else:
    print("您的 BMI 值为：" + str(bmi) + "，属于肥胖范围")