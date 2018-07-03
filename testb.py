from PIL import Image
from word2image import image2word

image = Image.open("test.png")

message = image2word(image)

print(''.join(message))