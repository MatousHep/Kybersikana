import umachine
import utime

led=umachine.Pin(11,umachine.Pin.OUT)

while True:
    led.toggle()
    utime.sleep(1)