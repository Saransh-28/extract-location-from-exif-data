# import all the required modules
import PIL.Image as pil
import PIL.ExifTags 
from gmplot import gmplot
from geopy.geocoders import Nominatim
import webbrowser

# open image and extract the metadata of image using pillow
name = str(input('Enter the name of the image - '))
img = PIL.Image.open(name)
exif = {
    PIL.ExifTags.TAGS[i]: x for i,x in img._getexif().items() if i in PIL.ExifTags.TAGS
}

''' extract the gps location (if it is present in metadata) and 
convert it to latitude and longitude format and plot the location using gmplot and save it to map.html ,
used Nominatim from geopy.geocoders to get the name of the location and open map.html using webbrowser '''
try:
    n=exif['GPSInfo'][2]
    e=exif['GPSInfo'][4]
    lat = (((n[0]*60) + n[1]*60)+n[2])/60/60
    lon = (((e[0]*60) + e[1]*60)+e[2])/60/60
    MAP = gmplot.GoogleMapPlotter(lat,lon,10)
    MAP.marker(lat,lon,'mark')
    MAP.draw('map.html')
    location = Nominatim(user_agent='GetLoc')
    location_name = location.reverse(f'{lat} , {lon}')
    print(f'location -- {location_name}')
    webbrowser.open('map.html',new=2)
except:
    print('NO DATA FOUND IN THE IMAGE')
