# -*- coding: utf-8 -*-
##########################
####    图片处理相关   ####
##########################

import win32gui
import shutil
import io
import auto
import sys
import os
import time
from skimage.metrics import structural_similarity
import cv2 as cv
from PIL import Image
from PyQt5.QtWidgets import QApplication
import constant as c
import util
import numpy as np
from matplotlib import pyplot as plt
#######
#######


hwnd_title = dict()


########
########

def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

def dir_check():
    util.log_title('文件夹检查')
    dir_List = [
        c.img_dir_path,c.flag_dir_path,c.sub_dir_path,c.data_dir_path,
        c.train_dir,c.front_img_dir,c.others_img_dir,c.new_front_img_dir,c.new_others_img_dir
        ];
    for path in dir_List:
        dir_create(path)
        print(f'\t{path}\t\tok')
    return True

def dir_create(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'文件夹创建 -> {path}')

def time_str():
    localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #系统当前时间年份
    year=time.strftime('%Y',time.localtime(time.time()))
    #月份
    month=time.strftime('%m',time.localtime(time.time()))
    #日期
    day=time.strftime('%d',time.localtime(time.time()))
    #具体时间 小时分钟毫秒
    mdhms=time.strftime('%m%d%H%M%S',time.localtime(time.time()))
    return f'{year}_{month}_{day}_{mdhms}'

def shot():
    # util.log_title('截图')
    win32gui.EnumWindows(get_all_hwnd, 0)
    gbf_title = ''
    for h,t in hwnd_title.items():
        # print(h, t)
        if t.startswith('Granblue Fantasy'):
            gbf_title = t
            # print(gbf_title)
            hwnd = win32gui.FindWindow(None, gbf_title)
            app = QApplication(sys.argv)
            desktop_id = app.desktop().winId()
            screen = QApplication.primaryScreen()
            img_desk = screen.grabWindow(desktop_id).toImage()
            img_sc = screen.grabWindow(hwnd).toImage()
            img_desk.save(c.img_desktop_path)
            img_sc.save(c.img_sc_path)
            # print(f'img_desktop save to -> {os.path.abspath(c.img_desktop_path)}')
            # print(f'img_gbf save to -> {os.path.abspath(c.img_sc_path)}')
    if gbf_title == '':
        print('gbf not start')
        return False
    return True

#### 图片检查
def image_check(img_path,size):
    util.log_title('截图检查')
    with Image.open(img_path) as img:
        if img.size[1] == size[1]:
            print(f'\t\tsize={size}\t\tok')
            return True
    print('Imgae Size Error')
    return False

#### 裁剪
def crop(source_path,target_path,shape):
    with Image.open(source_path) as img:

        fighting_flag_img = img.crop(shape)
        fighting_flag_img.save(target_path)
        return True

## 相似性判断
def compare_image(path_image1, path_image2):
    imageA = cv.imread(path_image1)
    imageB = cv.imread(path_image2)
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)

    (score, diff) = structural_similarity(grayA, grayB, full=True)
    # print("SSIM: {}".format(score))
    return score


def acrop():
    crop(c.img_sc_path,c.main_img_path,c.main_shape)
    crop(c.img_sc_path,c.raid_img_path,c.raid_shape)
    crop(c.img_sc_path,c.batload_img_path,c.batload_shape)
    crop(c.img_sc_path,c.error_img_path,c.error_shape)
    crop(c.img_sc_path,c.resload_img_path,c.resload_shape)
    crop(c.img_sc_path,c.battle_img_path,c.battle_shape)
    crop(c.img_sc_path,c.fa_img_path,c.fa_shape)
    crop(c.img_sc_path,c.result_img_path,c.result_shape)
    crop(c.img_sc_path,c.stepload_img_path,c.stepload_shape)
    crop(c.img_sc_path,c.summon_img_path,c.summon_shape)
    crop(c.img_sc_path,c.readysum_img_path,c.readysum_shape)
    crop(c.img_sc_path,c.attack_img_path,c.attack_shape)
    crop(c.img_sc_path,c.again_img_path,c.again_shape)
    crop(c.img_sc_path,c.event_img_path,c.event_shape)

#### 是否在主页
def is_main():
    rate = compare_image(c.main_flag_img_path,c.main_img_path)
    if rate > 0.95:
        print('主页 状态:' + str(rate))
        return True
    else:
        print('非主页 状态:' + str(rate))
        return False

#### 是否在讨伐
def is_raid():
    rate = compare_image(c.raid_flag_img_path,c.raid_img_path)
    if rate > 0.95:
        print('讨伐 状态:' + str(rate))
        return True
    else:
        print('非讨伐 状态:' + str(rate))
        return False

#### 是否在batload
def is_batload():
    rate = compare_image(c.batload_flag_img_path,c.batload_img_path)
    if rate > 0.95:
        print('batload 状态:' + str(rate))
        return True
    else:
        print('非batload 状态:' + str(rate))
        return False

#### 是否在error
def is_error():
    rate = compare_image(c.error_flag_img_path,c.error_img_path)
    if rate > 0.95:
        print('error 状态:' + str(rate))
        return True
    else:
        print('非error 状态:' + str(rate))
        return False

#### 是否在resload
def is_resload():
    rate = compare_image(c.resload_flag_img_path,c.resload_img_path)
    if rate > 0.95:
        print('resload 状态:' + str(rate))
        return True
    else:
        print('非resload 状态:' + str(rate))
        return False

#### 是否在stepload
def is_stepload():
    rate = compare_image(c.stepload_flag_img_path,c.stepload_img_path)
    if rate > 0.95:
        print('stepload 状态:' + str(rate))
        return True
    else:
        print('非stepload 状态:' + str(rate))
        return False

#### 是否在event
def is_event():
    rate = compare_image(c.event_flag_img_path,c.event_img_path)
    if rate > 0.95:
        print('event 状态:' + str(rate))
        return True
    else:
        print('非event 状态:' + str(rate))
        return False

#### 是否在战斗
def is_battle():
    rate = compare_image(c.battle_flag_img_path,c.battle_img_path)
    if rate > 0.95:
        print('战斗 状态:' + str(rate))
        return True
    else:
        print('非战斗 状态:' + str(rate))
        return False

#### 是否在fa 1是2否0未知
def is_fa():
    rate1 = compare_image(c.fa_flag_1_img_path,c.fa_img_path)
    if rate1 > 0.95:
        print('未fa状态:' + str(rate1))
        return 2
    rate2 = compare_image(c.fa_flag_2_img_path,c.fa_img_path)
    if rate2 > 0.95:
        print('fa 状态:' + str(rate2) + ' ' + str(rate1))
        return 1
    return 0

#### 是否在攻击 1是2否0未知
def is_attack():
    rate1 = compare_image(c.attack_flag_1_img_path,c.attack_img_path)
    rate2 = compare_image(c.attack_flag_2_img_path,c.attack_img_path)
    if rate1 > 0.95:
        print('未attack状态:' + str(rate1))
        return 2
    
    if rate2 > 0.95:
        print('attack 状态:' + str(rate2) + ' ' + str(rate1))
        return 1
    return 0

#### 是否在result
def is_result():
    rate = compare_image(c.result_flag_img_path,c.result_img_path)
    if rate > 0.95:
        print('result 状态:' + str(rate))
        return True
    else:
        print('非result 状态:' + str(rate))
        return False

#### 是否在agrinresult
def is_again_result():
    rate = compare_image(c.again_flag_img_path,c.again_img_path)
    if rate > 0.95:
        print('again_result 状态:' + str(rate))
        return True
    else:
        print('非again_result 状态:' + str(rate))
        return False

#### 是否在summon
def is_summon():
    rate = compare_image(c.summon_flag_img_path,c.summon_img_path)
    if rate > 0.90:
        print('summon 状态:' + str(rate))
        return True
    else:
        print('非summon 状态:' + str(rate))
        return False

#### 是否在readysum
def is_readysum():
    rate = compare_image(c.readysum_flag_img_path,c.readysum_img_path)
    if rate > 0.95:
        print('readysum 状态:' + str(rate))
        return True
    else:
        print('非readysum 状态:' + str(rate))
        return False

def is_exp_window():
    explocation,expscore = template_match(c.exp_flag_img_path, c.img_sc_path)
    print('exp弹窗 打分', explocation, expscore)
    return expscore > 3

def is_honor_window():
    honorlocation,honorscore = template_match(c.honor_flag_img_path, c.img_sc_path)
    print('honor弹窗 打分', honorlocation, honorscore)
    return honorscore > 3

def is_nightmare_window():
    nightmarelocation,nightmarescore = template_match(c.nightmare_flag_img_path, c.img_sc_path)
    print('nightmare弹窗 打分', nightmarelocation, nightmarescore)
    return nightmarescore > 3

def is_halfhong_window():
    halfhonglocation,halfhongscore = template_match(c.halfhong_flag_img_path, c.img_sc_path)
    print('halfhong弹窗 打分', halfhonglocation, halfhongscore)
    return halfhongscore > 3

def is_halfhongrecover_window():
    halfhongrecoverlocation,halfhongrecoverscore = template_match(c.halfhongrecover_flag_img_path, c.img_sc_path)
    print('halfhongrecover弹窗 打分', halfhongrecoverlocation, halfhongrecoverscore)
    return halfhongrecoverscore > 3

def is_neterror_window():
    neterrorlocation,neterrorscore = template_match(c.neterror_flag_img_path, c.img_sc_path)
    print('neterror弹窗 打分', neterrorlocation, neterrorscore)
    return neterrorscore > 4

def is_trophy_window():
    trophylocation,trophyscore = template_match(c.trophy_flag_img_path, c.img_sc_path)
    print('trophy弹窗 打分', trophylocation, trophyscore)
    return trophyscore > 4

def is_validate():
    location,score = template_match(c.validate_flag_img_path, c.img_sc_path)
    okx, oky = find_xy(c.ok_flag_img_path)
    print('验证码 打分', location, score, okx, oky)
    return score > 4 and okx>0 and oky>0


# def is_scene(scene):
#     print(scene+"标识截图")
#     rate = 0
#     exec('crop(c.img_sc_path,c.{}_img_path,c.{}_shape)'.format(scene, scene))
#     exec('rate = compare_image(c.{}_flag_img_path,c.{}_img_path)'.format(scene, scene))
#     print(rate)
#     if rate > 0.95:
#         print(scene+"状态")
#         return True
#     else:
#         print("非"+scene+"状态")
#         return False


            

### 弹窗判断
# 是  切分出包含4人物大图  360 * 120
# 否  False 
def popup_sub_crop():
    util.log_title('弹窗判断')
    shape_dict = {} 
    for i in range(len(c.popup_flag_img_paths)):
        shape,score = template_match(c.popup_flag_img_paths[i],c.img_sc_path)
        shape_dict[shape] = (score,i)
    
    print(shape_dict)
    max_shape = max(shape_dict, key=shape_dict.get)
    score,i = shape_dict[max_shape]
    print(f'最大区域 {max_shape} 最终得分为 {score}' )
    if score >=3 :
        sub_shape = (
            max_shape[0]+c.popup_move_shapes[i][0],
            max_shape[1]+c.popup_move_shapes[i][1],
            max_shape[2]+c.popup_move_shapes[i][2],
            max_shape[3]+c.popup_move_shapes[i][3]
        )
        print(f'弹框区域  {sub_shape}')
        return crop(c.img_sc_path,c.popup_sub_img_path,sub_shape)
    print(f'没有弹框')
    return False

#### 匹配
def template_match(template_path,src_path):
    img = cv.imread(src_path,0)
    img2 = img.copy()
    template = cv.imread(template_path,0)
    w, h = template.shape[::-1]
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED','cv.TM_CCORR',
                'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    shape_dict = {}
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)  
        shape = (top_left[0],top_left[1],bottom_right[0],bottom_right[1])
        if shape_dict.get(shape) == None:
            shape_dict[shape] = 1;
        else:
            shape_dict[shape] = shape_dict[shape]+1        
        max_shape = max(shape_dict, key=shape_dict.get)
    return max_shape,shape_dict[max_shape]

### 根据index返回对应 图片在桌面的中心点
def find_xy_indesktop(template_path):
    util.log_title('坐标查找')
    shape,score = template_match(template_path,c.img_desktop_path)
    print(f'最高得分区域 {shape} 得分为 {score}')
    if score >= 3:
        x = (shape[2]+shape[0])//2
        y = (shape[3]+shape[1])//2
        print(f'中心点坐标为 {(x,y)}')
        return x,y
    else:
        print(f'所有区域得分均小于3，匹配失败')
        return 0,0
### 根据index返回对应 图片在游戏的中心点
def find_xy(template_path):
    util.log_title('坐标查找')
    shape,score = template_match(template_path,c.img_sc_path)
    print(f'最高得分区域 {shape} 得分为 {score}')
    if score >= 3:
        x = (shape[2]+shape[0])//2
        y = (shape[3]+shape[1])//2
        print(f'中心点坐标为 {(x,y)}')
        return x,y
    else:
        print(f'所有区域得分均小于3，匹配失败')
        return 0,0

#### 
def find_mouse_in_desktop():    
    img = cv.imread(c.img_desktop_path,0)
    img2 = img.copy()
    template = cv.imread(c.mouse_flag_img_path,0)
    w, h = template.shape[::-1]
    
    img = img2.copy()
    shape_list = []
    threshold = 0.85
    res = cv.matchTemplate(img,template,cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    x = 10000
    y = 10000
    for pt in zip(*loc[::-1]):
        top_left = pt
        bottom_right = (top_left[0] + w, top_left[1] + h)  
        shape = (top_left[0],top_left[1],bottom_right[0],bottom_right[1])
        shape_list.append(shape)
        new_x = (shape[2]+shape[0])//2
        if new_x < x :        
            x = new_x
            y = (shape[3]+shape[1])//2

    print(f'中心点坐标为 {(x,y)}')
    return x,y


### 切成4份 360 * 120   ->    4  *  (90*120)
def crop_4():
    util.log_title('弹窗人物切分')
    w = 90
    h = 120
    for i in range(len(c.crop_4_img_names)):
        shape = (w*i, 0, w*(i+1), h)
        crop(c.popup_sub_img_path,c.crop_4_img_paths[i],shape)


###  数据保存
def save_data_img(front_index):
    for i in range(len(c.crop_4_img_paths)):
        save_path = ''
        if i == front_index:
            save_path = os.path.join(c.new_front_img_dir,time_str()+'_'+str(i)+'.jpg')
        else:
            save_path = os.path.join(c.new_others_img_dir,time_str()+'_'+str(i)+'.jpg')
        shutil.copyfile(c.crop_4_img_paths[i],save_path)

### 
def move_new_to_train():
    move_file(c.new_front_img_dir,c.front_img_dir)
    move_file(c.new_others_img_dir,c.others_img_dir)

def move_file(src_path,target_path):
    file_list=os.listdir(src_path)
    if len(file_list)>0:
        for file in file_list:
            shutil.move(
                os.path.join(src_path,file),
                os.path.join(target_path,file)
                )   
    print(f'{src_path} -> {target_path} 完毕')
####################################
####################################


if __name__ == '__main__':
    dir_check()