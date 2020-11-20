# %load /home/altvu/canvas/constructs/grphcsol/blkeasel.py
# %load /home/altvu/canvas/constructs/grphcsol/blkeasel.py
# %load /home/altvu/canvas/constructs/grphcsol/blkeasel.py
#!/usr/bin/python3

from PIL import Image, ImageFilter, ImageEnhance

os = Image.os
path = os.path

intro = (
    f"easel -- a composition of modules and functions for algorithmic artistry\n"
    f"version 0.1\n"
    f"an altvu construct\n"
)


homed = os.environ.get("HOME")
dotd = os.environ.get("PWD")


def image_list(srchd="."):
    flxts = ("png", "jpg", "ppm", "svg", "bpm", "jpeg")
    flist = []
    for dname, dpath, files in os.walk(srchd, topdown=True):
        if len(dname) > 0:
            for f in files:
                if f.endswith(flxts):
                    flist.append(path.join(path.abspath(dname), f))
    return flist


def image_info(filename):
    with Image.open(filename) as im:
        fdeets = (
            f"image: {im.filename}\n"
            f"format: {im.format}\n"
            f"size: {im.size}\n"
            f"mode: {im.mode}\n"
            f"bands: {im.getbands()}\n"
            f"bounding box: {im.getbbox()}\n"
            f"channel: {im.getchannel(0)}\n"
            f"\v"
        )
    print(fdeets.rstrip())
    return {
        im.filename: {
            "format": im.format,
            "size": im.size,
            "mode": im.mode,
            "bands": im.getbands(),
            "bounds": im.getbbox(),
        }
    }


def image_display(filename):
    with Image.open(filename) as im:
        im.show()
    return {"image": im.filename, "format": im.format, "mode": im.mode, "size": im.size}


# def image_focus():
#    imgls, imgdex=image_list(indxf)
#    with open(imgdex) as oneimg:
#        for line in oneimg:
#            idex, ifnm=line.split(' ')
#            print(ifnm)
#            print(line.rstrip())


def main():
    imgls = image_list()


if __name__ == "__main__":
    main()
