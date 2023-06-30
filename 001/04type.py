# 第一种数据类型：字符串（str）
# 表示文本内容，用引号包裹，可以用 len() 函数求其长度
len("r u ok?")
len('高中生哪有不疯的，硬撑罢了！')
# hmmm... 是的，还是需要 print 一下才能真正输出
print(len("r u ok?"))
print(len('高中生哪有不疯的，硬撑罢了！'))
# 你可能注意到了，空格和标点也是占据一个长度的，但是特殊的，例如转义符，不会占据长度
# 例如下方这个例子，转义符 ”\“ 不占据长度，空格占据长度，”n“ 也占据一个长度，也就是说，一个完整的转义符只算一个长度
print(len("你 \n说 \n话 \n带 \n空 \n格"))

print("=========")

# 你也可以提取字符串某一位置的单个字符，在字符串后跟个方括号，里面放上一个数字，名曰 ”索引“，这是就可以提取该索引位置上的字符
# 索引也就是排排坐，从第一个字符数起，是 0、1、2、3、4、5、6...
print("这串字符串的长度为："+str(len("I do.")))  # 这里 str() 函数将数据类型为整数类型的数据转换为字符串以供输出
print("I do."[0])  # 索引为 0，输出 I
print("I do."[1])  # 索引为 1，输出空格
print("I do."[2])  # 索引为 2，输出 d
print("I do."[3])  # 索引为 3，输出 o
print("I do."[4])  # 索引为 4，输出句号

print("=========")

# 第二、三种数据类型：整数类型（int）与浮点数类型（float）
# 可以看看前面有关计算器的文件，不多说啦

#