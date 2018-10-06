#create on 28/9/2018
#@author Jw Huang
#create a method to get POI details from google,more detail please visit google api for place search.

import sys
import requests
ty=sys.getfilesystemencoding()


#set keywords
keywords=['restaurant']
akey=''#please setting your google_api key for place search & place detail
#set loactionfile
locationfile=r'C:\Users\' #please reset your own file path for location, you need to define search centres, strored as 4 rows, $name,id,lon,lat 
location=[]
location_txt=open(locationfile,'r')
locationhead=location_txt.readline()
for line in location_txt.readlines():
    line=line.strip('\n')
    line=line.split(',')
    location.append(line)
location_txt.close()

n=len(location)
l=len(keywords)
#set outputfile
outputfile=r'C:\Users\' #please reset your output file path, normal as .csv file
headline='name,type,lon,lat,day1,day2,day3,day4,day5,day6,day7' #return detail head name of output file, most important imformation get from google is open_hours of POI
out_text=open(outputfile,'a')
out_text.write(headline+'\n')

for i in range(0,n):
    LocaLine=location[i]
    x=LocaLine[2]
    y=LocaLine[3]
    print('Search area number:',i)
    for j in range(0,l):
        keyword=keywords[j]
        #search place detail
        print('search ',keyword)
        #set nearbysearch Url
        NearBysearch_url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+y+','+x+'&radius=1500'+'&type='+keyword+'&keyword=cruise&key='+akey #search radius is 1500m
        html=requests.get(NearBysearch_url)
        place_search=html.json()
        status=place_search['status']
        if status!='ZERO_RESULTS':
            for item in place_search['results']:
                name=item['name']
                lo=item['geometry']['location']
                lon=lo['lng']
                lat=lo['lat']
                place_id=item['place_id']
                #search place_detail
                place_detail_url='https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&key='+akey
                place_detail=requests.get(place_detail_url)
                place_d=place_detail.json()
                week_txt=[]
                s = name + ',' + keyword + ','+str(lon) + ',' + str(lat)
                for value in place_d['result']['opening_hours']['weekday_text']:
                    week_txt.append(value)
                # weekday_period=week_txt[0]+','+week_txt[1]+','+week_txt[2]+','+week_txt[3]+','+week_txt[4]+','+week_txt[5]+','+week_txt[6]
                for line in week_txt:
                    s=s+','+line
                out_text.write(s+'\n')
out_text.close()
