from PIL import Image
import os
import math

proDir = os.path.split(os.path.abspath(__file__))[0]

# 合并所有好友头像
# path为存储头像图像的文件夹相对于当前路径的相对路径，这里应该为'images/'
def merge_images():
    print("Merging head images......")

    # 设置每个图片需要缩放到的大小
    photo_width = 200
    photo_height = 200

    # 保存所有本地图片的绝对地址
    photo_list = []
    # 头像图片文件夹的绝对路径
    dirName = os.path.join(proDir, 'image')

    # os.walk用来遍历某一个文件夹下的所有文件夹和文件，递归便利，os是python自带库
    # 具体参数用法参考python手册
    for root, dirs, files in os.walk(dirName):
        for file in files:
            # 遍历所有文件，如果文件名包含jpg则获取该文件绝对路径添加到photo_list
            # os.path.join(root, file)拼接为这个文件的绝对路径
            if "jpg" in file and os.path.getsize(os.path.join(root, file)) > 0:
                photo_list.append(os.path.join(root, file))

    pic_num = len(photo_list)
    # 合并图片的列数
    line_max = int(math.sqrt(pic_num))
    # 合并图片的行数
    row_max = int(math.sqrt(pic_num))
    print(line_max, row_max, pic_num)

    # 如果好友太多行数大于20行则限制为20行
    if line_max > 20:
        line_max = 20
        row_max = 20

    num = 0
    # 需要合并的图片总数
    pic_max = line_max * row_max

    # 新建底图，长款为行数*200px,列数*200px
    toImage = Image.new('RGBA', (photo_width * line_max, photo_height * row_max))

    # 循环粘贴每一个头像图片
    for i in range(0, row_max):
        for j in range(0, line_max):
            # 读取对应的头像图片
            pic_fole_head = Image.open(photo_list[num])
            # 把图片伸缩到设置的大小（200px*200px）
            tmppic = pic_fole_head.resize((photo_width, photo_height))
            # 计算图片粘贴的位置
            loc = (int(j % row_max * photo_width), int(i % row_max * photo_height))
            # 把头像图片粘贴到底图对应位置
            toImage.paste(tmppic, loc)
            num = num + 1
            if num >= len(photo_list):
                break
        if num >= pic_max:
            break
    print(toImage.size)
    # 保存图片
    toImage.save('merged.png')

merge_images()