import requests
import telebot
import time
import threading
import os
bot=telebot.TeleBot("Токен тг бота")
token="Токен дискорда"
group_id=Айди группы тг
admin_id=Айди пользователя тг

id=["Айди румы из дискорда"]

def get_messages(token:str,chatid:str):
    headers = {
        "authorization": token
    }
    a=requests.get(f"https://discord.com/api/v9/channels/{chatid}/messages?limit=50", headers=headers)
    return a.json()
def check(ch_id):
    sended=[]
    while 1:
        msg=get_messages(token,ch_id)[0]["attachments"]
        if msg:
            for i in msg:
                if i["url"] not in sended:
                    filename=i["filename"]
                    response=requests.get(i["url"])
                    try:
                        if response.status_code==200:
                            with open(filename,'wb') as imgfile:
                                imgfile.write(response.content)
                        bot.send_photo(group_id, photo=open(filename, 'rb'))
                    except:
                        bot.send_message(admin_id, f"Возникла ошибка при отправке или загрузки файла {filename}")
                        continue
                    try:
                        os.remove(filename)
                    except:
                        bot.send_message(admin_id, f"Возникла ошибка при удалении файла {filename}")
                        continue
                    sended.append(i["url"])
        time.sleep(5)
for i in id:
    threading.Thread(target=check, args=(i,)).start()