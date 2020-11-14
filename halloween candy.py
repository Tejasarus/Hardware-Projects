import RPi.GPIO as GPIO
import time

# Set up for the necessary GPIO PINS

GPIO.setmode(GPIO.BOARD)
channel = 40
PIR = 11


GPIO.setup(channel, GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)

# Motor control functions

def motor_on(pin):
    GPIO.output(pin,GPIO.HIGH)
    
def motor_off(pin):
    GPIO.output(pin,GPIO.LOW)

# Give the motion sensor time to set up

print("intializing...")
time.sleep(2)
print("ready")
x=1

# Main program (Run the motor when motion is detected)

if __name__ == '__main__':
    try:
        while(True):
            if(GPIO.input(PIR) == True):
                print("motion")
                print(x)
                x = x+1
        
                motor_off(channel)
                time.sleep(0.5)
                motor_on(channel)
                time.sleep(2)
                print("ready")
                
            
                
            
        
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
