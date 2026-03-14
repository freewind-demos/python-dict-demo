# Python 字典操作

# 创建字典
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

# 访问值
print(f"名字: {person['name']}")
print(f"年龄: {person.get('age')}")

# 添加/修改
person["email"] = "zhangsan@example.com"
person["age"] = 26

# 删除
del person["city"]
email = person.pop("email")

# 遍历
for key, value in person.items():
    print(f"{key}: {value}")

# 字典推导式
squares = {x: x**2 for x in range(5)}
print(f"平方字典: {squares}")

# 合并字典
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}
print(f"合并: {merged}")
