from AltinoLite import *
Open()

count = 0

while 1:
    go(300,300)
    if count >500:
        go(0,0)
        break

    delay(1)
    count += 1

close()
