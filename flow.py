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

def paste():
    auto.click_right_button()
    auto.move_to_click(224,822)


def test():
    if sc.shot():                                                          ## 截图
        if sc.image_check(c.img_sc_path,c.screen_size):                    ## 检查截图大小
            sc.acrop()
            sc.is_die2()
            sc.is_battle2() 
            sc.is_battle()
            sc.is_raidcheck()
            sc.is_threeerror_window()
            exit()
            auto.toclick(704,204)
            auto.move_to_click(203,595)
            paste()
            exit()
            sc.is_summon()
            sc.is_pending_result()
            sc.is_battle2()
            sc.is_die()
            if sc.is_raid():
                if sc.is_nullep():
                    print('没有豆子了')
                    auto.toclick(398,174)
            if sc.is_douzirecover_window:
                print('豆子回复了')
            exit()
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
    if sumname == 'hades':
        hadesx, hadesy = sc.find_xy(c.hades_flag_img_path)
        if hadesx>0 and hadesy>0:
            print('找到召唤石hades', hadesx, hadesy)
            auto.toclick(hadesx,hadesy)
            return
        hades2x, hades2y = sc.find_xy(c.hades2_flag_img_path)
        if hades2x>0 and hades2y>0:
            print('找到召唤石hades2', hades2x, hades2y)
            auto.toclick(hades2x,hades2y)
            return
    if sumname == 'chuanmatmp':
        chuanmax, chuanmay = sc.find_xy(c.chuanma_flag_img_path)
        if chuanmax>0 and chuanmay>0:
            print('找到召唤石chuanma', chuanmax, chuanmay)
            auto.toclick(chuanmax,chuanmay)
            return
        dabax, dabay = sc.find_xy(c.daba_flag_img_path)
        if dabax>0 and dabay>0:
            print('找到召唤石daba', dabax, dabay)
            auto.toclick(dabax,dabay)
            return
        hadesx, hadesy = sc.find_xy(c.hades_flag_img_path)
        if hadesx>0 and hadesy>0:
            print('找到召唤石hades', hadesx, hadesy)
            auto.toclick(hadesx,hadesy)
            return
        hades2x, hades2y = sc.find_xy(c.hades2_flag_img_path)
        if hades2x>0 and hades2y>0:
            print('找到召唤石hades2', hades2x, hades2y)
            auto.toclick(hades2x,hades2y)
            return   
    if sumname == 'huanglong':
        huanglongx, huanglongy = sc.find_xy(c.huanglong_flag_img_path)
        if huanglongx>0 and huanglongy>0:
            print('找到召唤石huanglong', huanglongx, huanglongy)
            auto.toclick(huanglongx,huanglongy)
            return
    if sumname == 'fengma':
        fengmax, fengmay = sc.find_xy(c.fengma_flag_img_path)
        if fengmax>0 and fengmay>0:
            print('找到召唤石fengma', fengmax, fengmay)
            auto.toclick(fengmax,fengmay)
            return
    if sumname == 'qijie':
        qijiex, qijiey = sc.find_xy(c.qijie_flag_img_path)
        if qijiex>0 and qijiey>0:
            print('找到召唤石qijie', qijiex, qijiey)
            auto.toclick(qijiex,qijiey)
            return
        lux, luy = sc.find_xy(c.lu_flag_img_path)
        if lux>0 and luy>0:
            print('找到召唤石lu', lux, luy)
            auto.toclick(lux,luy)
            return
    if sumname == 'zhousi':
        zhousix, zhousiy = sc.find_xy(c.zhousi_flag_img_path)
        if zhousix>0 and zhousiy>0:
            print('找到召唤石zhousi', zhousix, zhousiy)
            auto.toclick(zhousix,zhousiy)
            return
    if sumname == 'gaoda':
        gaodax, gaoday = sc.find_xy(c.gaoda_flag_img_path)
        if gaodax>0 and gaoday>0:
            print('找到召唤石gaoda', gaodax, gaoday)
            auto.toclick(gaodax,gaoday)
            return
    if sumname == 'niqiu':
        niqiux, niqiuy = sc.find_xy(c.niqiu_flag_img_path)
        if niqiux>0 and niqiuy>0:
            print('找到召唤石niqiu', niqiux, niqiuy)
            auto.toclick(niqiux,niqiuy)
            return
        xianyux, xianyuy = sc.find_xy(c.xianyu_flag_img_path)
        if xianyux>0 and xianyuy>0:
            print('找到召唤石xianyu', xianyux, xianyuy)
            auto.toclick(xianyux,xianyuy)
            return
    
    auto.toclick(159,508)

def toTag(tag):
    if tag == 3:
        auto.toclick(370,90)
    # 二号书签位
    if tag == 2:
        auto.toclick(242,90)
    # 一号书签位
    else:
        auto.toclick(106,90)

## 杀牛任务
def taskshaniu():
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
                selectSummon('huanglong')
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
                setState('result')
                # 可能会出现正在加载按钮的情况 这种情况等待
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx == 0 and oky == 0:
                    continue
                if sc.is_again_result():
                    print('继续结算页 状态')
                    auto.toclick(200,557)
                else:
                    toTag(2)
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
                toTag(2)

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
                setState('result')
                # 可能会出现正在加载按钮的情况 这种情况等待
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx == 0 and oky == 0:
                    continue
                if sc.is_again_result():
                    print('继续结算页 状态')
                    auto.toclick(200,557)
                else:
                    toTag(2)
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
                toTag(2)

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
    


## 大巴任务
def taskdaba():
    global lastTime
    global lastState
    util.log_h1_start(f'开始')
    start_time = time.time()
    battle_time = 0
    attackTime = 0
    while(True):
        time.sleep(0.4)
        if sc.shot() and sc.image_check(c.img_sc_path,c.screen_size):                                                          ## 截图
            sc.acrop() ## 分截图
            if sc.is_error(): ## 如果出现错误页面 直接刷新
                auto.refresh()
                continue
            if sc.is_defeated():
                auto.refresh()
                continue
            if sc.is_validate(): ## 出现验证码 最高优先级事件 退出并报警
                dealValidate()
                continue
            if lastTime > 10:
                auto.refresh()
                lastTime = 0
                continue
            if sc.is_summon():
                # if sc.is_hpcheck():
                setState('summon')
                selectSummon('gaoda')
                #selectSummon('qijie')
                auto.toclick(419,759)
                # else:
                #     setState('xueliang')
                #     print('大巴血量太低换一只')
                #     auto.move_to_click(20,93)
                continue
            if sc.is_readysum():
                setState('readysum')
                auto.toclick(419,787)
                continue
            if sc.is_raid():
                if sc.is_nullep():
                    print('没有豆子了')
                    auto.toclick(398,174)
                    continue
                if sc.is_raidcheck():
                    auto.toclick(252,258)
                    time.sleep(1)
                    # 进行其他场次结算
                    auto.toclick(154,323)
                    continue
                israidid = sc.is_raidid()
                if israidid == False:
                    auto.toclick(462,343)
                    time.sleep(0.1)
                    israidid = sc.is_raidid()
                if israidid == True:
                    auto.move_to_click(704,204)
                    time.sleep(0.1)
                    auto.move_to_click(704,204)
                    auto.move_to_click(203,595)
                    paste()
                    auto.toclick(406,594)
                
            if sc.is_batload():
                setState('batload')
                continue
            if sc.is_resload():
                setState('resload')
                # auto.toclick(112,532)
                continue
            if sc.is_battle2() or sc.is_battle():
                if sc.is_die():
                    auto.move_to_click(22,90)
                    continue
                if sc.is_fa() == 2:
                    auto.toclick(112,532)
                if sc.is_fa() == 1:
                    isattack =  sc.is_attack()
                    if isattack == 0:
                        auto.refresh()
                        attackTime = 0
                        time.sleep(0.4)
                        auto.toclick(325,412)
                        continue
                    if isattack == 1:
                        setState('attack')
                        continue
                    attackTime+= 1
                    print(attackTime)
                    if attackTime > 60:
                        print('尼玛币卡了')
                        auto.refresh()
                        attackTime = 0
                        time.sleep(0.4)
                        auto.toclick(325,412)

                continue
            if sc.is_exup2():
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
                if sc.is_pending_result():
                    print('待结算页 状态')
                    auto.toclick(200,557)
                    time.sleep(1)
                    # 进行其他场次结算
                    auto.toclick(154,323)
                else:
                    auto.move_to_click(20,93)
                continue
            if sc.is_douzi_window():
                okx, oky = sc.find_xy(c.douzi2_flag_img_path)
                if okx>0 and oky>0:
                    print('豆子弹窗 状态', okx, oky)
                    oky = oky + 100
                    auto.toclick(okx, oky)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky - 200)
                    time.sleep(0.5 + random.random()/10)
                    auto.toclick(okx, oky + 55)
                    setState('douzi')
                    continue
            if sc.is_douzirecover_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('吃完豆子弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    time.sleep(1)
                    continue
            if sc.is_trophy_window():
                okx, oky = sc.find_xy(c.closebutton_flag_img_path)
                if okx>0 and oky>0:
                    print('获得成就弹窗 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('close')
                    continue
            if sc.is_exp_window() or sc.is_honor_window()  or sc.is_neterror_window():
                okx, oky = sc.find_xy(c.ok_flag_img_path)
                if okx>0 and oky>0:
                    print('按钮 状态', okx, oky)
                    auto.toclick(okx,oky)
                    setState('ok')
                    continue
            if sc.is_die2():
                auto.move_to_click(22,90)
                continue
            if sc.is_threeerror_window():
                time.sleep(600)
                auto.refresh()
                continue
            if sc.is_iderror_window():
                auto.refresh()
                continue
            if sc.is_black_window():
                setState('black')
                continue
            


            # 走到这里就是未识别的场景 直接exit
            setState('error')
            print('此场景未识别')
            if lastState == 'error' and lastTime > 6:
                send("errorsence")
                playsound('alert.mp3')
                exit()
            continue
        return False
    end_time = time.time()
    cost_time = end_time - start_time
    util.log_h1_end(f'结束 耗时 %.3f' % cost_time)
    time.sleep(1)


