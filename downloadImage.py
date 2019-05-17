# 导入itchat包
import itchat
import os

proDir = os.path.split(os.path.abspath(__file__))[0]
image_dir = os.path.join(proDir, 'image')


# 下载所有好友头像并存储
def download_images(frined_list):
    image_dir = os.path.join(proDir, 'image')
    # 计数器，保存每一个头像图片名为 num.jpg
    num = 1
    for friend in frined_list:
        # 赋值当前需要保存的图片的名称
        image_name = str(num) + '.jpg'
        num += 1
        # 使用itchat自带函数get_head_img获取好友头像图片的二进制流
        # friend["UserName"]为当前好友的唯一标识符
        img = itchat.get_head_img(userName=friend["UserName"])
        # 将图片二进制流img变量写入到images/文件夹下对应jpg文件
        with open(os.path.join(image_dir, image_name), 'wb') as file:
            file.write(img)

if __name__ == '__main__':
    # 自动登陆，会出现二维码，扫码确认后登陆微信
    itchat.auto_login()
    # get_friends获取所有好友信息函数，返回list存储到friends变量
    friends = itchat.get_friends(update=True)
    # 把好友信息传入下载图片函数
    download_images(friends)
