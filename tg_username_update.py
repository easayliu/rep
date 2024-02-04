#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Updated:
#  1. 使用async来update lastname，更加稳定
#  2. 增加emoji clock，让时间显示更加有趣味

import time
import os
import sys
import logging
import asyncio
import random
from time import strftime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from emoji import emojize


dizzy = emojize(":dizzy:")
cake = emojize(":cake:")
all_time_emoji_name = ["clock12", "clock1230", "clock1", "clock130", "clock2", "clock230", "clock3", "clock330", "clock4", "clock430", "clock5", "clock530", "clock6", "clock630", "clock7", "clock730", "clock8", "clock830", "clock9", "clock930", "clock10", "clock1030", "clock11", "clock1130"]
time_emoji_symb = [emojize(":%s:" %s) for s in all_time_emoji_name]

api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file+'.session'):
    api_id = input('api_id: ')
    api_hash = input('api_hash: ')
else:
    api_id = 123456
    api_hash = '00000000000000000000000000000000'

client1 = TelegramClient(api_auth_file, api_id, api_hash)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def change_name_auto():
    # Set time zone to UTC+8
    # ln -sf /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
    # https://stackoverflow.com/questions/4788533/python-strftime-gmtime-not-respecting-timezone

    print('will change name')

    while True:
        try:
            time_cur = strftime("%H:%M:%S:%p:%a", time.localtime())
            hour, minu, seco, p, abbwn = time_cur.split(':')
            emojis = ["😀", "😄", "😊", "😎", "😍", "🤩", "🥳", "🥰"]
            random_emoji = random.choice(emojis)            
            if seco=='00' or seco=='30':
                shift = 0
                mult = 1
                if int(minu)>30: shift=1
                # print((int(hour)%12)*2+shift)
                # hour symbols
                hsym = time_emoji_symb[(int(hour)%12)*2+shift]
                # await client1.send_message('me', hsym)
                for_fun = random.random() 
                if for_fun < 0.10:
                    last_name = 'Easay %s:%s %s %s %s' % (hour, minu, p, abbwn, random_emoji)
                elif for_fun < 0.30:
                    last_name = 'Easay %s:%s %s %s %s' % (hour, minu, p, abbwn, random_emoji)
                elif for_fun < 0.60:
                    last_name = 'Easay %s:%s %s %s %s' % (hour, minu, p, abbwn, random_emoji)
                elif for_fun < 0.90:
                    last_name = 'Easay %s:%s %s %s %s' % (hour, minu, p, abbwn, random_emoji)
                else:
                    last_name = 'Easay %s:%s %s %s %s' % (hour, minu, p, abbwn, random_emoji)
        
                await client1(UpdateProfileRequest(first_name=last_name))
                logger.info('Updated -> %s' % last_name)
        
        except KeyboardInterrupt:
            print('\nwill reset last name\n')
            await client1(UpdateProfileRequest(last_name=''))
            sys.exit()

        except Exception as e:
            print('%s: %s' % (type(e), e))

        await asyncio.sleep(1)


# main function
async def main(loop):

    await client1.start()

    # create new task
    print('creating task')
    task = loop.create_task(change_name_auto())
    await task
     
    print('It works.')
    await client1.run_until_disconnected()
    task.cancel()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))