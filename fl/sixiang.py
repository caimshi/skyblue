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
import screen as sc
import random
import requests
from playsound import playsound
import flow

#######
#######


hwnd_title = dict()


########
########

if __name__ == '__main__':
    dir_check()

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

def dealValidate():
    ## 发送验证码警告给微信
    location,score = sc.template_match(c.validate_flag_img_path, c.img_sc_path)
    sc.crop(c.img_sc_path, c.valiall_img_path, location)
    captchalocation,captchascore = sc.template_match(c.captcha_flag_img_path, c.valiall_img_path)
    print(captchalocation,captchascore)
    dt = time.strftime("%Y%m%d%H%M%S", time.localtime()) 
    captchapath = os.path.join(c.captcha_dir_path, dt +".jpg")
    sc.crop(c.valiall_img_path, captchapath, captchalocation)
    send("gbfvalidate")
    playsound("alert.mp3")
    exit()

def send(str):
    requests.get('https://sctapi.ftqq.com/SCT21935TDNmguH9AuQl97S4cQJUdhyP0.send?title=' + str)

def goback():
    auto.move_to_click(28, 59)



# 全局控制变量
lastState = ''
lastTime = 0
def setState(state):
    global lastState
    global lastTime
    if lastState == state:
        lastTime += 1
    else:
        lastState = state
        lastTime = 0
    print('当前状态为' + state + ':第' +str(lastTime) + '次')
## 四象任务
def tasksixiang():
    global lastTime
    global lastState
    util.log_h1_start(f'开始')
    start_time = time.time()
    battle_time = 0
    while(True):
        time.sleep(0.5)
        if sc.shot() and sc.image_check(c.img_sc_path,c.screen_size):                                                          ## 截图
            sc.acrop() ## 分截图
            if sc.is_error(): ## 如果出现错误页面 直接刷新
                auto.refresh()
                continue
            if sc.is_validate(): ## 出现验证码 最高优先级事件 退出并报警
                dealValidate()
                continue
            if lastTime > 8:
                auto.refresh()
                lastTime = 0
                continue
            if sc.is_summon():
                setState('summon')
                flow.selectSummon('titan')
                # time.sleep(0.1)
                auto.toclick(419,759)
                continue
            if sc.is_readysum():
                setState('readysum')
                auto.toclick(419,759)
                continue
            if sc.is_resume():
                setState('resume')
                auto.toclick(412,623)
                continue
            if sc.is_quest() or sc.is_specialquest():
                setState('is_quest')
                flow.toTag(2)
                continue
            if sc.is_batload():
                setState('batload')
                continue
            if sc.is_stepload():
                setState('stepload')
                continue
            if sc.is_resload():
                setState('resload')
                # auto.toclick(112,532)
                continue
            if sc.is_friend():
                auto.toclick(196,768)
                continue
            if sc.is_battle():
                if sc.is_fa() == 2:
                    auto.toclick(112,532)
                if sc.is_fa() == 1:
                    isattack =  sc.is_attack()
                    if isattack == 0:
                        auto.refresh()
                        continue
                    if isattack == 1:
                        setState('attack')
                        continue
                    time.sleep(1.5)
                    auto.toclick(433,502)
                    continue
                continue
                
            exupx, exupy = sc.find_xy(c.exup_flag_img_path)
            if exupx>0 and exupy>0:
                print('ex升级 状态', exupx, exupy)
                auto.toclick(exupx,exupy)
                setState('exup')
                continue
            if sc.is_result():
                # flow.toTag(2)
                # continue
                setState('result')
                # 可能会出现正在加载按钮的情况 这种情况等待
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx == 0 and oky == 0:
                    setState('resulthalf')
                    continue
                if sc.is_again_result():
                    print('继续结算页 状态')
                    auto.toclick(200,557)
                else:
                    flow.toTag(2)
                continue
            if sc.is_halfhong_window():
                okx, oky = sc.find_xy(c.halfhong2_flag_img_path)
                if okx>0 and oky>0:
                    print('小红弹窗 状态', okx, oky)
                    oky = oky + 100
                    auto.toclick(okx, oky)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky + 400)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky + 55)
                    setState('halfhong')
                    continue
            if sc.is_halfhongrecover_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('吃完小红弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_trophy_window():
                okx, oky = sc.find_xy(c.closebutton_flag_img_path)
                if okx>0 and oky>0:
                    print('获得成就弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('close')
                    continue
            # 出现特殊星本逻辑和普通战货不一样 战斗逻辑不同
            if sc.is_extreme_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    time.sleep(2)
                    tasksixiangsp()
                    continue
            if sc.is_exp_window() or sc.is_honor_window() or sc.is_sixiang_window()  or sc.is_neterror_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_event():
                flow.toTag(2)

            # 走到这里就是未识别的场景 直接exit
            setState('error')
            print('此场景未识别')
            if lastState == 'error' and lastTime > 3:
                playsound('alert.mp3')
                exit()
            continue
        return False
    end_time = time.time()
    cost_time = end_time - start_time
    util.log_h1_end(f'结束 耗时 %.3f' % cost_time)
    time.sleep(1)



## 星本任务中的特殊星本处理
def tasksixiangsp():
    global lastTime
    global lastState
    util.log_h1_start(f'开始')
    start_time = time.time()
    battle_time = 0
    while(True):
        time.sleep(0.5)
        if sc.shot() and sc.image_check(c.img_sc_path,c.screen_size):                                                          ## 截图
            sc.acrop() ## 分截图
            if sc.is_error(): ## 如果出现错误页面 直接刷新
                auto.refresh()
                continue
            if sc.is_validate(): ## 出现验证码 最高优先级事件 退出并报警
                dealValidate()
                continue
            if lastTime > 8:
                auto.refresh()
                lastTime = 0
                continue
            if sc.is_summon():
                setState('summon')
                flow.selectSummon('titan')
                continue
            if sc.is_readysum():
                setState('readysum')
                auto.toclick(419,759)
                continue
            if sc.is_batload():
                setState('batload')
                continue
            if sc.is_resload():
                setState('resload')
                # auto.toclick(112,532)
                continue
            if sc.is_battle():
                if sc.is_fa() == 2:
                    auto.toclick(112,532)
                if sc.is_fa() == 1:
                    isattack =  sc.is_attack()
                    if isattack == 0:
                        auto.refresh()
                        continue
                    if isattack == 1:
                        setState('attack')
                        continue
                continue
            exupx, exupy = sc.find_xy(c.exup_flag_img_path)
            if exupx>0 and exupy>0:
                print('ex升级 状态', exupx, exupy)
                auto.toclick(exupx,exupy)
                setState('exup')
                continue
            if sc.is_result():
                setState('result')
                return
            if sc.is_halfhong_window():
                okx, oky = sc.find_xy(c.halfhong2_flag_img_path)
                if okx>0 and oky>0:
                    print('小红弹窗 状态', okx, oky)
                    oky = oky + 100
                    auto.toclick(okx, oky)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky + 400)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky + 55)
                    setState('halfhong')
                    continue
            if sc.is_halfhongrecover_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('吃完小红弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_trophy_window():
                okx, oky = sc.find_xy(c.closebutton_flag_img_path)
                if okx>0 and oky>0:
                    print('获得成就弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('close')
                    continue
            if sc.is_exp_window() or sc.is_honor_window() or sc.is_nightmare_window() or sc.is_neterror_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_event():
                flow.toTag(2)

            # 走到这里就是未识别的场景 直接exit
            setState('error')
            print('此场景未识别')
            if lastState == 'error' and lastTime > 3:
                exit()
            continue
        return False
    end_time = time.time()
    cost_time = end_time - start_time
    util.log_h1_end(f'结束 耗时 %.3f' % cost_time)
    time.sleep(1)


