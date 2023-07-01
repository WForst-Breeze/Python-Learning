# 如何解决 if 套娃问题？快快端上逻辑运算罢！
# and：列出的所有条件需要同时满足，or：列出的所有条件只需一个满足，not：返回相反的结果
# 运算顺序为： not->and->or，你可以使用括号来改变运算顺序：
x = int(input("x="))
if not(x > 5 and (x < 10 or x == 12)):  # 即 x ≠ 12 且 x ≤ 5，或 x > 10 且 x ≤ 5
    print("1")
else:
    print("0")
if not x > 5 and x < 10 or x == 12:  # 等价于：if ((not x > 5) and x < 10) or x == 12，即 x ≤ 5 或 x = 12
    print("1")
else:
    print("0")