# PipDeck
A Pip-Boy inspired macropad console built from 3D printed parts and powered by a Raspberry Pi Pico. 

Customisation:
If you'd like to change the function of the 16 keys/buttons, do the following:
- Familiarise yourself with this page: https://docs.circuitpython.org/projects/hid/en/latest/api.html
- Find the button you'd like to change in the code. For example the top left key (key1) is mapped to Keycode.KEYPAD_SEVEN
- Find the appropriate keycode for the desired result from the CircuitPython documentation above.
- Replace the keycode in the code.py script.

So if you want to reprogramme key1 from Keypad 7 to the F12 function key:

Original: 
```
while True:
    if key1.value is True:
        keyboard.press(Keycode.KEYPAD_SEVEN)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_SEVEN)
```
New:
```
while True:
    if key1.value is True:
        keyboard.press(Keycode.F24)
        time.sleep(0.15)
        keyboard.release(Keycode.F24)  
```
