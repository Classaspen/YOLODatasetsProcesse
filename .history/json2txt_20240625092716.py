import json
import os
 
name2id = {'sentry_B': 6}
 
 
def convert(img_size, x, y, w, h, box):

    x_ = x /1440
    w_ = w /1440
    y_ = y /1280
    h_ = h /1280
    
    box_ = (box[0]/1440, box[1]/1280, box[2]/1440, box[3]/1280, box[4]/1440, box[5]/1280, box[6]/1440, box[7]/1280)
    return (x_, y_, w_, h_, box_[0], box_[1], box_[2], box_[3], box_[4], box_[5], box_[6], box_[7])
 
def decode_json(json_floder_path, txt_outer_path, json_name):
 
    if not json_name.endswith(".json"):
        return
    txt_name = os.path.join(txt_outer_path, json_name[json_name.rfind("/")+1:-5] + '.txt')
 
    with open(txt_name, 'w') as f:
        json_path = os.path.join(json_floder_path, json_name)
        data = json.load(open(json_path, 'r', encoding='gb2312', errors='ignore'))
        img_w = data['imageWidth']
        img_h = data['imageHeight']
        isshape_type = data['shapes'][0]['shape_type']
        print(isshape_type)
        for i in data['shapes']:
            label_name = i['label']
            label_id = i['group_id']
            x1 = float(i['points'][0][0])
            x2 = float(i['points'][1][0])
            x3 = float(i['points'][2][0])
            x4 = float(i['points'][3][0])
            
            y1 = float(i['points'][0][1])
            y2 = float(i['points'][1][1])
            y3 = float(i['points'][2][1])
            y4 = float(i['points'][3][1])
            
            x = (x1+x2+x3+x4)/4
            y = (y1+y2+y3+y4)/4
            
            w = ((x4-x1)+(x3-x2))/2
            h = ((y2-y1)+(y3-y4))/2
            
            bb = (x1, y1, x2, y2, x3, y3, x4, y4)

            bbox = convert((1440, 1280),x, y, w, h, bb)

            try:
                f.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')
            except:
                pass
 
 
if __name__ == "__main__":
    json_floder_path = 'C:/Users/17007/Desktop/4号搞下来的/HERO/cam0_sentry_B/label/' #请将json文件的文件夹放在该文件夹下
    txt_outer_path = 'C:/Users/17007/Desktop/4号搞下来的/HERO/cam0_sentry_B/label_txt/' 
    json_names = os.listdir(json_floder_path)
    print("共有：{}个文件待转化".format(len(json_names)))
    flagcount = 0
    for json_name in json_names:
        decode_json(json_floder_path, txt_outer_path, json_name)  # 这里设置是否要缩放坐标，如果为False则不用缩放
        flagcount += 1
        print("还剩下{}个文件未转化".format(len(json_names) - flagcount))
    print('转化全部完毕')