from AltinoLite import *
Open()

while 1:#첫번째 (출발)
    #후방센서를 터치하면 출발
    if sensor.IR[6]>100:
        go(400,400)
        delay(500)
        break

while 1:#두번째 (출발~첫번째 터널)

    steering(0)
    go(400,400)
    
    #정지코드 좌우 센서 잡기
    if sensor.IR[4]>200:
        if sensor.IR[5]>200:
            steering(0)
            go(0,0)
            break
        
    #1,2,3번 센서 벽에 닿을시 후진
    #전방센서
    if sensor.IR[2]>45:
        go(0,0)
        #오른쪽 센서가 가까우면
        if sensor.IR[1]<sensor.IR[3]:
            steering(127)
            go(-500,-200)
            delay(800)
            go(0,0)
            steering(-127)
            go(300,400)
            delay(1000)
            steering(0)
        #왼쪽 센서가 가까우면
        else:
            steering(-127)
            go(-200,-500)
            delay(800)
            go(0,0)
            steering(127)
            go(400,300)
            delay(1000)
            steering(0)

    #1,3번 전방 센서가 벽을 마주했을시
    elif sensor.IR[1]>60:
        go(0,0)
        steering(-127)
        go(-200,-500)
        delay(800)
        go(0,0)
        steering(127)
        go(400,300)
        delay(1000)
        steering(0)
    elif sensor.IR[3]>60:
        go(0,0)
        steering(127)
        go(-500,-200)
        delay(800)
        go(0,0)
        steering(-127)
        go(300,400)
        delay(1000)
        steering(0)
        
    #후방센서
    elif sensor.IR[6]>100:
        steering(0)
        go(0,0)
    
    #4,5번 센서 벽에 닿을시
    elif sensor.IR[4]>70 and sensor.IR[4]<=100:
        steering(-63)
        go(300,300)
        delay(500)
    elif sensor.IR[5]>70 and sensor.IR[5]<=100:
        steering(63)
        go(300,300)
        delay(500)
        
    elif sensor.IR[4]>100:
        steering(-127)
        go(300,300)
        delay(500)
    elif sensor.IR[5]>100:
        steering(127)
        go(300,300)
        delay(500)

    #터널을 통과시----------------------------------------STOP출력,전조등,브레이크등
    if sensor.CDS<=100:
        led(1)
        led(2)
        go(0,0)
        DisplayLine(0xfb,0xfb,0xdb,0xdb,0xdb,0xdb,0xdf,0xdf)
        delay(1000)
        DisplayLine(0xc0,0xc0,0xc0,0xff,0xff,0xc0,0xc0,0xc0)
        delay(1000)
        DisplayLine(0x7e,0xff,0xc3,0xc3,0xc3,0xc3,0xff,0x7e)
        delay(1000)
        DisplayLine(0xff,0xff,0xd8,0xd8,0xd8,0xd8,0xf8,0xf8)
        delay(1000)
        DisplayLine(0,0,0,0,0,0,0,0)
        break#다음터널을 위한 반복문 정지
    #터널이 아닐시에 모든 전등 off
    elif sensor.CDS > 100:
        led(0)

    #아무런 일이 없으면 바퀴를 일자로 맞춘후 주행
    else:
        steering(0)

while 1:#세번째 (두번째 터널 ~ 피니쉬 라인)

    count = 0
    steering(0)
    go(400,400)

    delay(1)#터널 중복 정지를 막기 위한 딜레이 count = 500이 1초 
    count += 1

    #finish라인 정지 마지막 반복문에만 넣기
    if sensor.IR[1]>30 and sensor.IR[2]>30 and sensor.IR[3]>30 and sensor.IR[4]>5 and sensor.IR[5]>5:
        go(-400,-400)#급제동 코드
        delay(100)
        go(0,0)
        steering(0)
        for i in range (3):
            led(15)
            delay(1000)
            led(0)
            delay(1000)
        break
        

    #정지코드 좌우 센서 잡기
    if sensor.IR[4]>200:
        if sensor.IR[5]>200:
            steering(0)
            go(0,0)
            break
        
    #1,2,3번 센서 벽에 닿을시 후진
    #전방센서
    if sensor.IR[2]>45:
        go(0,0)
        #오른쪽 센서가 가까우면
        if sensor.IR[1]<sensor.IR[3]:
            steering(127)
            go(-500,-200)
            delay(800)
            go(0,0)
            steering(-127)
            go(300,400)
            delay(1000)
            steering(0)
        #왼쪽 센서가 가까우면
        else:
            steering(-127)
            go(-200,-500)
            delay(800)
            go(0,0)
            steering(127)
            go(400,300)
            delay(1000)
            steering(0)

    #1,3번 전방 센서가 벽을 마주했을시
    elif sensor.IR[1]>60:
        go(0,0)
        steering(-127)
        go(-200,-500)
        delay(800)
        go(0,0)
        steering(127)
        go(400,300)
        delay(1000)
        steering(0)
    elif sensor.IR[3]>60:
        go(0,0)
        steering(127)
        go(-500,-200)
        delay(800)
        go(0,0)
        steering(-127)
        go(300,400)
        delay(1000)
        steering(0)
        
    #후방센서
    elif sensor.IR[6]>100:
        steering(0)
        go(0,0)
    
    #4,5번 센서 벽에 닿을시
    elif sensor.IR[4]>70 and sensor.IR[4]<=100:
        steering(-63)
        go(300,300)
        delay(500)
    elif sensor.IR[5]>70 and sensor.IR[5]<=100:
        steering(63)
        go(300,300)
        delay(500)
    
    elif sensor.IR[4]>100:
        steering(-127)
        go(300,300)
        delay(500)
    elif sensor.IR[5]>100:
        steering(127)
        go(300,300)
        delay(500)

    #터널을 통과시----------------------------------------노래 출력
    if sensor.CDS<=100 and count > 3000:#첫번째 터널을 통과 6초후에 작동하는 코드
        led(1)
        sound(37)
        delay(400)
        sound(0)
        delay(100)
        led(0)
        led(4)
        sound(41)
        delay(500)
        sound(0)
        led(0)
        led(8)
        sound(41)
        delay(500)
        sound(0)
        led(0)
        #터널을 나갈때 까지 문자 안출력하기 위해 딜레이
        go(400,400)
        delay(1000)
        #break#다음터널을 위한 반복문 정지
    #터널이 아닐시에 모든 전등 off
    elif sensor.CDS > 100:
        led(0)

    #아무런 일이 없으면 바퀴를 일자로 맞춘후 주행
    else:
        steering(0)

        
close()

