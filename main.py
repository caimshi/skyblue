# -*- coding: utf-8 -*-
##########################
####    程序入口      ####
##########################


import screen as sc
import util
import constant as c
import time
import auto
import os
import argparse
import flow

###  将新图加入训练集 并 训练模型
def move_learn():
    sc.dir_check()
    util.log_title('图片朝向确认')
    confirm = input(f'请确认路径  {os.path.abspath(c.new_front_img_dir)}   下图片朝向均为  > 前 <  : (确认后输入 Y , 输入其他退出) ')
    if confirm == 'Y' or confirm == 'y':
        confirm = input(f'请确认路径  {os.path.abspath(c.new_others_img_dir)}   下图片朝向均为  > 左 右 后 < : (确认后输入 Y , 输入其他退出)')
        if confirm == 'Y' or confirm == 'y':
            util.log_h1_start('开始')
            sc.move_new_to_train()   
    util.log_h1_end('结束')

### 测试
def run_test():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        if(True):
            util.log_h1_start(f'开始')
            start_time = time.time()
            flow.test()
            end_time = time.time()
            cost_time = end_time - start_time
            util.log_h1_end(f'结束 耗时 %.3f' % cost_time)
            time.sleep(3)
            exit()

### 自动执行战货
def auto_taskzhanhuo():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        flow.taskzhanhuo()

### 自动执行星本
def auto_taskxingben():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        flow.taskxingben()



parser = argparse.ArgumentParser()

parser.add_argument("--test", help="Run Test", type=int)
parser.add_argument("--zhanhuo", help="Auto Task Zhanhuo", type=int)
parser.add_argument("--xingben", help="Auto Task xingben", type=int)
parser.add_argument("--learn", help="Lean Clean", type=int)

args = parser.parse_args()

if args.test:
    run_test()

if args.zhanhuo:
    auto_taskzhanhuo()

if args.xingben:
    auto_taskxingben()

if args.learn:
    move_learn()


if __name__ == '__main__':
    print('Bye~')
