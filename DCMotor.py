from machine import Pin, PWM


class Moves:
    RIGHT = 'R'
    LEFT = 'L'

    FORWARD = 1
    BACKWARD = 0


class DCMotor:
    def __init__(self, pwm_a=0, pwm_b=2, ai1=13, ai2=15, bi1=12, bi2=14, stby=16):
        self._right = [PWM(Pin(pwm_a), freq=1000), Pin(ai1, Pin.OUT), Pin(ai2, Pin.OUT)]
        self._left = [PWM(Pin(pwm_b)), Pin(bi1, Pin.OUT), Pin(bi2, Pin.OUT)]
        self._stby = Pin(stby, Pin.OUT)
        self._stby.on()

    def move(self, direction, motor, speed=None):
        if speed is not None:
            speed = self.__map_value(speed, 0, 100, 0, 1023)
        if motor == Moves.RIGHT:
            motor = self._right
        elif motor == Moves.LEFT:
            motor = self._left
        else:
            raise Exception('Invalid motor')

        if direction == Moves.FORWARD:
            self.forward(motor, speed)
        elif direction == Moves.BACKWARD:
            self.backward(motor, speed)
        else:
            raise Exception('Invalid direction')

    def stop(self, motor):
        if motor == Moves.RIGHT:
            motor = self._right
        elif motor == Moves.LEFT:
            motor = self._left
        else:
            raise Exception('Invalid motor')
        motor[1].off()
        motor[2].off()

    @staticmethod
    def forward(motor, speed):
        motor[0].duty(speed)
        motor[1].on()
        motor[2].off()

    @staticmethod
    def backward(motor, speed):
        motor[0].duty(speed)
        motor[1].off()
        motor[2].on()

    @staticmethod
    def __map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min