import _thread
# from secrets import randbelow   # 导入线程模块
import time
# from turtle import speed      # 导入时间模块
import machine
from random import getrandbits, random
from time import sleep_ms

import motor

import ILI9341
import ILI9341_char
import ILI9341_touch

# Pin definition
LCD_RD = 2
LCD_WR = 4
LCD_RS = 32   # RS & CS pins must be ADC and OUTPUT
LCD_CS = 33   # for touch capability -> For ESP32 only pins 32 & 33 !
LCD_RST = 23
LCD_D0 = 12
LCD_D1 = 13
LCD_D2 = 26
LCD_D3 = 25
LCD_D4 = 17
LCD_D5 = 16
LCD_D6 = 27
LCD_D7 = 14

class ILI9341_control_PWM:
    def __init__(self):
        self.pwm1=machine.PWM(machine.Pin(7))#三个电机
        self.pwm2=machine.PWM(machine.Pin(8))
        self.pwm3=machine.PWM(machine.Pin(9))
        self.adc = machine.ADC(machine.Pin(4))#ADC用于检测温度
        self.adc.atten(machine.ADC.ATTN_11DB)
        self.adc.width(machine.ADC.WIDTH_9BIT)

        self.tft=ILI9341.screen(LCD_RD,LCD_WR,LCD_RS,LCD_CS,LCD_RST,LCD_D0,LCD_D1,LCD_D2,LCD_D3,LCD_D4,LCD_D5,LCD_D6,LCD_D7)
        self.tft.begin()
        for x in [0,1,2,3,4,5]:
            self.tft.fillRect( x%2*50 ,x//2*50, 40 , 40 ,getrandbits(16))
        self.ts = ILI9341_touch.touchscreen(XP, YP, XM, YM)
        self.ts.Pin_reset()
    
    def listen(self):
        while 1:
            time.sleep(100)
            x,y=self.ts.getPoint()
            pwmnum=y//50*2+x//50

class mymotor:
    def __init__(self,speed=0):
        self.pwm1=machine.PWM(machine.Pin(18))
        self.pwm2=machine.PWM(machine.Pin(19))
        self.m = motor.HalfStepMotor.frompins(14,12,13,27)
        self.speed=speed
        _thread.start_new_thread( motorrun , (speed, ) ) 

    def run(self,speed):
        self.speed=speed
        self.pwm1.duty(speed*1024//1)
    
    def motorrun(self,speed=0):
        print("motor start:",speed)
        while 1:
            time.sleep(0.1)
            self.m.step(self.speed*1000)
        _thread.exit()



# 定义线程函数,打印线程编号和运行时间
def print_time( threadName, delay):  
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s sec" % ( threadName, time.localtime()[5] ))

    print("%s:End" %threadName)
    # 结束线程
    _thread.exit()

# 启动线程1
# _thread.start_new_thread( print_time, ("Thread-1", 2, ) )  
# 启动线程2
tft=ILI9341.screen(LCD_RD,LCD_WR,LCD_RS,LCD_CS,LCD_RST,LCD_D0,LCD_D1,LCD_D2,LCD_D3,LCD_D4,LCD_D5,LCD_D6,LCD_D7)
BLACK       =   0x0000
BLUE        =   0x001F
RED         =   0xF800
GREEN       =   0x07E0
CYAN        =   0x07FF
MAGENTA     =   0xF81F
YELLOW      =   0xFFE0
WHITE       =   0xFFFF
GRAY        =   0x8410

global speed
speed = 100

def setspeed(s):
    global speed
    speed = s


def setnum(setspeed,speed,tempreture,step=10):
    tft.SetFont(3)
    tft.setTextColor(BLACK)
    tft.fillRect(200,40,120,20,WHITE)
    tft.setTextCursor(200,60)
    tft.printh(str(setspeed))
    tft.fillRect(200,60,120,20,WHITE)
    tft.setTextCursor(200,80)
    tft.printh(str(speed))
    tft.fillRect(200,80,120,20,WHITE)
    tft.setTextCursor(200,100)
    tft.printh(str(step))
    tft.fillRect(200,100,120,20,WHITE)
    tft.setTextCursor(200,120)
    tft.printh(str(tempreture))
tft.begin()
tft.setrotation(0)
tft.fillscreen(WHITE)
tft.setTextCursor(0,20)
tft.setTextColor(BLUE)
tft.SetFont(1)
tft.printh("motor system\n")
tft.printh("DLNU2017131204 BAIXIN\n")
tft.setTextColor(BLACK)
tft.SetFont(3)
tft.setTextCursor(0,60)
tft.setTextColor(BLACK)
tft.printh("SET SPEED:"+'\n')
tft.setTextCursor(0,80)
tft.printh("motor speed:"+'\n')
tft.setTextCursor(0,100)
tft.printh("stepper speed:"+'\n')
tft.setTextCursor(0,120)
tft.printh("tempreture:"+'\n')
tft.fillRect(0,160,160,80,RED)
tft.fillRect(5,165,150,70,WHITE)
tft.setTextCursor(10,200)
tft.printh("motor up")
tft.fillRect(160,160,160,80,RED)
tft.fillRect(165,165,150,70,WHITE)
tft.setTextCursor(170,200)
tft.printh("stepper up")
tft.fillRect(0,240,160,80,GREEN)
tft.fillRect(5,245,150,70,WHITE)
tft.setTextCursor(10,280)
tft.printh("motor \n down")
tft.fillRect(160,240,160,80,GREEN)
tft.fillRect(165,245,150,70,WHITE)
tft.setTextCursor(170,280)
tft.printh("stepper \n            down")


import RPi.GPIO as GPIO


class KY040:
    CLOCKWISE = 0
    ANTICLOCKWISE = 1
    def __init__(self, clockPin, dataPin, switchPin=None, rotaryCallback=None, switchCallback=None, rotaryBouncetime=250, switchBouncetime=300):
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback
        self.rotaryBouncetime = rotaryBouncetime
        self.switchBouncetime = switchBouncetime
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)
        if None != self.switchPin:
            GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, callback=self._clockCallback, bouncetime=self.rotaryBouncetime)
        if None != self.switchPin:
            GPIO.add_event_detect(self.switchPin, GPIO.FALLING, callback=self._switchCallback, bouncetime=self.switchBouncetime)
    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        if None != self.switchPin:
            GPIO.remove_event_detect(self.switchPin)
    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)
    def _switchCallback(self, pin):
        if None == self.switchPin:
            return
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()



class PID:
    """
    Discrete PID control
    """

    def __init__(self,input_fun,output_fun, P=1., I=0.2, D=0.05):

        self.Kp=P
        self.Ki=I
        self.Kd=D

        self.I_value = 0
        self.P_value = 0
        self.D_value = 0

        self.I_max=1
        self.I_min=0

        self.set_point=0.0

        self.prev_value = 0

        self.output = 0

        self.output_fun = output_fun
        self.input_fun = input_fun

        self.last_update_time = pyb.millis()


    def update(self):

        if pyb.millis()-self.last_update_time > 500:
            """
            Calculate PID output value for given reference input and feedback
            """
            current_value = self.input_fun()
            self.error = self.set_point - current_value

            self.P_value = self.Kp * self.error
            self.D_value = self.Kd * ( current_value-self.prev_value)


            lapsed_time = pyb.millis()-self.last_update_time
            lapsed_time/=1000. #convert to seconds
            self.last_update_time = pyb.millis()
            self.I_value += self.error * self.Ki

            if self.I_value > self.I_max:
                self.I_value = self.I_max
            elif self.I_value < self.I_min:
                self.I_value = self.I_min

            self.output = self.P_value + self.I_value - self.D_value

            if self.output<0:
                self.output = 0.0
            if self.output>100:
                self.output = 1.0


            self.output_fun(self.output)

            self.last_update_time=pyb.millis()

def touchlisten():
    x,y=ts.Point_Listen()
    if y <160 and y>320:
        if x<160:
            changespeed(100) #点击的是加速领域
        elif x>160:
            changespeed(-100) #点击的是减速领域
            
def ILI9341_control_PWM(num):
    pwm1=machine.PWM(machine.Pin(18))
    pwm2=machine.PWM(machine.Pin(19))
    pwm2.duty(0)

    for y in range(100):
        for i in range(7,13):
            temdert = random()
            for x in range(5):
                speeddert = random()
                setnum((i*5+x-5)*10,(i*5-5+x)*10-10+20*speeddert,21+0.3*temdert,10)
                sleep_ms(400)
                pwm1.duty(i*x*10)
            for x in range(20):
                speeddert = random()
                setnum(i*5*10,i*5*10+-1+2*speeddert,21+0.3*temdert,10)
                sleep_ms(400)
                pwm1.duty(i*5*10)
            for x in range(20):
                speeddert = random()
                setnum(i*5*10,i*5*10+-1+2*speeddert,21+0.3*temdert,20)
                sleep_ms(400)
                pwm1.duty(i*5*10)
                _thread.exit()
_thread.start_new_thread( ILI9341_control_PWM , (2123, ) )  
# ILI9341_control_PWM(1111)
CLOCKPIN = 5
DATAPIN = 6
timeold=time()
def rotaryChange(direction):
    PIDdealtime(time()-timeold)
    timeold=time()

motor=mymotor(300)

ky040 = KY040(CLOCKPIN, DATAPIN, rotaryCallback=rotaryChange)
ky040.start()
from PID import PID
pid = PID(1, 0.2, 0.05, setpoint=1, scale='us')
def PIDdealtime(time,speed):
    controlled_system.update(1/time)
    control = pid.update(time,(speed-250)/500)
    motor.run(1/control)
    setnum(control*500+250)



def Dealtemp(tempreture):
    num=tempreture[2]
    f=float(tempreture[3])
    t=num+f
    setnum(tempreture=t)

from machine import UART

uart = UART(1, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters
def updatetemp():
    t=uart.read()
    Dealtemp(tempreture=t)
    sleep_ms(10000)

_thread.start_new_thread( updatetemp , ( ) )  

