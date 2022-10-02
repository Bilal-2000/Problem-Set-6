from PIL import Image, ImageOps
import sys


def main():
    shirt = Image.open("shirt.png")
    muppetPic = Image.open("before1.png")

    # crop and resize before/muppet pic
    muppetCropped = ImageOps.fit(
        muppetPic, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    # paste shirt over muppet croppped image
    muppetCropped.paste(shirt, box=None, mask=shirt)

    # save new pic as 2nd CLI arg name
    muppetCropped.save("result.png")


if __name__ == "__main__":
    main()
