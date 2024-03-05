from PIL import Image

img = Image.open('test.png')
extracted_data = bytearray()
data_index = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixel = list(img.getpixel((i, j)))
        hidden_byte = []
        for k in range(3):
            hidden_byte.append(pixel[k])
        extracted_data.extend(hidden_byte)

with open('extracted_file.py', 'wb') as file:
    file.write(extracted_data)
    
