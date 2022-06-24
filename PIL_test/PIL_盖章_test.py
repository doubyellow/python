# coding=utf-8
import os
import shutil
from PIL import Image


image_water = Image.open(r"/picture/jpeg.gif")
# 将印章图片转换为rgba值
rgba_water = image_water.convert("RGBA")
# 获取印章尺寸
image_water_x, image_water_y = rgba_water.size


# for root, dirs, files in os.walk(os.getcwd()):
# 获取需要加印的图片路径
png = []
for root, dirs, files in os.walk(r'/picture'):
    for file in files:
        fe = os.path.join(root, file)
        if fe.endswith("png"):
            png.append(fe)
if not os.path.exists(r"/png"):
    os.mkdir(r"/png")
else:
    print("存在文件夹")

# 加印后文件保存路径
new_path = os.path.join(r"/", "png")

# 读取文件
for i in png:
    png_obj = Image.open(i)
    # 获取尺寸
    png_obj_x, png_obj_y = png_obj.size
    # 重新设置图片长宽
    png_obj=png_obj.resize((1920, 927), resample=Image.ANTIALIAS)
    # 将目标图片转换为rgba值
    rgba_png = png_obj.convert("RGBA")
    # 获取尺寸
    rgba_png_obj_x, rgba_png_obj_y = rgba_png.size
    # print(rgba_png_obj_x, rgba_png_obj_y)
    # 缩放图片尺
    scale = 7
    watermark_scale = max(rgba_png_obj_x / (scale * image_water_x), rgba_png_obj_y / (scale * image_water_y))
    new_size = (int(image_water_x * watermark_scale), int(image_water_y * watermark_scale))
    rgba_water = rgba_water.resize(new_size, resample=Image.ANTIALIAS)

    # 印章与图片融合
    rgba_png.paste(rgba_water, (rgba_png_obj_x - image_water_x, rgba_png_obj_y - image_water_y))
    out = Image.composite(rgba_png, png_obj, rgba_png)
    # b = i.split(".png")[0] + "new" + ".png"
    b = os.path.join(new_path, i.split("\\")[-1])
    out = out.resize((png_obj_x, png_obj_y), resample=Image.ANTIALIAS)
    out.save(b)

    print("*" * 30)
    print(f"{i}完成盖章扫描")

    # if "new" in b:
    #     shutil.move(b, new_path)

# for root, dirs, files in os.walk(new_path):
#
#     print("*" * 30)
#     print(root, dirs, files)
#
#     for file in files:
#         old_file_name = os.path.join(root, file)
#
#         g = file.split("new")[0] + ".png"
#
#         new_file_name = os.path.join(root, g)
#
#         os.rename(old_file_name, new_file_name)
#
#         print("%s 完成创建" % (g))
