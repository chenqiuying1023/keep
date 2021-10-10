
import requests
import base64
from pyquery import PyQuery as pq  
import time
import pandas as pd 
from pprint import pprint

import pymongo

import hashlib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_proxies_headers():
    spiderId=''
    secret=''
    orderno=''
    proxy='forward.xdaili.cn:80'
    proxies={
        'http':'http://'+proxy,
        'https':'https://'+proxy,
    }
    timestamp = str(int(time.time()))
    planText="orderno={},secret={},timestamp={}".format(orderno,secret,timestamp)
    s=planText.encode()
    md5_string = hashlib.md5(s).hexdigest()
    sign=md5_string.upper()
    headers={
        'Proxy-Authorization':'sign={}&orderno={}&timestamp={}'.format(sign,orderno,timestamp),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    return proxies,headers

proxies,headers1=get_proxies_headers()

### MongoDB数据库连接
client=pymongo.MongoClient(host='localhost',port=27017)  # 数据库连接接口
db=client['keep_app']  # 指定数据库
collection=db['list_info']  # 指定集合，类似于表
collection_new=db['detail_info']


### 列表页面信息采集
api='https://api.gotokeep.com/feed/v1/feed/list'
params={
    'feedType':'sports',
    'limit':6,
    'needCommentInfo':0,
    'needFavoriteInfo':1,
    'needFellowshipInfo':1,
    'needLikeInfo':1,
    'needRelationInfo':1,
    'sort':'byTime',
}
response=requests.get(url=api,params=params)
# print(response.text)
json=response.json()
# pprint(json)
lastId=json['data']['lastId'].replace('entry','')
item_list=json['data']['items']
print(lastId)
# for item in item_list:
#     with open(r'E:\jiedan\Atongyongjiedan\keep_list_all.json','a',encoding='utf-8') as fa:
#         fa.write(str(item)+'\n')
#     # pprint(item)
#     # break
index=0
while True:
    index+=1
    print('*'*80)
    print(index)
    headers2={
        'Host': 'api.gotokeep.com',
        'x-model-raw': 'iPhone7,2',
        'x-screen-width': '375',
        'User-Agent': 'Keep/7.8.1 (iPhone; iOS 12.5.2; Scale/2.00)',
        'x-is-new-device': 'true',
        'x-timestamp': '1629374440851',
        'x-session-id': '1629400340',
        'x-bundleId': 'com.gotokeep.keep',
        'x-os': 'iOS',
        'x-keep-timezone': 'Asia/Shanghai',
        'x-device-id': 'b9e9e4a8814d43c58f68bd9cc4b8e4407e47b8fa',
        'x-os-version': '12.5.2',
        'x-channel': 'Apple Store',
        'x-ads': 'DtkeXyV6Gah1gVU2VLjQVt1YNvIoD7cT912+jWjEPcWxKimCYfqb9us+phX86ZO2MJ+d2jpZ3gJWudtchF+j6Z3oX0XZfKp1a0RHUggZuhCS+ZzGi19kmjU1Fw5GHb1+5G+gbWRV0pN53Ms8clIKwXPFF6CnmrIK2V3dl3nUcd6SzOGDd2Sgr0uXsLa2lZI+z9sTENr9L2G6vp2MeCG4g3HT1o824/n5Qux/FGSUsRqoGz2xvRrfevWn2wo61ZuLcQ9nUoRy+ZKj/Kx7EFBtlpRTj+GqNWmfHMfwyh7B2kxmTRL6dTscjuJAQB7bzwCo3OgNOiTfuDRMDwmlyOlZrquofkA4oerAfNuy+Gb2lylnPh3ThcvgK2x/XOvQnWtPXvSemyrUyD1Zq7Rnlppnw9u1xS5TuoJzXFDKohTqRE0ePX6BbYwozkOP/b72oPn7AXMqHJMjIkZQD8fNXQ9uMw==',
        'x-model': 'iPhone 6',
        'Connection': 'keep-alive',
        'x-locale': 'zh-Hans-CN',
        'x-version-code': '30961',
        'x-is-guest': 'Y',
        'x-version-name': '7.8.1',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZmRiMGViNDkwZTEzYjQ4YjQwODYyMGYiLCJ1c2VybmFtZSI6IuiwpuWSjOeahOW-iOS5hSIsIl92IjoiMSIsIl9lZCI6IlUrN2ZiRlU4SVNMUE5RUk9pVlBvS3h2djViQlJmbWJCRnp0TzZvWk1JWVJpSmhmUjBSWVkzMEIrRzVnT21DMFAiLCJnZW5kZXIiOiJNIiwiZGV2aWNlSWQiOiIiLCJpc3MiOiJodHRwczovL3d3dy5nb3Rva2VlcC5jb20vIiwiZXhwIjoxNjUyNzAzMjAwLCJpYXQiOjE2MjkzNzUyMDB9.B_QlE0Vd8-7r3-c0Y-UFbsYSVUL8HTGlIYiQZVi1AZY',
        'x-flutter-plugin-version': '0.9.0',
        'x-user-id': '5fdb0eb490e13b48b408620f',
        'x-carrier': '0',
        'Accept': '*/*',
        'Accept-Encoding': 'br, gzip, deflate',
        'x-connection-type': '2',
        'x-manufacturer': 'Apple',
        'x-screen-height': '667',
        'x-app-platform': 'keepapp'
    }
    headers=dict(headers1,**headers2)
    params={
        'feedType':'sports',
        'limit':6,
        'needCommentInfo':0,
        'needFavoriteInfo':1,
        'needFellowshipInfo':1,
        'needLikeInfo':1,
        'needRelationInfo':1,
        'sort':'byTime',
        
        'lastId':lastId,  
        'sessionId':'5fdb0eb490e13b48b408620f|1629375718032'
    }
    while True:
        try:
            response=requests.get(url=api,params=params,headers=headers,proxies=proxies,verify=False,timeout=5)
            break
        except requests.exceptions.ProxyError:
            print('ProxyError')
            continue
        except requests.exceptions.ConnectTimeout:
            print('ConnectTimeout')
            continue
        except requests.exceptions.ReadTimeout:
            print('ReadTimeout')
            continue
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
            continue
        except requests.exceptions.ChunkedEncodingError:
            print('ChunkedEncodingError')
            continue
    json=response.json()
    lastId=json['data']['lastId'].replace('entry','')
    item_list=json['data']['items']
    print(lastId)
    for item in item_list:
        # pprint(item)
        author_id=item['payload']['author_id']
        item['_id']=author_id

        try:
            collection.insert_one(item)  # 插入数据 insert_one插入一个对象 insert_many插入多个对象
        except pymongo.errors.DuplicateKeyError:
            pass



def get_info(result):
    userId=result['_id']
    if userId in id_list:
        return
    while True:
        api='https://api.gotokeep.com/social-user/v1/people/home'
        headers2={
            'Host': 'api.gotokeep.com',
            'x-model-raw': 'iPhone7,2',
            'x-screen-width': '375',
            'User-Agent': 'Keep/7.8.1 (iPhone; iOS 12.5.2; Scale/2.00)',
            'x-is-new-device': 'true',
            'x-timestamp': '1629433733502',
            'x-session-id': '1629461989',
            'x-bundleId': 'com.gotokeep.keep',
            'x-os': 'iOS',
            'x-keep-timezone': 'Asia/Shanghai',
            'x-device-id': 'b9e9e4a8814d43c58f68bd9cc4b8e4407e47b8fa',
            'x-os-version': '12.5.2',
            'x-channel': 'Apple Store',
            'x-ads': 'DtkeXyV6Gah1gVU2VLjQVt1YNvIoD7cT912+jWjEPcWxKimCYfqb9us+phX86ZO2MJ+d2jpZ3gJWudtchF+j6Z3oX0XZfKp1a0RHUggZuhCS+ZzGi19kmjU1Fw5GHb1+5G+gbWRV0pN53Ms8clIKwXPFF6CnmrIK2V3dl3nUcd6SzOGDd2Sgr0uXsLa2lZI+z9sTENr9L2G6vp2MeCG4g3HT1o824/n5Qux/FGSUsRqoGz2xvRrfevWn2wo61ZuLcQ9nUoRy+ZKj/Kx7EFBtlpRTj+GqNWmfHMfwyh7B2kxmTRL6dTscjuJAQB7bzwCo3OgNOiTfuDRMDwmlyOlZrquofkA4oerAfNuy+Gb2lylnPh3ThcvgK2x/XOvQnWtPXvSemyrUyD1Zq7Rnlppnw9u1xS5TuoJzXFDKohTqRE0ePX6BbYwozkOP/b72oPn7AXMqHJMjIkZQD8fNXQ9uMw==',
            'x-model': 'iPhone 6',
            'Connection': 'keep-alive',
            'x-locale': 'zh-Hans-CN',
            'x-version-code': '30961',
            'x-is-guest': 'Y',
            'x-version-name': '7.8.1',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZmRiMGViNDkwZTEzYjQ4YjQwODYyMGYiLCJ1c2VybmFtZSI6IuiwpuWSjOeahOW-iOS5hSIsIl92IjoiMSIsIl9lZCI6IlUrN2ZiRlU4SVNMUE5RUk9pVlBvS3h2djViQlJmbWJCRnp0TzZvWk1JWVJpSmhmUjBSWVkzMEIrRzVnT21DMFAiLCJnZW5kZXIiOiJNIiwiZGV2aWNlSWQiOiIiLCJpc3MiOiJodHRwczovL3d3dy5nb3Rva2VlcC5jb20vIiwiZXhwIjoxNjUyOTY3NDMxLCJpYXQiOjE2Mjk2Mzk0MzF9.rK6neBMqBj9e7b20iHAbGBNz8fyMRfjBXVSAODXm-uU',
            'x-flutter-plugin-version': '0.9.0',
            'x-user-id': '5fdb0eb490e13b48b408620f',
            'x-carrier': '0',
            'Accept': '*/*',
            'Accept-Encoding': 'br, gzip, deflate',
            'x-connection-type': '2',
            'x-manufacturer': 'Apple',
            'x-screen-height': '667',
            'x-app-platform': 'keepapp'
        }
        headers=dict(headers1,**headers2)
        params={
            'userId':userId
        }
        while True:
            try:
                response=requests.get(url=api,headers=headers,params=params,proxies=proxies,verify=False,timeout=5)
                break
            except requests.exceptions.ProxyError:
                print('ProxyError')
                continue
            except requests.exceptions.ConnectTimeout:
                print('ConnectTimeout')
                continue
            except requests.exceptions.ReadTimeout:
                print('ReadTimeout')
                continue
            except requests.exceptions.ConnectionError:
                print('ConnectionError')
                continue
            except requests.exceptions.ChunkedEncodingError:
                print('ChunkedEncodingError')
                continue
        json=response.json()
        # pprint(json)
        result['home']=json

        api='https://api.gotokeep.com/social-user/v1/record'
        while True:
            try:
                response=requests.get(url=api,headers=headers,params=params,proxies=proxies,verify=False,timeout=5)
                break
            except requests.exceptions.ProxyError:
                print('ProxyError')
                continue
            except requests.exceptions.ConnectTimeout:
                print('ConnectTimeout')
                continue
            except requests.exceptions.ReadTimeout:
                print('ReadTimeout')
                continue
            except requests.exceptions.ConnectionError:
                print('ConnectionError')
                continue
            except requests.exceptions.ChunkedEncodingError:
                print('ChunkedEncodingError')
                continue
        json=response.json()
        # pprint(json)
        result['record']=json
        home=result['home']
        record=result['record']
        try:
            if home['text']=='操作太快了，休息一下吧' or home['text']=='账号出了点问题，请重新登录':
                # time.sleep(1)
                print('home',home['text'])
                pprint(home)
                continue
        except KeyError:
            pprint(home)
            continue
        try:
            if record['text']=='操作太快了，休息一下吧' or record['text']=='账号出了点问题，请重新登录':
                # time.sleep(1)
                pprint(record)
                print('record',record['text'])
                continue
        except KeyError:
            pprint(record)
            continue
            # time.sleep(100000)
        break

    try:
        collection_new.insert_one(result)  # 插入数据 insert_one插入一个对象 insert_many插入多个对象
    except pymongo.errors.DuplicateKeyError:
        pass
    time.sleep(2)
    

### 详细信息采集

results=collection.find()
results2=collection_new.find()
id_list=[]
for result in results2:
    id_list.append(result['_id'])

print(id_list)

index=2235
for result in results[index:]:
    print('*'*80)
    print(index)
    index+=1
    # pprint(result)
    get_info(result=result)
    # break




### 信息提取整理
results=collection_new.find()
all_list=[]
row_index=0
for result in results:
    print(row_index)
    row_index+=1
    # pprint(result)
    home=result['home']
    if home['text']=='操作太快了，休息一下吧' or home['text']=='账号出了点问题，请重新登录' or home.get('msg','')=='Concurrent number exceeds limit':
        collection_new.delete_one(result)
        continue

    try:
        userBasicInfo=home["data"]["headInfo"]["userBasicInfo"]
    except TypeError:
        pprint('home',home)
        collection_new.delete_one(result)
        continue
        

    username=userBasicInfo.get('username','')
    gender=userBasicInfo.get('gender','')
    province=userBasicInfo['location']['province']
    if province==None:
        province=''
    memberStatus=userBasicInfo.get('memberStatus','')

    userSocialStaticsInfo=home["data"]["headInfo"]["userSocialStaticsInfo"]
    totalEntries=userSocialStaticsInfo['totalEntries']
    follow=userSocialStaticsInfo['follow']
    followed=userSocialStaticsInfo['followed']
    liked=userSocialStaticsInfo['liked']

    try:
        completeCount=home["data"]["headInfo"]['creatorStatsInfo']['completeCount']
    except TypeError:
        continue
    try:
        verifyDesc=home["data"]["headInfo"]['userVerifyInfo']['verifyDesc']
    except TypeError:
        verifyDesc=''

    achievementBadgeCount=home["data"]["headInfo"]['userAchievementInfo']["achievementBadgeCount"]
    levelInfos=home["data"]["headInfo"]['userAchievementInfo']["levelInfos"]
    level=''
    training=''
    running=''
    yoga=''
    cycling=''
    hiking=''


    for le in levelInfos:
        name=le['name']
        if name=='总等级':
            level=le['level']
        if name=='健身':
            training=le['duration']
        if name=='跑步':
            running=le['duration']
        if name=='瑜伽':
            yoga=le['duration']
        if name=='骑行':
            cycling=le['duration']
        if name=='行走':
            hiking=le['duration']
        # print(le)
    

    record=result['record']
    if record['text']=='操作太快了，休息一下吧' or record['text']=='账号出了点问题，请重新登录' or record.get('msg','')=='Concurrent number exceeds limit':
        collection_new.delete_one(result)
        continue
    userSportSummary=record['data']['userSportSummary']
    if userSportSummary==None:
        minutesDuration=''
        currMonthMinutesDuration=''
        joinTime=''
    else:
        minutesDuration=userSportSummary['minutesDuration']
        currMonthMinutesDuration=userSportSummary['currMonthMinutesDuration']
        joinTime=userSportSummary['joinTime']
        timeArray = time.localtime(joinTime)
        # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        joinTime= time.strftime("%Y-%m-%d", timeArray)
    
    info=[username,gender,province,memberStatus,totalEntries,follow,followed,liked,completeCount,verifyDesc,achievementBadgeCount,level,minutesDuration,currMonthMinutesDuration,joinTime,training,running,yoga,cycling,hiking]
    all_list.append(info)
    print(info)
    # pprint(home)
    print('*'*80)
    # pprint(record)
    # break
columns=['username','gender','province','memberStatus','totalEntries','follow','followed','liked','completeCount','verifyDesc','achievementBadgeCount','level','minutesDuration','currMonthMinutesDuration','joinTime','training','running','yoga','cycling','hiking']
df=pd.DataFrame(data=all_list,columns=columns)
df.to_excel('E:\jiedan\Atongyongjiedan\info.xlsx',index=False)





