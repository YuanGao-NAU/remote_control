#!/usr/bin/env python
# Fuck!
import RPi.GPIO as GPIO
import time
def DHT11(pin):
	    data = []
	    GPIO.setmode(GPIO.BCM)
	    time.sleep(1)
	    GPIO.setup(pin, GPIO.OUT)
	    GPIO.output(pin, GPIO.LOW)
	    time.sleep(0.02)
	    GPIO.output(pin, GPIO.HIGH)
	    GPIO.setup(pin, GPIO.IN)
	    while GPIO.input(pin) == GPIO.LOW:
		        continue
	    while GPIO.input(pin) == GPIO.HIGH:
		        continue
	    i = 0
	    while i < 40:
		        j = 0
		        while GPIO.input(pin) == GPIO.LOW:
			            continue
        while GPIO.input(pin) == GPIO.HIGH:
			            j += 1
			            if j> 100:
				                break   
		         if j < 8:
			            data.append(0)
		        else:
			            data.append(1)
		        i += 1
	    print "sensor is working"
    #print data
	    humidity_bit = data[0:8]
	    humidity_point_bit = data[8:16]
	    temperature_bit = data[16:24]
	    temperature_point_bit = data[24:32]
	    check_bit = data[32:40]
	    humidity = 0
	    humidity_point = 0
	    temperature = 0
	    temperature_point = 0
	    check = 0
	    for i in range(8):
		        humidity += humidity_bit[i] * 2 ** (7-i)
		        humidity_point += humidity_point_bit[i] * 2 ** (7-i)
		        temperature += temperature_bit[i] * 2 ** (7-i)
		        temperature_point += temperature_point_bit[i] * 2 ** (7-i)
 		        check += check_bit[i] * 2 ** (7-i)
	    tmp = humidity + humidity_point + temperature + temperature_point
	    if check == tmp:
		        print "temperature :", temperature, "*C, humidity:", humidity, "%"
		        return(temperature,humidity)
	    else:
		        print("wrong")
		        return(False,False)
	    GPIO.cleanup()
if __name__=='__main__':
    pin =21
	    T,H = DHT11(pin)

作者：ATangYaaaa
链接：https://www.jianshu.com/p/6cae5ae7957f
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
