# 图片校验，输出不合规格的图片名文件
from PIL import Image
import os
import csv
import pandas as pd

# 定义图片校验函数
def check_image(folder_path, question_type):
    invalid_images = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_path = os.path.join(root, file)
                image = Image.open(image_path)
                width, height = image.size
                size_in_mb = os.path.getsize(image_path) / (1024 * 1024)  # 文件大小换算成MB

                if question_type == '点选':
                    if not (100 <= width <= 992 and 100 <= height <= 718):
                        invalid_images.append(file)
                elif question_type == '填空':
                    if width > 2048 or height > 2048 or size_in_mb > 1:
                        invalid_images.append(file)
                elif question_type == '拖拽':
                    if not (width == 2000 and height == 1500):
                        invalid_images.append(file)

    return invalid_images

# 文件夹路径
point_folder = '点选'
drag_folder = '拖拽'
fill_folder = '填空'

# 分别对三个文件夹进行校验
point_invalid_images = check_image(point_folder, '点选')
drag_invalid_images = check_image(drag_folder, '拖拽')
fill_invalid_images = check_image(fill_folder, '填空')

# 保存不符合要求的图片名到txt文件中
with open('invalid_images.txt', 'w', encoding="utf-8") as f:
    for img in point_invalid_images + drag_invalid_images + fill_invalid_images:
        f.write(img + '\n')

# 保存不符合要求的图片名到csv文件中
with open('invalid_images.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Invalid Images'])
    for img in point_invalid_images + drag_invalid_images + fill_invalid_images:
        writer.writerow([img])

# 保存不符合要求的图片名到excel文件中
df = pd.DataFrame({'Invalid Images': point_invalid_images + drag_invalid_images + fill_invalid_images})
df.to_excel('invalid_images.xlsx', index=False)


# 添加提示信息--不要让窗口停下来
print("文件保存成功！按下 Enter 键退出程序...")
# 等待用户按下回车键
input()