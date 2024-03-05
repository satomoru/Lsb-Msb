from PIL import Image

img = Image.open('test.png')

file = open('test.py', 'rb').read()
file_bytes = bytearray(file)
data_index = 0
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixel = list(img.getpixel((i, j)))
        for k in range(3):
            if data_index < len(file_bytes):
                pixel[k] = file_bytes[data_index]
                data_index += 1
        img.putpixel((i, j), tuple(pixel))
img.save('termux_community_uz.png')
￼Enter
