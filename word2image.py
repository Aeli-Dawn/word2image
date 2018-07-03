from PIL import Image as img

def word2image(string):
	message = list(string)
	picture = img.new("RGB", (8, int(len(message) / 2)))
	pixels = []

	for letter in message:
		l = ord(letter)
		pixels.append((int(l * .5), l, l))

	picture.putdata(pixels)

	return picture

def image2word(picture):
	pixels = picture.getdata()
	message = []

	for tup in pixels:
		message.append(chr(tup[2]))
	
	return message