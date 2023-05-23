from PIL import ImageGrab as ig
import pyautogui as pg

def isCollision(data):
    for i in range(940,980):
        for j in range(330,360):
            print(data[i,j])
            if data[i,j] < 100:
                print('Pulando')
                pg.keyDown('up')
                return
    return


while True:
    image = ig.grab().convert("L")
    data = image.load()
    isCollision(data)
    """for i in range(940,980):
        for j in range(330,360):
            data[i,j] = 0
    image.show()
    break"""