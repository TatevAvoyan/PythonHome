def my_print(*params, end="\n"):
    text = ''
    for i in params:
        text += str(i)
        text += ' '
    print(text, end=end)


my_print(324, 'Hello', 35, True, "HI", end=" ====== ")
my_print(324, 'Hello', 35, True, "HI", end="\t")
my_print(324)


print(324, 'Hello', 35, True, "HI", end=" ====== ")
print(324, 'Hello', 35, True, "HI", end="\t")
print(324)
