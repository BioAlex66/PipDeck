# PipDeck WIP Code with Circuitpython on Pico
# Written by BioAlex
# Heavily borrowed from Adafruit tutorials and dronebotworkshop.
import time
import board
import digitalio
import neopixel
import usb_hid
import rotaryio

# Keyboard setup
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Switch setup
togswitch = digitalio.DigitalInOut(board.GP1)
togswitch.switch_to_input(pull=digitalio.Pull.DOWN)

# Keylayout
key1 = digitalio.DigitalInOut(board.GP2)
key1.direction = digitalio.Direction.INPUT
key1.pull = digitalio.Pull.DOWN

key2 = digitalio.DigitalInOut(board.GP3)
key2.direction = digitalio.Direction.INPUT
key2.pull = digitalio.Pull.DOWN

key3 = digitalio.DigitalInOut(board.GP4)
key3.direction = digitalio.Direction.INPUT
key3.pull = digitalio.Pull.DOWN

key4 = digitalio.DigitalInOut(board.GP5)
key4.direction = digitalio.Direction.INPUT
key4.pull = digitalio.Pull.DOWN

key5 = digitalio.DigitalInOut(board.GP6)
key5.direction = digitalio.Direction.INPUT
key5.pull = digitalio.Pull.DOWN

key6 = digitalio.DigitalInOut(board.GP7)
key6.direction = digitalio.Direction.INPUT
key6.pull = digitalio.Pull.DOWN

key7 = digitalio.DigitalInOut(board.GP8)
key7.direction = digitalio.Direction.INPUT
key7.pull = digitalio.Pull.DOWN

key8 = digitalio.DigitalInOut(board.GP9)
key8.direction = digitalio.Direction.INPUT
key8.pull = digitalio.Pull.DOWN

key9 = digitalio.DigitalInOut(board.GP10)
key9.direction = digitalio.Direction.INPUT
key9.pull = digitalio.Pull.DOWN

key10 = digitalio.DigitalInOut(board.GP11)
key10.direction = digitalio.Direction.INPUT
key10.pull = digitalio.Pull.DOWN

key11 = digitalio.DigitalInOut(board.GP12)
key11.direction = digitalio.Direction.INPUT
key11.pull = digitalio.Pull.DOWN

key12 = digitalio.DigitalInOut(board.GP13)
key12.direction = digitalio.Direction.INPUT
key12.pull = digitalio.Pull.DOWN

# Buttons for sound io
# key13 is headphones
key13 = digitalio.DigitalInOut(board.GP14)
key13.direction = digitalio.Direction.INPUT
key13.pull = digitalio.Pull.DOWN

# key14 is headset
key14 = digitalio.DigitalInOut(board.GP15)
key14.direction = digitalio.Direction.INPUT
key14.pull = digitalio.Pull.DOWN

# key15 is speakers
key15 = digitalio.DigitalInOut(board.GP16)
key15.direction = digitalio.Direction.INPUT
key15.pull = digitalio.Pull.DOWN

# key16 is mute
key16 = digitalio.DigitalInOut(board.GP17)
key16.direction = digitalio.Direction.INPUT
key16.pull = digitalio.Pull.DOWN


# Update this to match the number of NeoPixel LEDs connected to your board.
pixel_top = neopixel.NeoPixel(board.GP0, 5)
pixel_top.brightness = 0.5
pixel_butt = neopixel.NeoPixel(board.GP21, 4)
pixel_butt.brightness = 0.3

# Rotary encoder

encoder = rotaryio.IncrementalEncoder(board.GP20, board.GP19)
encbutton = digitalio.DigitalInOut(board.GP18)
encbutton.direction = digitalio.Direction.INPUT
encbutton.pull = digitalio.Pull.UP
cc = ConsumerControl(usb_hid.devices)

encbutton_state = None
last_position = encoder.position

while True:
    if key1.value is True:
        keyboard.press(Keycode.KEYPAD_SEVEN)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_SEVEN)
    if key2.value is True:
        keyboard.press(Keycode.KEYPAD_EIGHT)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_EIGHT)
    if key3.value is True:
        keyboard.press(Keycode.KEYPAD_NINE)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_NINE)
    if key4.value is True:
        keyboard.press(Keycode.KEYPAD_FOUR)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_FOUR)
    if key5.value is True:
        keyboard.press(Keycode.KEYPAD_FIVE)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_FIVE)
    if key6.value is True:
        keyboard.press(Keycode.KEYPAD_SIX)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_SIX)
    if key7.value is True:
        keyboard.press(Keycode.KEYPAD_ONE)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_ONE)
    if key8.value is True:
        keyboard.press(Keycode.KEYPAD_TWO)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_TWO)
    if key9.value is True:
        keyboard.press(Keycode.KEYPAD_THREE)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_THREE)
    if key10.value is True:
        keyboard.press(Keycode.KEYPAD_PERIOD)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_PERIOD)
    if key11.value is True:
        keyboard.press(Keycode.KEYPAD_ZERO)
        time.sleep(0.15)
        keyboard.release(Keycode.KEYPAD_ZERO)
    if key12.value is True:
        keyboard.press(Keycode.WINDOWS, Keycode.L)
        time.sleep(0.15)
        keyboard.release(Keycode.ENTER)
    if key13.value is True:
        keyboard.press(Keycode.F21)
        pixel_butt[0] = (255,255,255)
        time.sleep(0.3)
        keyboard.release(Keycode.F21)
    if key14.value is True:
        keyboard.press(Keycode.F22)
        pixel_butt[1] = (255,255,255)
        time.sleep(0.3)
        keyboard.release(Keycode.F22)
    if key15.value is True:
        keyboard.press(Keycode.F23)
        pixel_butt[2] = (255,255,255)
        time.sleep(0.3)
        keyboard.release(Keycode.F23)
    if key16.value is True:
        keyboard.press(Keycode.F24)
        pixel_butt[3] = (255,255,255)
        time.sleep(0.3)
        keyboard.release(Keycode.F24)
    if togswitch.value is True:
        pixel_top.fill((0, 255, 0))
        pixel_butt.fill((255, 50, 0))

    else:
        pixel_top.fill((255, 50, 0))
        pixel_butt.fill((0, 50, 255))

    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        print(current_position)
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        print(current_position)
    last_position = current_position
    if not encbutton.value and encbutton_state is None:
        encbutton_state = "pressed"
    if encbutton.value and encbutton_state == "pressed":
        print("Button pressed.")
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        encbutton_state = None


