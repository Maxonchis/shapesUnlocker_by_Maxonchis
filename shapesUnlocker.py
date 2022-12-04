# based on script by Rockstar94
# edit by Maxonchis t.me/maxonchis

import os

mask = ".i3d.shapes"
unlockCount = 0
shapesCount = 0

def main():
    global shapesCount
    dlcPath = input("Specify the path DLC or any folder with shapes files. For example E:\Giants Engine\YourFolder: ")

    if not dlcPath:
        dlcPath = os.getcwd()

    for top, dirs, files in os.walk(dlcPath):
        for nm in files:
            if nm.endswith(mask):
                shapesCount += 1
                shapePath = os.path.join(top, nm)
                UnlockFile(shapePath)

    print(f"Total shapes unlocked {unlockCount} from {shapesCount}\n")
    print("#" * 40)
    print("Script edit by Maxonchis. t.me/maxonchis")
    print("#" * 40)

def UnlockFile(src):
    f = open(src, "r+b")
    srcFile = bytearray(f.read())

    global unlockCount

    if srcFile[0] == 7 or srcFile[0] == 5 or srcFile[0] == 0 or srcFile[0] == 1:
        logTextFS = 'FS15'
        logTextUnl = ''
        if srcFile[0] == 5 or srcFile[0] == 7:
            logTextFS = 'FS17/FS19/FS22'
            if srcFile[1] == 32:
                ChangeBytes(srcFile, 2)
                srcFile[1] = 0
                srcFile[3] = 0
                f.seek(0)
                f.write(srcFile)
                unlockCount += 1
            else:
                logTextUnl = ' already'
        else:
            if srcFile[2] == 128:
                ChangeBytes(srcFile, 1)
                srcFile[0] = 0
                srcFile[2] = 0
                f.seek(0)
                f.write(srcFile)
                unlockCount += 1
            else:
                logTextUnl = ' already'
        print(logTextFS + ' .shapes file: "{0}"'.format(src) + logTextUnl + ' unlocked!')
    else:
        print('Unknown .shapes file format: "{0}"'.format(src))

def ChangeBytes(file, nr):
    newValue = file[nr] - 13
    hexValue = hex(newValue & (2 ** 8 - 1))
    intValue = int(hexValue, 16)
    file[nr] = intValue

if __name__ == '__main__':
    main()
