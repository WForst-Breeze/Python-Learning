# 如果你需要一堆数据，而不想去一个个定义变量，那么可以使用列表：
optional_subject = ["物理", "化学"]  # 定义 3+3 高考选课
# 如果你想加东西，可以使用针对列表的方法，append（不是函数！）
optional_subject.append("地理")
# 列表与其他数据类型的不同点是，列表是可变的，举个例子：
text = "oh my minecraft client"
print(text.upper())  # 使字符串大写
print(text)  # 然而字符串本身没有变化
text = text.upper()  # 如果想变化，需要重新赋值
# 单列表可以直接使用 append 方法来改变原列表，而不需重新赋值（也不应重新赋值）
print(optional_subject)
optional_subject.append("生物")
print(optional_subject)

print("==========")

# 现在我们的列表里有四个科目了，但我们只能选择三门，如果想移除地理科目，可以使用 remove 方法
optional_subject.remove("地理")
print(optional_subject)

print("==========")

# Python 的列表允许同时存放不同数据类型的数据
data_type = ["string", False, None, 3.14]
data_type.append(3)
data_type.append(True)
print(data_type)

print("==========")

# 同样地，列表和字符串一样可以使用索引，可以使用 len() 求长度
print(len(optional_subject))  # 求列表中的元素数量
print(optional_subject[2])  # 输出列表中第三个元素
# 你也可以通过索引赋值来修改列表对应位置的元素
optional_subject[2] = "地理"
print(optional_subject)

print("==========")

# 还有一些针对列表的函数：
final_grade = [75, 95, 97, 90, 97, 70]
print(max(final_grade))  # 输出最大值
print(min(final_grade))  # 输出最小值
print(sorted(final_grade))  # 从小到大排序列表