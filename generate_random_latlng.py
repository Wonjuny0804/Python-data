# 37.444265, 126.825731
# 37.688567, 127.141360
import random
import string

if __name__ == '__main__':
    sLat = float(input('Start Lat\n'))
    eLat = float(input('End Lat\n'))
    sLng = float(input('Start Lat\n'))
    eLng = float(input('End Lat\n'))
    batch = int(input('How many random locations do you want?\n'))


    for i in range(batch):
        lat = random.uniform(sLat, eLat)
        lng = random.uniform(sLng, eLng)
        print("{"+"lat: {0}, lng: {1}".format(lat, lng)+"}", end=",")
