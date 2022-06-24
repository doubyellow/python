# coding=utf-8
from PIL import Image, ImageFont, ImageDraw
import os


def CreateImg(text):
    # 文字大小
    fontSize = 50
    liens = text.split('\n')
    high = 18 * fontSize
    wight = 18 * fontSize
    # high = len(max(liens, key=len)) * (fontSize + 5) * 5
    # wight = len(liens) * (fontSize + 5) * 5
    center = ((high - len(max(liens, key=len)) * fontSize) / 2, (wight - len(liens) * fontSize) / 2)
    # 画布颜色
    im = Image.new("RGB", (high, wight), (0, 0, 0))
    dr = ImageDraw.Draw(im)
    # 字体样式
    font_path = os.path.join(os.path.dirname(__file__), "simkai.ttf")
    font = ImageFont.truetype(font=font_path, index=0, size=fontSize)
    # 文字颜色
    dr.text(center, text, font=font, fill="#FFFF00")
    # file = os.path.split(os.path.dirname(__file__))[0]
    file_name = text.replace('\n', '')
    save_file = os.path.join(r"C:\Users\ASUS\Pictures\Camera Roll", f"{file_name}.png")
    im.save(save_file)
    im.show()


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    # CreateImg('法人身份证')
    # CreateImg('个人征信授权书')
    # CreateImg('公司章程')
    # CreateImg('关于同意查询和报\n送信用信息的函')
    # CreateImg('关于同意查询和报送信\n用信息的函（电子签名）')
    # CreateImg('营业执照')
    # CreateImg('购销合同')
    CreateImg("手持身份证照片")
    # CreateImg('购销合同2')
