import os

# 设置要读取文件的目录路径
directory = 'C:/Users/username/Desktop/HERO/cam0_sentry_B/labels/images/train'

# 创建一个 'train.txt' 文件
with open('train.txt', 'w') as f:
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 检查是否为 .txt 文件
        if filename.endswith('.png'):
            # 拼接文件的绝对路径
            file_path = os.path.join(directory, filename)
            # 将文件路径写入 'train.txt' 文件
            f.write(file_path + '\n')