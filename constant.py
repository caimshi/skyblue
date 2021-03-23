# -*- coding: utf-8 -*-
import os

# 截图存档目录
img_dir_path = r'images'
flag_dir_path = r'images/flag'
sub_dir_path = r'images/sub'
data_dir_path = r'images/data'
store_dir_path = r'images/store'
captcha_dir_path = r'images/captcha'

model_dir_path = r'model'

driver_dir_path = r'./driver'

##############

### images
img_sc_name = 'gbf.jpg'
img_sc_path = os.path.join(img_dir_path,img_sc_name)

img_desktop_name = 'desktop.jpg'
img_desktop_path = os.path.join(img_dir_path,img_desktop_name)


### images/data/
train_dir = os.path.abspath(data_dir_path+'/train')
validation_dir = data_dir_path+'/validation'
new_dir_path = os.path.abspath(data_dir_path+'/new')

front_img_dir = os.path.join(train_dir,'front')
others_img_dir = os.path.join(train_dir,'others')

new_front_img_dir = os.path.abspath(new_dir_path+'/front')
new_others_img_dir = os.path.abspath(new_dir_path+'/others')

### model/
model_path = os.path.join(model_dir_path,'mhxy.h5')


### images/sub
main_shape = (100,316,171,353)
main_img_name = 'main.jpg'
main_img_path =  os.path.join(sub_dir_path,main_img_name)

raid_shape = (481,228,529,282)
raid_img_name = 'raid.jpg'
raid_img_path =  os.path.join(sub_dir_path,raid_img_name)

batload_shape = (146,348,449,432)
batload_img_name = 'batload.jpg'
batload_img_path =  os.path.join(sub_dir_path,batload_img_name)

resload_shape = (326,716,529,749)
resload_img_name = 'resload.jpg'
resload_img_path =  os.path.join(sub_dir_path,resload_img_name)

stepload_shape = (122,518,482,537)
stepload_img_name = 'stepload.jpg'
stepload_img_path =  os.path.join(sub_dir_path,stepload_img_name)

battle_shape = (454,117,539,146)
battle_img_name = 'battle.jpg'
battle_img_path =  os.path.join(sub_dir_path,battle_img_name)

attack_shape = (377,491,491,517)
attack_img_name = 'attack.jpg'
attack_img_path =  os.path.join(sub_dir_path,attack_img_name)

fa_shape = (102,525,139,540)
fa_img_name = 'fa.jpg'
fa_img_path =  os.path.join(sub_dir_path,fa_img_name)

result_shape = (154,145,458,177)
result_img_name = 'result.jpg'
result_img_path =  os.path.join(sub_dir_path,result_img_name)

error_shape = (179,399,427,485)
error_img_name = 'error.jpg'
error_img_path =  os.path.join(sub_dir_path,error_img_name)

summon_shape = (225,298,383,319)
summon_img_name = 'summon.jpg'
summon_img_path =  os.path.join(sub_dir_path,summon_img_name)

readysum_shape = (248,592,353,611)
readysum_img_name = 'readysum.jpg'
readysum_img_path =  os.path.join(sub_dir_path,readysum_img_name)

again_shape = (102,534,128,555)
again_img_name = 'again.jpg'
again_img_path =  os.path.join(sub_dir_path,again_img_name)

event_shape = (486,436,525,476)
event_img_name = 'event.jpg'
event_img_path =  os.path.join(sub_dir_path,event_img_name)



popup_sub_img_path = os.path.join(sub_dir_path,'pop_sub.jpg')


crop_4_img_names = ['1.jpg','2.jpg','3.jpg','4.jpg']
crop_4_img_paths = [ os.path.join(sub_dir_path,crop_4_img_name) for crop_4_img_name in crop_4_img_names ]

### images/flag

main_flag_img_name = 'main_flag.jpg'
main_flag_img_path = os.path.join(flag_dir_path,main_flag_img_name)
raid_flag_img_name = 'raid_flag.jpg'
raid_flag_img_path = os.path.join(flag_dir_path,raid_flag_img_name)
batload_flag_img_name = 'batload_flag.jpg'
batload_flag_img_path = os.path.join(flag_dir_path,batload_flag_img_name)
resload_flag_img_name = 'resload_flag.jpg'
resload_flag_img_path = os.path.join(flag_dir_path,resload_flag_img_name)
stepload_flag_img_name = 'stepload_flag.jpg'
stepload_flag_img_path = os.path.join(flag_dir_path,stepload_flag_img_name)
battle_flag_img_name = 'battle_flag.jpg'
battle_flag_img_path = os.path.join(flag_dir_path,battle_flag_img_name)
ok_flag_img_name = 'ok_flag.jpg'
ok_flag_img_path = os.path.join(flag_dir_path,ok_flag_img_name)
usebutton_flag_img_name = 'usebutton_flag.jpg'
usebutton_flag_img_path = os.path.join(flag_dir_path,usebutton_flag_img_name)
exup_flag_img_name = 'exup_flag.jpg'
exup_flag_img_path = os.path.join(flag_dir_path,exup_flag_img_name)
result_flag_img_name = 'result_flag.jpg'
result_flag_img_path = os.path.join(flag_dir_path,result_flag_img_name)
error_flag_img_name = 'error_flag.jpg'
error_flag_img_path = os.path.join(flag_dir_path,error_flag_img_name)
neterror_flag_img_name = 'neterror_flag.jpg'
neterror_flag_img_path = os.path.join(flag_dir_path,neterror_flag_img_name)
summon_flag_img_name = 'summon_flag.jpg'
summon_flag_img_path = os.path.join(flag_dir_path,summon_flag_img_name)
readysum_flag_img_name = 'readysum_flag.jpg'
readysum_flag_img_path = os.path.join(flag_dir_path,readysum_flag_img_name)
exp_flag_img_name = 'exp_flag.jpg'
exp_flag_img_path = os.path.join(flag_dir_path,exp_flag_img_name)
honor_flag_img_name = 'honor_flag.jpg'
honor_flag_img_path = os.path.join(flag_dir_path,honor_flag_img_name)
again_flag_img_name = 'again_flag.jpg'
again_flag_img_path = os.path.join(flag_dir_path,again_flag_img_name)
event_flag_img_name = 'event_flag.jpg'
event_flag_img_path = os.path.join(flag_dir_path,event_flag_img_name)
nightmare_flag_img_name = 'nightmare_flag.jpg'
nightmare_flag_img_path = os.path.join(flag_dir_path,nightmare_flag_img_name)
fa_flag_1_img_name = 'fa_flag_1.jpg'
fa_flag_1_img_path = os.path.join(flag_dir_path,fa_flag_1_img_name)
fa_flag_2_img_name = 'fa_flag_2.jpg'
fa_flag_2_img_path = os.path.join(flag_dir_path,fa_flag_2_img_name)
attack_flag_1_img_name = 'attack_flag_1.jpg'
attack_flag_1_img_path = os.path.join(flag_dir_path,attack_flag_1_img_name)
attack_flag_2_img_name = 'attack_flag_2.jpg'
attack_flag_2_img_path = os.path.join(flag_dir_path,attack_flag_2_img_name)

halfhong_flag_img_name = 'halfhong_flag.jpg'
halfhong_flag_img_path = os.path.join(flag_dir_path,halfhong_flag_img_name)
halfhong2_flag_img_name = 'halfhong2_flag.jpg'
halfhong2_flag_img_path = os.path.join(flag_dir_path,halfhong2_flag_img_name)
halfhongrecover_flag_img_name = 'halfhongrecover_flag.jpg'
halfhongrecover_flag_img_path = os.path.join(flag_dir_path,halfhongrecover_flag_img_name)
trophy_flag_img_name = 'trophy_flag.jpg'
trophy_flag_img_path = os.path.join(flag_dir_path,trophy_flag_img_name)
closebutton_flag_img_name = 'closebutton_flag.jpg'
closebutton_flag_img_path = os.path.join(flag_dir_path,closebutton_flag_img_name)
validate_flag_img_name = 'vali_flag.jpg'
validate_flag_img_path = os.path.join(flag_dir_path,validate_flag_img_name)
captcha_flag_img_name = 'captcha_flag.jpg'
captcha_flag_img_path = os.path.join(flag_dir_path,captcha_flag_img_name)

#store
validate1_store_img_name = 'validate1.jpg'
validate1_store_img_path = os.path.join(store_dir_path,validate1_store_img_name)

# summon
titan_flag_img_name = 'titan_flag.jpg'
titan_flag_img_path = os.path.join(flag_dir_path,titan_flag_img_name)
titan2_flag_img_name = 'titan2_flag.jpg'
titan2_flag_img_path = os.path.join(flag_dir_path,titan2_flag_img_name)
shendun_flag_img_name = 'shendun_flag.jpg'
shendun_flag_img_path = os.path.join(flag_dir_path,shendun_flag_img_name)

# fighting_flag_img_name = 'fighting_flag.jpg'
# fighting_flag_img_path = os.path.join(flag_dir_path,fighting_flag_img_name)

# popup_flag_img_names = ['popup_flag_1.jpg','popup_flag_2.jpg']
# popup_flag_img_paths = [ os.path.join(flag_dir_path,popup_flag_img_name) for popup_flag_img_name in popup_flag_img_names ]

# mouse_flag_img_name = 'mouse_flag.jpg'
# mouse_flag_img_path = os.path.join(flag_dir_path,mouse_flag_img_name)



### driver

driver_name = 'kmclass'

kmclass_dll_path = os.path.abspath(driver_dir_path+'/kmclassdll.dll').replace('\\','\\\\')

kmclass_driver_path = os.path.abspath(driver_dir_path+'/kmclass.sys').replace('\\','\\\\')


## 截图大小
screen_size = (642,1399)
sub_size = (360,120)


### 移动偏移
## 弹框偏移
popup_move_shapes = [(-84,33,96,140),(-82,29,182,135)]

## 鼠标偏移
mouse_move_shape = (16,15)



if __name__ == '__main__':
    print('ok')
    print(kmclass_driver_path)