#create on 23/3/2018
#@author Jw Huang
#create a method to catch POI from Baidu

#-*-coding:UTF-8-*-
import json
import sys
import requests  #导入requests库，这是一个第三方库，把网页上的内容爬下来用的
ty=sys.getfilesystemencoding()  #这个可以获取文件系统的编码形式
import time


# keywords=['医院','学校','餐厅','停车场','商场'，'工厂']
keywords=['公园']
####Wuhan
# lat_1=29.987038
# lon_1=113.697002
# lat_2=31.344301
# lon_2=115.067124   #坐标范围
# las=1  #给las一个值1
#####Hong Kong
# lat_1=113.840957
# lon_1=22.198458
# lat_2=114.415297
# lon_2=22.539096  #坐标范围
# las=1  #给las一个值1
# ak=''###Baidu map api
#ak=''##google map api
ak=''##高德key
push=[]
for k in keywords:
    line='D:/Data/MCTS DATA/POI Data/'+k+'.csv'
    push.append(line)
#我们把变量都放在前面，后面就不涉及到变量了，如果要爬取别的POI，修改这几个变量就可以了，不用改代码了。

#矩形框爬取
# print (time.time())  #相较于python2.7，,python3print 需要加括号。
# print ('开始')
# urls=[] #声明一个数组列表
# lat_count=int((lat_2-lat_1)/las+1)
# lon_count=int((lon_2-lon_1)/las+1)
# for lat_c in range(0,lat_count):
#     lat_b1=lat_1+las*lat_c
#     for lon_c in range(0,lon_count):
#         lon_b1=lon_1+las*lon_c
#         for i in range(0,20):
#             page_num=str(i)
#             #url='http://api.map.baidu.com/place/v2/search?query=学校& bounds='+str(lat_b1)+','+str(lon_b1)+','+str(lat_b1+las)+','+str(lon_b1+las)+'&page_size=20&page_num='+str(page_num)+'&output=json&ak='+ak
#             url='http://restapi.amap.com/v3/place/polygon?polygon='+str(lat_b1)+','+str(lon_b1)+','+str(lat_b1+las)+','+str(lon_b1+las)+'&keywords=医院&output=josn&key='+ak
#             urls.append(url)
#urls.append(url)的意思是，将url添加入urls这个列表中。
#关键字爬取
T=len(keywords)
for l in range(0,T):

    k=keywords[l]
    p=push[l]
    print('现在开始爬取关键字为'+k+'的POI')
    url='http://restapi.amap.com/v3/place/text?keywords='+k+'&city=香港&output=josn&offset='

    html=requests.get(url)
    data=html.json()
    n=int(data['count'])/20
    urls=[]
    for i in range(0,int(n)):
        url = 'http://restapi.amap.com/v3/place/text?keywords='+k+'&city=香港&output=josn&offset=20&page='+str(i+1)+'&key='
        urls.append(url)
    f=open(p,'w')

    print ('url列表读取完成')

    for url in urls:
        time.sleep(10) #为了防止并发量报警，设置了一个10秒的休眠。
        html=requests.get(url)#获取网页信息
        data=html.json()#获取网页信息的json格式数据
    #if data['results'] is not None:
        for item in data['pois']:
            jname=item['name']
            # jlat=item['location']['lat']
            # jlon=item['location']['lng']
            location=item['location']
            location=location.split(',')
            jlat=location[0]
            jlon=location[1]
            #jadd=item['address']
            j_str=jname+','+str(jlat)+','+str(jlon)+','+'\n'
            f.write(j_str)
        print (time.time())
   # else:
    #    continue
    f.close()
print ('完成')
