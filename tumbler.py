import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm_frequency = 50
pwm.set_pwm_freq(pwm_frequency)
servo_min = (145 * pwm_frequency) // 50
servo_max = (580 * pwm_frequency) // 50

def servoSetting(angle):
    return ((servo_max - servo_min) * angle//180 + servo_min)

def motorSetting(speed):
    return int(speed * 4095.0 / 100.0)

def Tumble(servo1, servo2):
    pwm.set_pwm(servo1, 0, servoSetting(180))
    pwm.set_pwm(servo2, 0, servoSetting(0))
    time.sleep(1)
    pwm.set_pwm(servo1, 0, servoSetting(0))
    pwm.set_pwm(servo2, 0, servoSetting(180))
    time.sleep(1)

if __name__ == '__main__':
    try:

        pwm.set_pwm(1, 0, servoSetting(0))
        pwm.set_pwm(0, 0, servoSetting(180))
        pwm.set_pwm(2, 0, servoSetting(0))
        pwm.set_pwm(3, 0, servoSetting(180))
        #pwm.set_pwm(2, 0, servoSetting(90))
        #pwm.set_pwm(3, 0, servoSetting(90))
        print("Proceed with code?")
        inpt = input()
        noError = True
        while noError:
            Tumble(1,0)
            Tumble(2,3)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        pwm.set_pwm(1, 0, servoSetting(0))
        pwm.set_pwm(0, 0, servoSetting(180))
        pwm.set_pwm(2, 0, servoSetting(0))
        pwm.set_pwm(3, 0, servoSetting(180))
        time.sleep(1)
        print("Program stopped by User")
        #GPIO.cleanup()
