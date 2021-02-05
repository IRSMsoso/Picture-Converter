from PIL import Image
import keyboard
from time import sleep
import mouse

wool_colors = ((228, 228, 228, "White"),
               (160, 167, 167, "Light Gray"),
               (65, 65, 65, "Dark Gray"),
               (24, 20, 20, "Black"),
               (158, 43, 39, "Red"),
               (234, 126, 53, "Orange"),
               (194, 181, 28, "Yellow"),
               (57, 186, 46, "Lime Green"),
               (54, 75, 24, "Green"),
               (99, 135, 210, "Light Blue"),
               (38, 113, 145, "Cyan"),
               (37, 49, 147, "Blue"),
               (126, 52, 191, "Purple"),
               (190, 73, 201, "Magenta"),
               (217, 129, 153, "Pink"),
               (86, 51, 28, "Brown"))


def nearest_colour(subjects, query):
    return min(subjects, key=lambda subject: sum((s - q) ** 2 for s, q in zip(subject, query)))


def enter_command(s):
    keyboard.press_and_release('t')
    sleep(0.06)
    keyboard.write(s)
    sleep(0.06)
    keyboard.press_and_release('enter')


img = Image.open("picture.jpg")

print("Block size needed: " + str((int(img.size[0]/16), int(img.size[1]/16))))

pix = img.load()

print("Input Start Y for picture")
ystart = input()
print("Enter Start X coordinate")
xstartcoord = float(input())
print("Enter Start Y coordinate")
ystartcoord = float(input())
print("Enter Start Z coordinate")
zstartcoord = float(input())
# print("Enter direction (north|south|east|west)")
# direction_dict = {'north':180, 'south':0, 'east':270, 'west':90}
# x_rotation = direction_dict[input()]
x_rotation = 270

the_stack = []

print("Parsing Picture...")

for y in range(int(ystart) * 16, img.height):
    for x in range(0, img.width):
        the_stack.append((x, y, nearest_colour(wool_colors, img.getpixel((x, y)))[3]))

print("Number of Blocks:", len(the_stack))

xcoordbase = xstartcoord + 0.5
ycoordbase = ystartcoord + 0.35
zcoordbase = zstartcoord + 0.03125

for i in range(5):
    print(5 - i)
    sleep(1)


hotkey_dict = {"White":1,
               "Light Gray": 2,
               "Dark Gray": 4,
               "Black": 5,
               "Red": 9,
               "Orange": 0,
               "Yellow": 0,
               "Lime Green": 0,
               "Green": 8,
               "Light Blue": 6,
               "Cyan": 3,
               "Blue": 0,
               "Purple": 0,
               "Magenta": 0,
               "Pink": 0,
               "Brown": 7}


for bit in the_stack:
    hotkey_num = hotkey_dict[bit[2]]
    if hotkey_num != 0:
        keyboard.press_and_release(str(hotkey_num))
        sleep(0.1)
        enter_command("/teleport TBGOTWWATY " + str(xcoordbase) + " " + str(ycoordbase - 0.0625 * bit[1]) + " " + str(
            zcoordbase + 0.0625 * bit[0]) + " " + str(x_rotation) + " 0")
        sleep(0.1)
        mouse.right_click()
    sleep(0.1)
    if keyboard.is_pressed('shift'):
        break




