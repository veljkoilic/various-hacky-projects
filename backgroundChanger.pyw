import os
import ctypes
import urllib.request
import time

path_user = os.path.expanduser('~')
name_of_file = 'smrt.jpg'
path_to_file = os.path.join(path_user, 'Desktop', name_of_file)

imageURL = 'https://i.ytimg.com/vi/RNoHcWE8tbQ/maxresdefault.jpg'

while 1==1:
    time.sleep(1)
    urllib.request.urlretrieve(imageURL, path_to_file)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_file, 0)
