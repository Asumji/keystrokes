import time
import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller as MouseController

keyboard = Controller()
mouse = MouseController()
time.sleep(2)
print(mouse.position)

keyboard.press(Key.cmd_l)
keyboard.press("r")
keyboard.release(Key.cmd_l)
keyboard.release("r")
mouse.click(Button.left)

time.sleep(0.5)

mouse.position = (112, 720)
keyboard.type("cmd")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(0.5)

mouse.position = (500, 282)
mouse.click(Button.left)
keyboard.type("python")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.type("answer = input('Is this my home? ')")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(4)

keyboard.type("if (answer.upper() == 'NO'):\n print('Wooooooow buli!')\nelif (answer.upper() == 'YES'):\n print('Nice of you to say that c:')\nelse:\n print('Gib better answer!')")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

# keyboard.type("for i in range(1, 11):\n print('gotcha!')")
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)
# keyboard.press(Key.enter)
# keyboard.release(Key.enter)