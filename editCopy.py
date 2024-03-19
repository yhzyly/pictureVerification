# 根据不合格图片的txt记录文件查找更新的图片输出
# 新图片比老图片多个(1)的后缀
import os
import shutil

# 读取txt文件中的文件名列表
with open('invalid_images.txt', 'r' ,encoding="utf-8") as file:
    file_names = file.read().splitlines()

# 检查是否有(1)后缀的图片并保存到另一个文件夹
for file_name in file_names:
    file_path = os.path.join("点选", file_name)  # 添加pic/前缀
    if os.path.exists(file_path):
        base_name, extension = os.path.splitext(file_path)
        base_name_target, extension1 = os.path.splitext(file_name)
        print(base_name, extension)
        duplicate_file_name = f'{base_name}(1){extension}'
        if os.path.exists(duplicate_file_name):
            # 复制文件到另一个文件夹并以原文件名保存
            shutil.copy(duplicate_file_name, f'output/{base_name_target}{extension}')
            print(f'复制文件 {duplicate_file_name} 到 output 文件夹')

print('处理完成')