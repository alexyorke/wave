import urllib
import urllib2
import argparse
from sys import platform

def getScreenSize():
    import gtk
    import pygtk

    if platform.startswith("linux"):
        window = gtk.Window()
        screen = window.get_screen()
        return[int(screen.get_width()), int(screen.get_height())]
    elif platform == "win32":
        from win32api import GetSystemMetrics
        return[int(GetSystemMetrics(0)), int(GetSystemMetrics(1))]
    elif platform == "darwin":
        from Quartz import CGDisplayBounds
        from Quartz import CGMainDisplayID
        mainMonitor = CGDisplayBounds(CGMainDisplayID())
        return (mainMonitor.size.width, mainMonitor.size.height)


def setWallpaper(path):
    if platform.startswith("linux"):
        import commands
        command = "gconftool-2 --set /desktop/gnome/background/" + \
        "picture_filename --type string '" + path + "'"
        status, output = commands.getstatusoutput(command)

        unityCommand = "gsettings set org.gnome.desktop.background " + \
        "picture-uri file://" + path
        statusUnity, outputUnity = commands.getstatusoutput(unityCommand)
        if status is not 0 and statusUnity is not 0:
            print "Error: could not set wallpaper. "
    elif platform == "win32":
            import ctypes
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32 \
            .SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 0)
    else:
        print "Error: can't set wallpaper for " + \
        platform + ". Will be implemented soon."

# get the command-line arguments
parser = argparse.ArgumentParser()

parser.add_argument('--length', type=int,
                    help='the length of the picture in pixels. ' + \
                    'Defaults to desktop size.')
parser.add_argument('--height', type=int,
                    help='the height of the picture in pixels. ' + \
                    'Defaults to desktop size.')

parser.add_argument('--path', type=str,
                    help='path to the temp location to save the ' + \
                    'unsplash photo', required=True)

parser.add_argument('--category', type=str,
                    help='the type of picture (e.g. nature, sky)',
                    required=False)

parser.add_argument('--format', type=str,
                    help='the format the photo should be downloaded' + \
                    ' in (png or jpg)',
                    required=False)
parser.add_argument('--quality', type=int,
                    help='the quality of the jpg file (from 0 to 100.)' + \
                    'This has no effect if using png format.',
                    required=False)


args = parser.parse_args()

category = "random"

# ensure parameters were set correctly
if (category is not None):
    category = args.category

fmt = "jpg"

if (args.format is not None):
    fmt = args.format

if fmt is "png":
    quality = 100

picLength = None
picHeight = None

if args.length is not None and args.height is not None:
    # set height and length to desktop size
    picLength = int(args.length)
    picHeight = int(args.height)
else:
    screenDimensions = getScreenSize()
    picLength = screenDimensions[0]
    picHeight = screenDimensions[1]

fmt = fmt.strip()
if (fmt != "jpg") and (fmt != "png"):
    print "Error: format must be png or jpg"
    exit()

quality = 80
if args.quality is not None:
    quality = int(args.quality)

if quality > 100 or quality < 0:
    print "Error: quality must be between 0 and 100"
    exit()

# download photo
url = "https://source.unsplash.com/" + str(picLength) + \
"x" + str(picHeight) + "/?" + str(category)

var = urllib2.urlopen(url)
url_string = var.geturl()

# this seems to be the url for the 404 error page
if url_string.startswith("https://images.unsplash.com/" + \
                         "photo-1446704477871-62a4972035cd"):
    print "Error: no photos found."
    exit()

url_string = url_string.replace("&q=80", "&q=" + str(quality))
url_string = url_string.replace("&fm=jpg", "&fm=" + fmt)

urllib.urlretrieve(url_string, path + fmt)

setWallpaper(path + fmt)
