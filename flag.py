import itchat
# from itchat.content import *
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import time

flag = Image.open('China-Flag.png')  # flag dir here
flag_w, flag_h = flag.size
counter = 0


def process_img(filename):
    img = Image.open(filename)
    img_w, img_h = img.size
    re_flag = flag.resize((int(flag_w / flag_h * 0.25 * img_h), int(0.25 * img_h)),
                          Image.ANTIALIAS)
    img.paste(re_flag, (img_w - int(flag_w / flag_h * 0.25 * img_h),
        img_h - int(0.25 * img_h),
        img_w, img_h))
    img.save(f'process.png')
    return counter



@itchat.msg_register([itchat.content.PICTURE])
def get_img(msg):
    # friend = itchat.search_friends(userName=msg['FromUserName'])
    filename = msg['FileName']
    process_img(filename)
    itchat.send_image('process.png', msg['FromUserName'])
    time.sleep(2)




if __name__ == "__main__":
    itchat.auto_login(enableCmdQR=2)
