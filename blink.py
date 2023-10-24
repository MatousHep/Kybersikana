import umachine
import utime

led=umachine.Pin("LED",umachine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)