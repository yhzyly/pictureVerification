# 输出不合格的图片
import os
import shutil

# 读取txt文件中的文件名列表
with open('invalid_images.txt', 'r' ,encoding="utf-8") as file:
    file_names = file.read().splitlines()

strlist = ["点选","拖拽","填空"]
for i in range(3):
    for file_name in file_names:
        file_path = os.path.join(strlist[i], file_name)  # 添加pic/前缀
        if os.path.exists(file_path):
            base_name, extension = os.path.splitext(file_path)
            base_name_target, extension1 = os.path.splitext(file_name)
            print(base_name, extension)

            # 复制文件到另一个文件夹并以原文件名保存
            shutil.copy(file_path, f'output/{base_name_target}{extension}')
            print(f'复制文件 {file_name} 到 output 文件夹')
    

print('处理完成')