#import sys
#sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import datetime
import random
import time

#login, password='89165775463','helloend111'
vk_session = vk_api.VkApi( token="54ef672458b301255e5da023c15ae9ace2e462b2b05817815527a45c7b8a0dfd6e1e90c04e604a32f60e4")


a=1

session_api = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def minutes():
    x=str(datetime.datetime.now())
    y=x[11:]
    minutes=y[3:5]
    seconds=y[6:]
    return int(minutes)
def seconds():
    x=str(datetime.datetime.now())
    y=x[11:]
    minutes=y[3:5]
    seconds=y[6:]
    return int(seconds[0:2])


while True:
    for event in longpoll.listen():
        if(minutes()%5==0):
            #vk_session.method('wall.post', {'owner_id': '-137821135','message': "#6server\n Продам Cadillac CTV. Гос: 5.57кк, цена договорная, в лс.","attachments": 'photo100172_166443618'})
            #post=364397
            #vk_session.method('wall.delete', {'owner_id': '-163915966','post_id': str(post)})
            mastmp=vk_session.method('wall.get', {'owner_id': '-163915966','count': 20})
            x=len(mastmp["items"])
            for i in range (0,x):
                if(str(mastmp["items"][i]['from_id'])=='414517334'):
                    print(mastmp["items"][i]['id'])
                    vk_session.method('wall.delete', {'owner_id': '-163915966','post_id': str(mastmp["items"][i]['id'])})
            mastmp2=vk_session.method('wall.get', {'owner_id': '-137821135','count': 20})
            y=len(mastmp2["items"])
            for i in range (0,y):
                if(str(mastmp2["items"][i]['from_id'])=='414517334'):
                    print(mastmp2["items"][i]['id'])
                    vk_session.method('wall.delete', {'owner_id': '-137821135','post_id': str(mastmp2["items"][i]['id'])})
            vk_session.method('wall.post', {'owner_id': '-163915966','message': "#2server⛔⛔⛔⛔⛔⛔⛔⛔⛔\nПродам дом в Горной! Гос: 900к!\nДоплата договорная, в лс.",'attachment':'photo-177844818_456239077'})
            #vk_session.method('wall.post', {'owner_id': '-137821135','message': "#1server\n Продам Subaru WRX на 108 тонере и ВАЗ 2107 на 108 тонере и старых темно-синих фарах. \nЦена договорная, в лс.\n#2server. Продам коттедж в Жуковском, второй от ЖТУ. Гос: 1.1кк, дп договорная, в лс.\n #6server.\nПродам BMW 750 I. Гос: 1.449кк, без номеров, новая! Цена в лс!"})
            time.sleep(60)
            #print("good!")
            #vk_session.method('wall.post', {'owner_id': '-163915966','message': "#1server\n Продам Subaru WRX на 108 тонере, которого сейчас уже нет, и старых темно-синих фарах. \nЦена договорная, в лс."})
            #vk_session.method('wall.post', {'owner_id': '-137821135','message': "#1server\n Продам Subaru WRX на 108 тонере, которого сейчас уже нет, и старых темно-синих фарах. \nЦена договорная, в лс."})
            
    if(minutes()%20==0):
        print("ne good!")
        #vk_session.method('wall.post', {'owner_id': '-163915966','message': "#6server\n Продам Mercedes E63 (ешку). Гос: 5.94кк, цена договорная, в лс.","attachments":'photo100172_166443618'})
        #vk_session.method('wall.post', {'owner_id': '-137821135','message': "#6server\n Продам Cadillac CTV. Гос: 5.57кк, цена договорная, в лс.","attachments": 'photo100172_166443618'})
        #time.sleep(60)
