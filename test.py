# -*- coding: utf-8 -*-
##########################
####    程序入口      ####
##########################


import util
import constant as c
import time
import ocr
import os
import cv2 as cv
from PIL import Image

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


def crop(source_path,target_path,shape):
    with Image.open(source_path) as img:

        fighting_flag_img = img.crop(shape)
        fighting_flag_img.save(target_path)
        return True

### 测试
def run_test():
    util.log_h1_start(f'开始')
    start_time = time.time()
    realtest()
    end_time = time.time()
    cost_time = end_time - start_time
    util.log_h1_end(f'结束 耗时 %.3f' % cost_time)
    exit()

def realtest():
    print('test')
    location,score = template_match(c.validate_flag_img_path, c.validate1_store_img_path)
    print(location, score)
    if score > 4:
        captchalocation,captchascore = template_match(c.captcha_flag_img_path, c.validate1_store_img_path)
        print(captchalocation,captchascore)
        dt = time.strftime("%Y%m%d%H%M%S", time.localtime()) 
        captchapath = os.path.join(c.captcha_dir_path, dt +".jpg")
        crop(c.validate1_store_img_path, os.path.join(captchapath), captchalocation)
        print(captchapath)
        
        
        


run_test()