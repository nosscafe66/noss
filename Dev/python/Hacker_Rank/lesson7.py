if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        i = i + 1
        strnum = str(i) 
        if i <= n:
            #calc = i * "{}"
            arr.append(strnum)
            list_join = (''.join(arr))
    print(list_join)