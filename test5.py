from AltinoLite import*
#자율주행 함수 AUTO
#AUTO(0)->왼쪽
#AUTO(1)->오른쪽
def Auto(direction=0,th=13,sp=350,bsp=-350):
    if sensor.IR[1]>th and sensor.IR[2]>th and sensor.IR[3]>th:
        if direction == 0:
            go(bsp,bsp)
            steering(127)
        else:
            go(bsp,bsp)
            steering(-127)

    elif sensor.IR[1]>100 and sensor.IR[2]>th:
        go(bsp,bsp)
        steering(-127)

    elif sensor.IR[1]>th and sensor.IR[2]>th:
        go(sp,sp)
        steering(127)

    elif sensor.IR[2]>th and sensor.IR[3]>100:
        go(bsp,bsp)
        steering(127)

    elif sensor.IR[2]>th and sensor.IR[3]>th:
        go(sp,sp)
        steering(-127)

    elif sensor.IR[1]>th:
        go(sp,sp)
        steering(64)

    elif sensor.IR[3]>th:
        go(sp,sp)
        steering(-64)

    else:
        go(sp,sp)
        steering(0)

def mission1(do=37,mi=41): 
    

    
    sound(do)
    delay(500)
    sound(0)
    sound(41)
    delay(500)
    sound(0)
    sound(37)
    delay(500)
    sound(0)
    sound(41)
    delay(500)
    sound(0)
    sound(37)
    delay(500)
    sound(0)
    sound(41)
    delay(500)
    sound(0)

def mission2(a=0):
    DisplayLine(0x38,0x44,0x42,0x21,0x21,0x42,0x44,0x38)
    delay(1000)
    Display(0)
    
def stop(sp=-350):
    go(-350,-350)
    steering(0)
    delay(150)
    go(0,0)
    steering(0)

  
    

Open()

while 1:
    if sensor.IR[4]>200:
        break

while 1:
    Auto(1)#출발
    if sensor.CDS<100:
        stop(1)
        mission1(1)
        break
    
sensor.CNT=0

while 1:
    Auto(1)
    if sensor.CDS<100 and sensor.CNT>20:
        stop(1)
        mission2(1)
        break
    

    
    
close()
    
