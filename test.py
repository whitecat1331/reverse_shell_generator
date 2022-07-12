list_iter = iter(range(10))

for i in list_iter:
    if i == 3:
        next(list_iter,None)
    print(f"{i}")

