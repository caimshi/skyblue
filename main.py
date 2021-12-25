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
import fl.gzchl as gzchl
import fl.xingben as xingben
import fl.yuezhong as yuezhong
import fl.sixiang as sixiang
import fl.texing as texing

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
        xingben.taskxingben()
### 自动执行星本
def auto_tasktexing():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        texing.tasktexing()
def auto_tasksixiang():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        sixiang.tasksixiang()

### 自动执行月中
def auto_taskyuezhong():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        yuezhong.taskyuezhong()

### 自动执行大巴
def auto_taskdaba():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        flow.taskdaba()
### 自动执行shaniu
def auto_taskshaniu():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        flow.taskshaniu()
### 自动执行gzc
def auto_taskgzc95():
    util.log_h1(f'前置准备')
    if flow.dir_check():
        auto.open_driver()
        gzchl.taskgzc95()



parser = argparse.ArgumentParser()

parser.add_argument("--test", help="Run Test", type=int)
parser.add_argument("--zhanhuo", help="Auto Task Zhanhuo", type=int)
parser.add_argument("--daba", help="Auto Task daba", type=int)
parser.add_argument("--shaniu", help="Auto Task shaniu", type=int)
parser.add_argument("--xingben", help="Auto Task xingben", type=int)
parser.add_argument("--texing", help="Auto Task xingben", type=int)
parser.add_argument("--yuezhong", help="Auto Task yuezhong", type=int)
parser.add_argument("--sixiang", help="Auto Task sixiang", type=int)
parser.add_argument("--gzc95", help="Auto Task gzc95", type=int)
parser.add_argument("--learn", help="Lean Clean", type=int)

args = parser.parse_args()

if args.test:
    run_test()

if args.zhanhuo:
    auto_taskzhanhuo()

if args.xingben:
    auto_taskxingben()
if args.texing:
    auto_tasktexing()
if args.sixiang:
    auto_tasksixiang()

if args.daba:
    auto_taskdaba()

if args.yuezhong:
    auto_taskyuezhong()

if args.shaniu:
    auto_taskshaniu()

if args.gzc95:
    auto_taskgzc95()

if args.learn:
    move_learn()


if __name__ == '__main__':
    print('Bye~')
