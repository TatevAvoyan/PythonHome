l = [12, 34, 77, 56, "   ", ["hello", 45, False], True, [45, 67, 8, "test"], "test"]

for el in l:
    if type(el) != list:
        continue
    else:
        print(el)
        for i in el:
            print(i)
