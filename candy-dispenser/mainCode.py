import RPi.GPIO as GPIO
import datetime as dt

#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

Motor1A = 2
Motor1B = 3
Motor1C = 4
Motor1D = 18

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  if(GPIO.input(23) ==1):
    print('Dispensing Jolly Ranchers.')
    GPIO.output(Motor1A,GPIO.HIGH)
    time.sleep(5)
  if(GPIO.input(24) ==1):
    print('Dispensing caramel.')
    

print('Activating.')
