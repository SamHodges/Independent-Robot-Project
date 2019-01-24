import ASUS.GPIO as GPIO
import time
GPIO.setmode(GPIO.ASUS)


encoder1 = 32
GPIO.setup(encoder1,GPIO.OUT)

print "Turning motor on"
GPIO.output(encoder1,GPIO.HIGH)
sleep(2)
print "Stopping motor"
GPIO.output(encoder1,GPIO.LOW)
GPIO.cleanup()

#ground, power, signal
