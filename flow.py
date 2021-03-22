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
    requests.get('https://sctapi.ftqq.com/SCT21935TDNmguH9AuQl97S4cQJUdhyP0.send?title=gbfvalidate')
    exit()

def goback():
    auto.move_to_click(28, 59)

def test():
    print()
    if sc.shot():                                                          ## 截图
        if sc.image_check(c.img_sc_path,c.screen_size):                    ## 检查截图大小
            sc.acrop()
            is_stepload()
            print(c.validate1_store_img_path)
            location,score = sc.template_match(c.validate_flag_img_path, c.validate1_store_img_path)
            sc.is_validate()
            print(location, score)
            dealValidate()
            exit()
            sc.is_attack()
            sc.is_error()
            sc.is_main()                                           
            sc.is_raid()
            sc.is_result()
            sc.is_battle()
            sc.is_batload()
            sc.is_resload()
            sc.is_summon()
            sc.is_readysum()
            sc.is_fa()
            sc.is_event()
            if sc.is_exp_window() or sc.is_honor_window() or sc.is_nightmare_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
            
            if sc.is_result():
                if sc.is_again_result():
                    print('继续结算页 状态')
                
                # againx, againy = sc.is_again_result(c.again_flag_img_path)
                # if againx>0 and againy>0:
                #     print('结算页继续 状态', againx, againy)
                #     auto.toclick(againx,againy)
                
            if sc.is_halfhong_window():
                okx, oky = sc.find_xy(c.halfhong2_flag_img_path)
                if okx>0 and oky>0:
                    print('小红弹窗 状态', okx, oky)
                    oky = oky + 100
                    auto.toclick(okx, oky)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky + 400)
                    time.sleep(0.5 + random.random()/10)
                    # auto.toclick(okx, oky + 55)
    
            location,score = sc.template_match(c.exup_flag_img_path, c.img_sc_path)
            print('ex升级 打分', score)
            if score > 3:
                print('ex升级 状态', score)
            
            location,score = sc.template_match(c.ok_flag_img_path, c.img_sc_path)
            print('弹窗 打分', score)
            if score > 3:
                print('弹窗 状态', score)
            return True
    return False

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


def selectSummon(sumname):
    if sumname == 'titan':
        titan2x, titan2y = sc.find_xy(c.titan2_flag_img_path)
        if titan2x>0 and titan2y>0:
            print('找到召唤石titan2', titan2x, titan2y)
            auto.toclick(titan2x,titan2y)
            return
        titanx, titany = sc.find_xy(c.titan_flag_img_path)
        if titanx>0 and titany>0:
            print('找到召唤石titan', titanx, titany)
            auto.toclick(titanx,titany)
            return
        shendunx, shenduny = sc.find_xy(c.shendun_flag_img_path)
        if shendunx>0 and shenduny>0:
            print('没有找到titan 找到召唤石shendun', shendunx, shenduny)
            auto.toclick(shendunx,shenduny)
            return
    auto.toclick(159,508)

def toTag():
    # 二号书签位
    # auto.toclick(242,90)
    # 一号书签位
    auto.toclick(106,90)

## 战货任务
def taskzhanhuo():
    global lastTime
    global lastState
    util.log_h1_start(f'开始')
    start_time = time.time()
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
                selectSummon('titan')
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
                    time.sleep(2)
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
                setState('result')
                # 可能会出现正在加载按钮的情况 这种情况等待
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx == 0 and oky == 0:
                    continue
                if sc.is_again_result():
                    print('继续结算页 状态')
                    auto.toclick(200,557)
                else:
                    toTag()
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
            if sc.is_exp_window() or sc.is_honor_window() or sc.is_nightmare_window()  or sc.is_neterror_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_event():
                toTag()

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
    

## 星本任务
def taskxingben():
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
                selectSummon('titan')
                continue
            if sc.is_readysum():
                setState('readysum')
                auto.toclick(419,759)
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
            if sc.is_battle():
                if sc.is_fa() == 2:
                    auto.toclick(112,532)
                # if sc.is_fa() == 1:
                isattack =  sc.is_attack()
                if isattack == 0:
                    if lastState != 'attack':
                        setState('attack')
                        time.sleep(1)
                        continue
                    goback()
                    setState('noattack')
                if isattack == 2:
                    auto.toclick(433,502)
                    setState('attack')
                if isattack == 1:
                    setState('attack')
                continue
                
            exupx, exupy = sc.find_xy(c.exup_flag_img_path)
            if exupx>0 and exupy>0:
                print('ex升级 状态', exupx, exupy)
                auto.toclick(exupx,exupy)
                setState('exup')
                continue
            if sc.is_result():
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
                    toTag()
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
            if sc.is_nightmare_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    time.sleep(2)
                    taskxingbensp()
                    continue
            if sc.is_exp_window() or sc.is_honor_window()  or sc.is_neterror_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_event():
                toTag()

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


## 星本任务中的特殊星本处理
def taskxingbensp():
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
                selectSummon('titan')
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
                toTag()

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


