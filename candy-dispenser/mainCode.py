import RPi.GPIO as GPIO
import time

jr = 0
c = 0
spk = 0
l = 0

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
    jr = jr + 1
    print('Dispensing Jolly Ranchers.')
    GPIO.output(Motor1A,GPIO.HIGH)
    time.sleep(5)
    
  if(GPIO.input(24) ==1):
    c = c + 1
    print('Dispensing caramel.')
    GPIO.output(Motor1B,GPIO.HIGH)
    time.sleep(5)

  if(GPIO.input(24) ==1):
    spk = spk + 1
    print('Dispensing Sour Patch.')
    GPIO.output(Motor1C,GPIO.HIGH)
    time.sleep(5)
    
  if(GPIO.input(24) ==1):
    l = l + 1
    print('Dispensing LifeSavers.')
    GPIO.output(Motor1D,GPIO.HIGH)
    time.sleep(5)
