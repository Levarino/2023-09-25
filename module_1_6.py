my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Dict:", my_dict)
print("Existing value:", my_dict["Vasya"])
print(my_dict.get("Vassya", "Not existing value: None"))
my_dict["Pasha"] = 1980
my_dict["Dasha"] = 2012
a = my_dict.pop("Egor")
print("Deleted value:", a)
print("Modified dictionary:", my_dict)
my_set = {1, 42.314, 1, 42.314,1, "Яблоко", 42.314}
print("Set:", my_set)
print(my_set.add("Груша"))
print(my_set.add(3.14))
print(my_set.discard("Яблоко"))
print("Modified set:", my_set)