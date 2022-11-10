from AltinoLite import*
#자율주행 함수 AUTO
#AUTO(0)->왼쪽
#AUTO(1)->오른쪽
def Auto(direction=0,th=13,sp=350,bsp=-350):
   
    go(400,400)
    steering(0)
    #1,2,3번 센서 벽에 닿을시 후진
    #전방센서

    if sensor.IR[2]>20:
        go(0,0)
        #오른쪽 센서가 가까우면
        go(-400,-400)
        delay(100)
        if sensor.IR[1]<sensor.IR[3] + 20:
            led(2)
            steering(127)
            go(-500,-100)
            delay(600)
            go(0,0)
            led(0)
            led(4)
            steering(-127)
            go(0,600)
            delay(400)
            steering(0)
            led(0)
        #왼쪽 센서가 가까우면
        else:
            led(2)
            steering(-127)
            go(-100,-500)
            delay(600)
            led(0)
            led(8)
            go(0,0)
            steering(127)
            go(600,0)
            delay(400)
            steering(0)
            led(0)

    #1,3번 전방 센서가 벽을 마주했을시

    elif sensor.IR[1]>th and sensor.IR[1]<70:
        go(sp,sp)
        steering(64)

    elif sensor.IR[3]>th and sensor.IR[3]<70:
        go(sp,sp)
        steering(-64)
        
    if sensor.IR[1]>70:
        led(2)
        go(-400,-400)
        delay(100)
        go(0,0)
        steering(-127)
        go(-100,-500)
        delay(600)
        go(0,0)
        led(0)
        led(8)
        steering(127)
        go(600,0)
        delay(400)
        steering(0)
        led(0)
        
            
    elif sensor.IR[3]>70:
        led(2)
        go(-400,-400)
        delay(100)
        go(0,0)
        steering(127)
        go(-500,-100)
        delay(600)
        go(0,0)
        led(0)
        led(4)
        steering(-127)
        go(0,600)
        delay(400)
        steering(0)
        led(0)
        
    

    

def mission1(do=37,mi=41): 
    led(1)
    sound(37)
    delay(500)
    led(0)
    led(8)
    sound(41)
    delay(500)
    led(0)
    led(4)
    sound(41)
    delay(500)
    led(0)
    sound(0)
    



def mission2(a=0):
    DisplayLine(0x8f,0xce,0xec,0xf8,0x1f,0x37,0x73,0xf1)
    delay(1000)
    Display(0)

    DisplayLine(0x18,0x3c,0x7e,0xff,0xff,0x7e,0x3c,0x18)
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
