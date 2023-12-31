# 通过赋值操作，可以给一个变量赋予一个值
# 注意变量名不得出现空格、以数字开头、用引号包裹
variable = "《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作“提瓦特”的幻想世界，在这里，被神选中的人将被授予“神之眼”，导引元素之力。你将扮演一位名为“旅行者”的神秘角色，在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘“原神”的真相。"
print("你说得对，但"+ variable)
print("你知道吗？"+ variable + "！")
print("=======")
# 单纯的计算机不知道你在干什么，它只会照着你的指令做，所以你可以为一个变量重新赋值
variable = "原神，米自研，冒险游，提瓦特，神选中，授神眼，引元素。扮角色，邂同伴，击强敌，找亲人，掘真相。"
# 此时再次执行 print，输出内容就会随之改变
print("你说对，但"+ variable)
print("=======")
# 同时，你可以用一个变量来给另一个变量赋值
genshin = variable
variable = "《喵喵》喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵。喵喵喵喵喵喵喵喵喵喵「喵喵喵」喵喵喵喵喵，喵喵喵，喵喵喵喵喵喵喵喵喵喵「喵喵喵」，喵喵喵喵喵喵。喵喵喵喵喵喵喵喵「喵喵喵」喵喵喵喵，喵喵喵喵喵喵喵喵喵喵喵喵喵、喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵喵，喵喵喵喵喵喵喵——喵喵，喵喵喵喵「喵喵」喵喵喵。"
meow = variable
print("你说得对，但"+ genshin)
print("喵喵喵喵，喵" + meow)
print("=======")

# 同时给变量命名也有一些不成文的规则：
# 1. 不要用拼音：
# 首先拼音命名是这样的。例如命名 ”用户名“ 这一变量，又臭又长，需要完整读一遍才明白
yong_hu_ming = "蒙古海军司令"
# 而英文命名则一般情况下简短、易于理解
username = "蒙古海军司令"
# 同时，拼音不带声调符号容易产生误解，例如命名 ”高几“ 这一变量来记录高中学生年级信息，就会出现一些尴尬的情况
gaoji = "2"
# 英文则大多没有这个苦恼
# 好吧…… 看来 grade 也是个多义词，不过相较 “高几” “镐击” “高级” “**” 这些歧义而言好多了……吧？
grade = "2"
# 2. 避免使用中文变量名：
# 尽管现在 Python 支持了中文变量名，但语言通常会因为编码兼容问题而产生乱码等问题锟斤拷烫烫烫烫烫
# 其次，你切输入法真的不难受吗www
# 3. 下划线命名法：字母全部小写，不同单词以下划线做分隔
# 举几个例子吧——
# 用户年龄
user_age = "24"
# 初次输入
initial_input = "1145141919810"
# 你也可以使用驼峰命名法
UserAge = "24"
InitialInput = "1145141919810"

# 注意：
# i 变量名是大小写敏感的，也就是说 user_age≠User_age
# ii 变量名不要占用 Python 关键字，如 print，这会直接废掉它原本的能力。Python 关键字列表如下：
# false      class      from      or
# none       continue   global    pass
# true       def        if        raise
# and        del        import    return
# as         elif       in        try
# assert     else       is        while
# async      except     lambda    with
# await      finally    nonlocal  yield
# break      for        not
