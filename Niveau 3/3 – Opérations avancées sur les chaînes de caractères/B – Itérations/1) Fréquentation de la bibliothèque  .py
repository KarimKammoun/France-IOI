s=0
while True:
    try:
        a=input().split(" ")
        for i in a:
            s=s+int(i)
    except:
        print(s)
        break