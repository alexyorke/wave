# wave
Set your desktop picture to a new [unsplash](https://unsplash.com/) photo everyday. No dependencies, except for python. Works on Windows, Linux, and macOS.

![unsplash](https://source.unsplash.com/category/nature/900x400)

## Usage

```bash
usage: wave.py [-h] [--length LENGTH] [--height HEIGHT] --path PATH
               [--category CATEGORY] [--format FORMAT] [--quality QUALITY]

optional arguments:
  -h, --help           show this help message and exit
  --length LENGTH      the length of the picture in pixels. Defaults to
                       desktop size.
  --height HEIGHT      the height of the picture in pixels. Defaults to
                       desktop size.
  --path PATH          path to the temp location to save the unsplash photo
  --category CATEGORY  the type of picture (e.g. nature, sky)
  --format FORMAT      the format the photo should be downloaded in (png or
                       jpg)
  --quality QUALITY    the quality of the jpg file (from 0 to 100.)This has no
                       effect if using png format.
```

Examples:

`python wave.py --path ~/Pictures/unsplash.jpg` (sets desktop to random unsplash wallpaper in jpg format with quality 80)

`python wave.py --format jpg --quality=100 --category nature --path ~/Pictures/unsplash.jpg` (will set desktop picture to a random nature photo, in jpg, with the quality of 100)


## Credits
Inspired by https://github.com/splash-wallpapers/splash-cli

http://stackoverflow.com/questions/431205/how-can-i-programatically-change-the-background-in-mac-os-x

http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python

http://stackoverflow.com/questions/110362/how-can-i-find-the-current-os-in-python
