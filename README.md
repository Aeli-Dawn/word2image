# Word2Image

Word2Image is a library that converts words to images and those images into words

## Requirements

* [Python 3](https://www.python.org/downloads/)
* Pillow

```
pip3 install Pillow
```

## Usage

### word2image

```
import word2image as w2i
image = w2i.word2image("Some Text")
w2i.saveImage(image, "example.png")
```

### image2word

```
import word2image as w2i
image = w2i.loadImage("example.png")
message = w2i.image2word(image)
```

## Authors

* **Elijah Williams** - *Initial Work* - [TCM-TheCodingManiac](https://github.com/TCM-TheCodingManiac)