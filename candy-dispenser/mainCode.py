import RPi.GPIO as GPIO

#setup GPIO using Board numbering
GPIO.setmode(GPIO.BOARD)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  if(GPIO.input(23) ==1):
    print('Dispensing Jolly Ranchers.')
    

print('Activating.')
