import os

# 设置输入和输出目录
input_dir = 'C:/Users/username/Desktop/HERO/cam0_sentry_B/label_txt/'
output_dir = 'C:/Users/username/Desktop/HERO/cam0_sentry_B/labels/'

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
x, y, w, h = 0.0, 0.0, 0.0, 0.0
# 遍历输入目录中的所有文件
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # 构建输入和输出路径
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # 读取文件内容
        with open(input_path, 'r') as file:
            lines = file.readlines()
        
        # 处理第一行
        # first_line = lines[0].strip().split()
        first_line = [float(x) for x in lines[0].strip().split()]
        x = round((float(first_line[1]) + float(first_line[3]) + float(first_line[5]) + float(first_line[7])) / 4, 6)
        y = round((float(first_line[2]) + float(first_line[4]) + float(first_line[6]) + float(first_line[8])) / 4, 6)
        w = round(((float(first_line[7]) - float(first_line[1])) + (float(first_line[5]) - float(first_line[3]))) / 2, 6)
        h = round(((float(first_line[4]) - float(first_line[2])) + (float(first_line[6]) - float(first_line[8]))) / 2, 6)
        # print(x,y,w,h)
        
        
        # if (float(first_line[0])==0):
        new_first_line = [str(13), *[format(x, '.6f') for x in [x, y, w, h]], *[str(x) for x in first_line[1:]]]
        lines[0] = ' '.join(new_first_line) + '\n'

        # 写入输出文件
        with open(output_path, 'w') as file:
            file.writelines(lines)

        print(f'Processed {filename}')
            
        # elif (float(first_line[0])==1):
        #     new_first_line = [str(13), *[format(x, '.6f') for x in [x, y, w, h]], *[str(x) for x in first_line[1:]]]
        #     lines[0] = ' '.join(new_first_line) + '\n'

        #     # 写入输出文件
        #     with open(output_path, 'w') as file:
        #         file.writelines(lines)

        #     print(f'Processed {filename}')
        
        
        # new_first_line = first_line[:1] + [x, y, w, h] + first_line[1:]
        # new_first_line = [str(x) for x in new_first_line]

        # lines[0] = ' '.join(new_first_line) + '\n'

        # # 写入输出文件
        # with open(output_path, 'w') as file:
        #     file.writelines(lines)

        # print(f'Processed {filename}')