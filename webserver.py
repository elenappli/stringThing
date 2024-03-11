import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from flask import Flask

#GPIO Pins
direction = 14 # DIR:Green wire 
step = 15 # STEP:Blue Wire
EN_pin = 24 # ENABLE:not used

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

app = Flask(__name__)


@app.route('/steps/<input>')
def set_steps(input):
    print(input)


    mymotortest.motor_go(False, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     int(input), # number of steps
                     .0005, # step delay [sec]
                     False, # True = print verbose output
                     .05) # initial delay [sec]

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
