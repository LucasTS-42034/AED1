n = int(4)
def fat(n):
    if n == 0:
        return 1
    else:
        return(n*fat(n-1))

print(fat(n))