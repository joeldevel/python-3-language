# copy gives you a list not bound to the original so it's safe to modify the copy
a_list = ['poti', 'floncho', 'urga']
print("a_list = ", a_list)
another_list = a_list.copy();
print("another_list = ", another_list)
print("another_list is a copy of a_list")
print("clearing a_list")
a_list.clear()
print("a_list = ",a_list)
print("another_list = ", another_list)
