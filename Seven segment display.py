import RP1.GPIO as gp
import time
from tm1637 import TM1637

gp.setwarnings(False)


clk = 17 #Clock pin
dio = 4 #Data pin


display = TM1637(clk, dio)


def display_time():
    current_time = time.strftime("%H%M") 
    display.number(int(current_time))
    time.sleep(1) 
    print("Displayang....")
    print(current_time)

try:
    for i in range(50):
        display_time()
except KeyboardInterrupt:
    print("Exiting...")
finally:
    display.clear() #Clear the display before exiting
    gp.cleanup()
