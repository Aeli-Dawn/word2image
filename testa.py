from PIL import Image
from word2image import word2image

image = word2image("testing")

image.save('test.png')