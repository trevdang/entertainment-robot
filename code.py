## Multi-purpose import
import time
import digitalio
import analogio
import board
import simpleio
import terminalio
## Import for keypad
import adafruit_matrixkeypad
## Import for motor
import pwmio
from adafruit_motor import servo
## Import for TFT display
import displayio
from adafruit_display_text import label
import adafruit_st7735r

def main():
    ## Define pin connected to piezo buzzer.
    PIEZO_PIN = board.D5
    photocell = analogio.AnalogIn(board.D2)

    ## Define rows, columns and actual keys for keypad use
    ## First row of keys not used
    cols = [digitalio.DigitalInOut(x) for x in (board.A2, board.A1, board.A0)]
    rows = [digitalio.DigitalInOut(x) for x in (board.A5, board.A4, board.A3)]
    keys = ((4, 5, 6),
            (7, 8, 9),
            ('*', 0, '#'))

    ## Create keypad object
    keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

    ## Create PWMOut objects connected to servo
    upperRight = pwmio.PWMOut(board.D10, frequency=50)#upper right
    upperLeft = pwmio.PWMOut(board.D11, frequency=50)#upper left
    lowerRight = pwmio.PWMOut(board.D12, frequency=50)#lower right
    lowerLeft = pwmio.PWMOut(board.D13, frequency=50)#lower left

    ## Create Servo objects for 4 servos.
    uLeft = servo.Servo(upperLeft)
    lLeft = servo.Servo(lowerLeft)
    uRight = servo.Servo(upperRight)
    lRight = servo.Servo(lowerRight)

    ## Level the feet at the start
    reset(uRight, lRight, uLeft, lLeft)

    ## Clear the display
    displayio.release_displays()

    ## Set up pins for our TFT display
    spi = board.SPI()
    tft_cs = board.D9
    tft_dc = board.D7

    ## Create display bus
    display_bus = displayio.FourWire(
        spi, command=tft_dc, chip_select=tft_cs, reset=board.D9
    )

    ## Create display object
    display = adafruit_st7735r.ST7735R(display_bus, width=160, height=128, rotation=90, bgr=True)

    ## Display instruction
    displayText("Lights off to begin", display, 1, 11, 64)

    ## Start up robot if lights off
    while photocell.value >= 40000:
        time.sleep(0.5)

    ## Artificial booting up
    displayText("Booting up...", display, 1, 11, 64)
    time.sleep(3.0)

    ## Display the menu
    displayMenu(display)

    ## Wait for user input
    while True:
        ## Get pressed keys
        keys = keypad.pressed_keys

        ## Do an action corresponding to the key pressed
        if keys and keys[-1] == 4:
            ## Do a dance name display
            countDown("Banana\nSplit", display, 34, 40)
            ## Draw corresponding image on TFT display
            draw(display, "/banana.bmp")
            ## Do the dance
            dance1(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        elif keys and keys[-1] == 5:
            ## Do a dance name display
            countDown("Shuffle", display, 28, 60)
            ## Draw corresponding image on TFT display
            draw(display, "/shuffle.bmp")
            ## Do the dance
            dance2(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        elif keys and keys[-1] == 6:
            ## Do a dance name display
            countDown("Swan \nLake", display, 40, 40)
            ## Draw corresponding image on TFT display
            draw(display, "/swan.bmp")
            ## Do the dance
            dance3(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        elif keys and keys[-1] == 7:
            ## Do a dance name display
            countDown("Butter", display, 32, 60)
            ## Draw corresponding image on TFT display
            draw(display, "/butter.bmp")
            ## Do the dance
            dance4(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        elif keys and keys[-1] == 8:
            ## Do a dance name display
            countDown("Shivers", display, 28, 60)
            ## Draw corresponding image on TFT display
            draw(display, "/shivers.bmp")
            ## Do the dance
            dance7(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        elif keys and keys[-1] == 9:
            ## Do a dance name display
            countDown("Kirby", display, 36, 60)
            ## Draw corresponding image on TFT display
            draw(display, "/kirby.bmp")
            ## Do the dance
            dance8(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        elif keys and keys[-1] == "#":
            ## Do a dance name display
            countDown("Banger", display, 32, 60)
            ## Draw corresponding image on TFT display
            draw(display, "/hula.bmp")
            ## Do the dance w/ music
            asap_dance(PIEZO_PIN, uRight, lRight, uLeft, lLeft)
            ## Bow to the audience
            his_last_bow(uRight, lRight, uLeft, lLeft)
            time.sleep(5.0)
            ## Go back to displaying the menu
            displayMenu(display)
#         elif keys and keys[-1] == "*":
#             draw(display)
#            displayMenu(display)
        elif keys and keys[-1] == 0:
            ## Do all the dances in sequence
            dance1(uRight, lRight, uLeft, lLeft)
            dance2(uRight, lRight, uLeft, lLeft)
            dance3(uRight, lRight, uLeft, lLeft)
            dance4(uRight, lRight, uLeft, lLeft)
            dance7(uRight, lRight, uLeft, lLeft)
            dance8(uRight, lRight, uLeft, lLeft)
            ## Go back to displaying the menu
            displayMenu(display)
        time.sleep(0.1)

# Display the menu
def displayMenu(display):
    displayText('Keys 4-9 - Basic \n           Dances\n\nKeys 0 - All Dances\n\nKeys # - Banger', display, 1, 11, 20)

# Level the feet
def reset(uRight, lRight, uLeft, lLeft):
    lRight.angle = 90
    lLeft.angle = 95
    uLeft.angle = 90
    uRight.angle = 90

# The first dance
def dance1(uRight, lRight, uLeft, lLeft):
    reset(uRight, lRight, uLeft, lLeft)
    for i in range(3): #needs fixing
        lRight.angle = 100 # power motor to move 0.0
        lLeft.angle = 100
        time.sleep(0.5)
        lRight.angle = 50
        lLeft.angle = 140
        time.sleep(0.5)
    reset(uRight, lRight, uLeft, lLeft)

# The second dance
def dance2(uRight, lRight, uLeft, lLeft):
    reset(uRight, lRight, uLeft, lLeft)
    for i in range(3):
        uRight.angle = 90
        uLeft.angle = 90
        time.sleep(0.5)
        uRight.angle = 135
        uLeft.angle = 135
        time.sleep(0.5)
        uRight.angle = 90
        uLeft.angle = 90
        time.sleep(0.5)
        uRight.angle = 45
        uLeft.angle = 45
        time.sleep(0.5)
    reset(uRight, lRight, uLeft, lLeft)

# The third dance
def dance3(uRight, lRight, uLeft, lLeft):
    reset(uRight, lRight, uLeft, lLeft)
    for i in range(3): #needs fixing
        lRight.angle = 100 # power motor to move 0.0
        lLeft.angle = 100
        time.sleep(0.5)
        lRight.angle = 180
        lLeft.angle = 30
        time.sleep(0.5)
    reset(uRight, lRight, uLeft, lLeft)

# The fourth dance
def dance4(uRight, lRight, uLeft, lLeft):
    reset(uRight, lRight, uLeft, lLeft)
    for i in range(3):
        lRight.angle = 180
        time.sleep(0.5)
        lRight.angle = 110
        time.sleep(0.5)
        lLeft.angle = 0
        time.sleep(0.5)
        lLeft.angle = 90
        time.sleep(0.5)
    reset(uRight, lRight, uLeft, lLeft)

# The seventh dance
def dance7(uRight, lRight, uLeft, lLeft):
    reset(uRight, lRight, uLeft, lLeft)
    for i in range(3):
        for angle in range(90, 135, 5):  # 90 - 135 degrees, 5 degrees at a time.
            uRight.angle = angle
            uLeft.angle = angle
            lRight.angle = 180 - angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(135, 45, -5):  # 135 - 45 degrees, 5 degrees at a time.
            uRight.angle = angle
            uLeft.angle = angle
            lRight.angle = 180 - angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(45, 90, 5):  # 45 - 90 degrees, 5 degrees at a time.
            uRight.angle = angle
            uLeft.angle = angle
            lRight.angle = 180 - angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
    reset(uRight, lRight, uLeft, lLeft)

# The eighth dance
def dance8(uRight, lRight, uLeft, lLeft):
    reset(uRight, lRight, uLeft, lLeft)
    for i in range(3):
        for angle in range(90, 20, -5):  # 90 - 20 degrees, 5 degrees at a time.
            lRight.angle = angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(20, 90, 5):  # 20 - 90 degrees, 5 degrees at a time.
            lRight.angle = angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(90, 160, 5):  # 90 - 160 degrees, 5 degrees at a time.
            lRight.angle = angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
        for angle in range(90, 135, 5):  # 90 - 135 degrees, 5 degrees at a time.
            uRight.angle = angle
            uLeft.angle = angle
            time.sleep(0.05)
        for angle in range(135, 45, -5):  # 135 - 45 degrees, 5 degrees at a time.
            uRight.angle = angle
            uLeft.angle = angle
            time.sleep(0.05)
        for angle in range(45, 90, 5):  # 45 - 90 degrees, 5 degrees at a time.
            uRight.angle = angle
            uLeft.angle = angle
            time.sleep(0.05)
        for angle in range(160, 90, -5):  # 160 - 90 degrees, 5 degrees at a time.
            lRight.angle = angle
            lLeft.angle = 180 - angle
            time.sleep(0.05)
    reset(uRight, lRight, uLeft, lLeft)

## Bow to audience
def his_last_bow(uRight, lRight, uLeft, lLeft):
    ## Stand on 1 leg
    while True:
        lRight.angle = 50
        time.sleep(1.0)
        break

    while True:
        uLeft.angle = 30
        time.sleep(1.0)
        break

    while True:
        lLeft.angle = 70
        time.sleep(1.0)
        break

    while True:
        uRight.angle = 50
        time.sleep(1.0)
        break

    while True:
        lLeft.angle = 150
        time.sleep(1.0)
        break

## Do a dance while playing the song
def fortnite_dance(PIEZO_PIN, uRight, lRight, uLeft, lLeft):
    # Define a list of tones/music notes to play.
    FORTNITE = [622, # Eb 0
            698,     # F  1
            831,     # Ab 2
            932]     # Bb 3
    # Main loop will go through each tone in order up and down.
    for i in range(2):
        # bar 1
        lLeft.angle = 135
        lRight.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(1))    # F
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(0.25)) # F
        lRight.angle = 135
        simpleio.tone(PIEZO_PIN, FORTNITE[2], duration=trans_dur_100(0.25)) # Ab
        uRight.angle = 135
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, FORTNITE[3], duration=trans_dur_100(0.25)) # Bb
        uRight.angle = 45
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[3], duration=trans_dur_100(0.75)) # Bb
        uRight.angle = 90
        uLeft.angle = 90
        simpleio.tone(PIEZO_PIN, FORTNITE[2], duration=trans_dur_100(0.75)) # Ab
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(0.25)) # F
        time.sleep(trans_dur_100(0.75))
        # bar 2
        lLeft.angle = 135
        lRight.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(1))    # F
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(0.25)) # F
        lRight.angle = 135
        simpleio.tone(PIEZO_PIN, FORTNITE[2], duration=trans_dur_100(0.25)) # Ab
        uRight.angle = 135
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, FORTNITE[3], duration=trans_dur_100(0.25)) # Bb
        uRight.angle = 45
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[3], duration=trans_dur_100(0.5))  # Bb
        uRight.angle = 90
        uLeft.angle = 90
        simpleio.tone(PIEZO_PIN, FORTNITE[2], duration=trans_dur_100(0.5))  # Ab
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(0.5))  # F
        lLeft.angle = 135
        lRight.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[0], duration=trans_dur_100(0.25)) # Eb
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(0.5))  # F
        # bar 3
        time.sleep(trans_dur_100(0.5))
        lLeft.angle = 45
        lRight.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[3], duration=trans_dur_100(0.25)) # Bb
        lLeft.angle = 135
        lRight.angle = 135
        simpleio.tone(PIEZO_PIN, FORTNITE[2], duration=trans_dur_100(0.25)) # Ab
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(0.25)) # F
        lLeft.angle = 135
        lRight.angle = 45
        simpleio.tone(PIEZO_PIN, FORTNITE[0], duration=trans_dur_100(0.25)) # Eb
        lLeft.angle = 45
        lRight.angle = 135
        simpleio.tone(PIEZO_PIN, FORTNITE[1], duration=trans_dur_100(2))    # F
        reset(uRight, lRight, uLeft, lLeft)

## Do another dance while playing another song
def asap_dance(PIEZO_PIN, uRight, lRight, uLeft, lLeft):
    # Define a list of tones/music notes to play.
    ASAP = [ 294, # low D   0
             311, # Eb      1
             349, # F       2
             392, # G       3
             440, # A       4
             466, # Bb      5
             523, # high C  6
             587 ] # D      7
    # Main loop will go through each tone in order up and down.
    for i in range(2):
        # bar 1
        simpleio.tone(PIEZO_PIN, ASAP[0], duration=trans_dur_132(1))    # low D
        lRight.angle = 135
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[7], duration=trans_dur_132(1))    # D
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        uRight.angle = 135
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(0.5))  # A
        uRight.angle = 45
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[2], duration=trans_dur_132(0.5))  # F
        # bar 2
        uRight.angle = 45
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[1], duration=trans_dur_132(1))    # Eb
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[6], duration=trans_dur_132(1))    # C
        lRight.angle = 135
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[5], duration=trans_dur_132(0.5))  # Bb
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        # bar 3
        lRight.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[0], duration=trans_dur_132(1))    # low D
        reset(uRight, lRight, uLeft, lLeft)
        lLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        reset(uRight, lRight, uLeft, lLeft)
        uRight.angle = 135
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[0], duration=trans_dur_132(0.25)) # low D
        uRight.angle = 45
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[0], duration=trans_dur_132(0.75)) # low D
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        # bar 4
        lRight.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.25)) # G
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.75)) # G
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[5], duration=trans_dur_132(0.5))  # Bb
        lRight.angle = 135
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(0.5))  # A
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        # bar 5
        simpleio.tone(PIEZO_PIN, ASAP[0], duration=trans_dur_132(1))    # low D
        uRight.angle = 45
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[7], duration=trans_dur_132(1))    # D
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        lRight.angle = 135
        lLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(0.5))  # A
        lRight.angle = 45
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[2], duration=trans_dur_132(0.5))  # F
        # bar 6
        lRight.angle = 135
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[1], duration=trans_dur_132(1))    # Eb
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[6], duration=trans_dur_132(1))    # C
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[5], duration=trans_dur_132(0.5))  # Bb
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.5))  # G
        # bar 7
        time.sleep(trans_dur_132(1))
        uRight.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[7], duration=trans_dur_132(0.5))  # D
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[7], duration=trans_dur_132(0.5))  # D
        uRight.angle = 45
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[7], duration=trans_dur_132(0.5))  # D
        uRight.angle = 135
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[6], duration=trans_dur_132(0.5))  # C
        reset(uRight, lRight, uLeft, lLeft)
        simpleio.tone(PIEZO_PIN, ASAP[5], duration=trans_dur_132(0.5))  # Bb
        lRight.angle = 45
        lLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[6], duration=trans_dur_132(0.5))  # C
        # bar 8
        lRight.angle = 180
        lLeft.angle = 0
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(0.75)) # A
        uRight.angle = 135
        uLeft.angle = 135
        simpleio.tone(PIEZO_PIN, ASAP[3], duration=trans_dur_132(0.25)) # G
        uRight.angle = 45
        uLeft.angle = 45
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        reset(uRight, lRight, uLeft, lLeft)
        time.sleep(trans_dur_132(1))
        lRight.angle = 150
        lLeft.angle = 0
        simpleio.tone(PIEZO_PIN, ASAP[0], duration=trans_dur_132(1))    # D
        # bar 9
        lLeft.angle = 150
        lRight.angle = 0
        simpleio.tone(PIEZO_PIN, ASAP[4], duration=trans_dur_132(1))    # A
        time.sleep(2)
        reset(uRight, lRight, uLeft, lLeft)

## Do an intro before a dance
def countDown(danceMove, display, x ,y):
    displayText(danceMove,display, 2, x, y)
    time.sleep(2.0)

## Helper function for music note durations
def trans_dur_100(dur):
    return (dur*60)/100

## Helper function for music note durations
def trans_dur_132(dur):
    return (dur*60)/132

## Display given text on TFT display
def displayText(dText, display, scl, x, y):
    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    ## Make the bitmap
    color_bitmap = displayio.Bitmap(160, 128, 1)
    ## Create the color palette
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xAA0088  # Bright Green

    ## create a tilegrid and push onto group object
    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Draw a label
    text_group = displayio.Group(scale=scl, x=x, y=y)
    text = dText
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
    text_group.append(text_area)  # Subgroup for text scaling
    # Append subgroup to main group
    splash.append(text_group)

## Draw an image based on given filename
def draw(display, file):
    # Setup the file as the bitmap data source
    bitmap = displayio.OnDiskBitmap(file)

    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(tile_grid)

    # Add the Group to the Display
    display.show(group)

## Start robot
main()
