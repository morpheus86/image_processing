from PIL import Image, ImageFilter

img = Image.open("./pokedex/hous.jpg")
# filter_image = img.filter(ImageFilter.BLUR)
# filter_image_smooth = img.filter(ImageFilter.SMOOTH)
# box = (200, 200, 800, 800)
# filter_img_crop = img.crop(box)
# filter_img_crop.save("crop.png", "png")
# # convert to black and white, blurr and smoothing the picture
# filter_img_convert = img.convert("L")
# filter_image.save("blur.png", "png")
# filter_image_smooth.save("smooth.png", "png")
# filter_img_convert.save("grey.png", "png")

img.thumbnail((400, 400))
img.save("thumbnail.jpg")
