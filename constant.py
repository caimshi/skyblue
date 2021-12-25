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

raidcheck_shape = (218,253,287,273)
raidcheck_img_name = 'raidcheck.jpg'
raidcheck_img_path =  os.path.join(sub_dir_path,raidcheck_img_name)

quest_shape = (71,452,159,469)
quest_img_name = 'quest.jpg'
quest_img_path =  os.path.join(sub_dir_path,quest_img_name)
specialquest_shape = (83,326,522,376)
specialquest_img_name = 'specialquest.jpg'
specialquest_img_path =  os.path.join(sub_dir_path,specialquest_img_name)
friend_shape = (233,449,480,486)
friend_img_name = 'friend.jpg'
friend_img_path =  os.path.join(sub_dir_path,friend_img_name)

raidid_shape = (70,685,529,1039)
raidid_img_name = 'raidid.jpg'
raidid_img_path =  os.path.join(sub_dir_path,raidid_img_name)

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

battle2_shape = (81,729,262,765)
battle2_img_name = 'battle2.jpg'
battle2_img_path =  os.path.join(sub_dir_path,battle2_img_name)

attack_shape = (377,491,491,517)
attack_img_name = 'attack.jpg'
attack_img_path =  os.path.join(sub_dir_path,attack_img_name)

exup2_shape = (144,501,451,526)
exup2_img_name = 'exup2.jpg'
exup2_img_path =  os.path.join(sub_dir_path,exup2_img_name)

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

summon2_shape = (230,340,379,355)
summon2_img_name = 'summon22.jpg'
summon2_img_path =  os.path.join(sub_dir_path,summon2_img_name)

readysum_shape = (248,592,353,611)
readysum_img_name = 'readysum.jpg'
readysum_img_path =  os.path.join(sub_dir_path,readysum_img_name)

again_shape = (102,534,128,555)
again_img_name = 'again.jpg'
again_img_path =  os.path.join(sub_dir_path,again_img_name)

pending_shape = (102,536,118,556)
pending_img_name = 'pending.jpg'
pending_img_path =  os.path.join(sub_dir_path,pending_img_name)

event_shape = (486,436,525,476)
event_img_name = 'event.jpg'
event_img_path =  os.path.join(sub_dir_path,event_img_name)

defeated_shape = (243,319,370,464)
defeated_img_name = 'defeated.jpg'
defeated_img_path =  os.path.join(sub_dir_path,defeated_img_name)

die_shape = (322,573,388,714)
die_img_name = 'die.jpg'
die_img_path =  os.path.join(sub_dir_path,die_img_name)
hpcheck_shape = (191,248,286,255)
hpcheck_img_name = 'hpcheck.jpg'
hpcheck_img_path =  os.path.join(sub_dir_path,hpcheck_img_name)
resume_shape = (345,610,488,639)
resume_img_name = 'resume.jpg'
resume_img_path =  os.path.join(sub_dir_path,resume_img_name)

# nullep_shape = (419,171,430,180)
nullep_shape = (395,171,406,180)
nullep_img_name = 'nullep.jpg'
nullep_img_path =  os.path.join(sub_dir_path,nullep_img_name)
valisend_shape = (125,903,486,956)
valisend_img_name = 'valisend.jpg'
valisend_img_path =  os.path.join(sub_dir_path,valisend_img_name)

valiall_img_name = 'valiall.jpg'
valiall_img_path =  os.path.join(sub_dir_path,valiall_img_name)



popup_sub_img_path = os.path.join(sub_dir_path,'pop_sub.jpg')


crop_4_img_names = ['1.jpg','2.jpg','3.jpg','4.jpg']
crop_4_img_paths = [ os.path.join(sub_dir_path,crop_4_img_name) for crop_4_img_name in crop_4_img_names ]

### images/flag

main_flag_img_name = 'main_flag.jpg'
main_flag_img_path = os.path.join(flag_dir_path,main_flag_img_name)
raid_flag_img_name = 'raid_flag.jpg'
raid_flag_img_path = os.path.join(flag_dir_path,raid_flag_img_name)
resume_flag_img_name = 'resume_flag.jpg'
resume_flag_img_path = os.path.join(flag_dir_path,resume_flag_img_name)
resume2_flag_img_name = 'resume2_flag.jpg'
resume2_flag_img_path = os.path.join(flag_dir_path,resume2_flag_img_name)
quest_flag_img_name = 'quest_flag.jpg'
quest_flag_img_path = os.path.join(flag_dir_path,quest_flag_img_name)
specialquest_flag_img_name = 'specialquest_flag.jpg'
specialquest_flag_img_path = os.path.join(flag_dir_path,specialquest_flag_img_name)
friend_flag_img_name = 'friend_flag.jpg'
friend_flag_img_path = os.path.join(flag_dir_path,friend_flag_img_name)
raidcheck_flag_img_name = 'raidcheck_flag.jpg'
raidcheck_flag_img_path = os.path.join(flag_dir_path,raidcheck_flag_img_name)
batload_flag_img_name = 'batload_flag.jpg'
batload_flag_img_path = os.path.join(flag_dir_path,batload_flag_img_name)
resload_flag_img_name = 'resload_flag.jpg'
resload_flag_img_path = os.path.join(flag_dir_path,resload_flag_img_name)
stepload_flag_img_name = 'stepload_flag.jpg'
stepload_flag_img_path = os.path.join(flag_dir_path,stepload_flag_img_name)
battle_flag_img_name = 'battle_flag.jpg'
battle_flag_img_path = os.path.join(flag_dir_path,battle_flag_img_name)
battle2_flag_1_img_name = 'battle2_flag_1.jpg'
battle2_flag_1_img_path = os.path.join(flag_dir_path,battle2_flag_1_img_name)
battle2_flag_2_img_name = 'battle2_flag_2.jpg'
battle2_flag_2_img_path = os.path.join(flag_dir_path,battle2_flag_2_img_name)
ok_flag_img_name = 'ok_flag.jpg'
ok_flag_img_path = os.path.join(flag_dir_path,ok_flag_img_name)
cancel_flag_img_name = 'cancel_flag.jpg'
cancel_flag_img_path = os.path.join(flag_dir_path,cancel_flag_img_name)
hpcheck_flag_img_name = 'hpcheck_flag.jpg'
hpcheck_flag_img_path = os.path.join(flag_dir_path,hpcheck_flag_img_name)
usebutton_flag_img_name = 'usebutton_flag.jpg'
usebutton_flag_img_path = os.path.join(flag_dir_path,usebutton_flag_img_name)
exup_flag_img_name = 'exup_flag.jpg'
exup_flag_img_path = os.path.join(flag_dir_path,exup_flag_img_name)
exup2_flag_img_name = 'exup2_flag.jpg'
exup2_flag_img_path = os.path.join(flag_dir_path,exup2_flag_img_name)
result_flag_img_name = 'result_flag.jpg'
result_flag_img_path = os.path.join(flag_dir_path,result_flag_img_name)
error_flag_img_name = 'error_flag.jpg'
error_flag_img_path = os.path.join(flag_dir_path,error_flag_img_name)
neterror_flag_img_name = 'neterror_flag.jpg'
neterror_flag_img_path = os.path.join(flag_dir_path,neterror_flag_img_name)
iderror_flag_img_name = 'iderror_flag.jpg'
iderror_flag_img_path = os.path.join(flag_dir_path,iderror_flag_img_name)
threeerror_flag_img_name = 'threeerror_flag.jpg'
threeerror_flag_img_path = os.path.join(flag_dir_path,threeerror_flag_img_name)
defeated_flag_img_name = 'defeated_flag.jpg'
defeated_flag_img_path = os.path.join(flag_dir_path,defeated_flag_img_name)
defeated2_flag_img_name = 'defeated2_flag.jpg'
defeated2_flag_img_path = os.path.join(flag_dir_path,defeated2_flag_img_name)
black_flag_img_name = 'black_flag.jpg'
black_flag_img_path = os.path.join(flag_dir_path,black_flag_img_name)
summon_flag_img_name = 'summon_flag.jpg'
summon_flag_img_path = os.path.join(flag_dir_path,summon_flag_img_name)
summon2_flag_img_name = 'summon2_flag.jpg'
summon2_flag_img_path = os.path.join(flag_dir_path,summon2_flag_img_name)
readysum_flag_img_name = 'readysum_flag.jpg'
readysum_flag_img_path = os.path.join(flag_dir_path,readysum_flag_img_name)
exp_flag_img_name = 'exp_flag.jpg'
exp_flag_img_path = os.path.join(flag_dir_path,exp_flag_img_name)
exp2_flag_img_name = 'exp2_flag.jpg'
exp2_flag_img_path = os.path.join(flag_dir_path,exp2_flag_img_name)
honor_flag_img_name = 'honor_flag.jpg'
honor_flag_img_path = os.path.join(flag_dir_path,honor_flag_img_name)
sixiang_flag_img_name = 'sixiang_flag.jpg'
sixiang_flag_img_path = os.path.join(flag_dir_path,sixiang_flag_img_name)
rupie_flag_img_name = 'rupie_flag.jpg'
rupie_flag_img_path = os.path.join(flag_dir_path,rupie_flag_img_name)
again_flag_img_name = 'again_flag.jpg'
again_flag_img_path = os.path.join(flag_dir_path,again_flag_img_name)
pending_flag_img_name = 'pending_flag.jpg'
pending_flag_img_path = os.path.join(flag_dir_path,pending_flag_img_name)
event_flag_img_name = 'event_flag.jpg'
event_flag_img_path = os.path.join(flag_dir_path,event_flag_img_name)
nightmare_flag_img_name = 'nightmare_flag.jpg'
nightmare_flag_img_path = os.path.join(flag_dir_path,nightmare_flag_img_name)
extreme_flag_img_name = 'extreme_flag.jpg'
extreme_flag_img_path = os.path.join(flag_dir_path,extreme_flag_img_name)
die_flag_img_name = 'die_flag.jpg'
die_flag_img_path = os.path.join(flag_dir_path,die_flag_img_name)
die2_flag_img_name = 'die2_flag.jpg'
die2_flag_img_path = os.path.join(flag_dir_path,die2_flag_img_name)
nullep_flag_img_name = 'nullep_flag.jpg'
nullep_flag_img_path = os.path.join(flag_dir_path,nullep_flag_img_name)
raidid_flag_img_name = 'raidid_flag.jpg'
raidid_flag_img_path = os.path.join(flag_dir_path,raidid_flag_img_name)
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
douzi_flag_img_name = 'douzi_flag.jpg'
douzi_flag_img_path = os.path.join(flag_dir_path,douzi_flag_img_name)
halfhong2_flag_img_name = 'halfhong2_flag.jpg'
halfhong2_flag_img_path = os.path.join(flag_dir_path,halfhong2_flag_img_name)
douzi2_flag_img_name = 'douzi2_flag.jpg'
douzi2_flag_img_path = os.path.join(flag_dir_path,douzi2_flag_img_name)
halfhongrecover_flag_img_name = 'halfhongrecover_flag.jpg'
halfhongrecover_flag_img_path = os.path.join(flag_dir_path,halfhongrecover_flag_img_name)
douzirecover_flag_img_name = 'douzirecover_flag.jpg'
douzirecover_flag_img_path = os.path.join(flag_dir_path,douzirecover_flag_img_name)
trophy_flag_img_name = 'trophy_flag.jpg'
trophy_flag_img_path = os.path.join(flag_dir_path,trophy_flag_img_name)
closebutton_flag_img_name = 'closebutton_flag.jpg'
closebutton_flag_img_path = os.path.join(flag_dir_path,closebutton_flag_img_name)
validate_flag_img_name = 'vali_flag.jpg'
validate_flag_img_path = os.path.join(flag_dir_path,validate_flag_img_name)
captcha_flag_img_name = 'captcha_flag.jpg'
captcha_flag_img_path = os.path.join(flag_dir_path,captcha_flag_img_name)
valisend_flag_img_name = 'valisend_flag.jpg'
valisend_flag_img_path = os.path.join(flag_dir_path,valisend_flag_img_name)

#store
validate1_store_img_name = 'validate1.jpg'
validate1_store_img_path = os.path.join(store_dir_path,validate1_store_img_name)
validate2_store_img_name = 'validate2.jpg'
validate2_store_img_path = os.path.join(store_dir_path,validate2_store_img_name)
validate3_store_img_name = 'validate3.jpg'
validate3_store_img_path = os.path.join(store_dir_path,validate3_store_img_name)

# summon
titan_flag_img_name = 'titan_flag.jpg'
titan_flag_img_path = os.path.join(flag_dir_path,titan_flag_img_name)
titan2_flag_img_name = 'titan2_flag.jpg'
titan2_flag_img_path = os.path.join(flag_dir_path,titan2_flag_img_name)
hades_flag_img_name = 'hades_flag.jpg'
hades_flag_img_path = os.path.join(flag_dir_path,hades_flag_img_name)
hades2_flag_img_name = 'hades2_flag.jpg'
hades2_flag_img_path = os.path.join(flag_dir_path,hades2_flag_img_name)
chuanma_flag_img_name = 'chuanma_flag.jpg'
chuanma_flag_img_path = os.path.join(flag_dir_path,chuanma_flag_img_name)
daba_flag_img_name = 'daba_flag.jpg'
daba_flag_img_path = os.path.join(flag_dir_path,daba_flag_img_name)
shendun_flag_img_name = 'shendun_flag.jpg'
shendun_flag_img_path = os.path.join(flag_dir_path,shendun_flag_img_name)
huanglong_flag_img_name = 'huanglong_flag.jpg'
huanglong_flag_img_path = os.path.join(flag_dir_path,huanglong_flag_img_name)
niqiu_flag_img_name = 'niqiu_flag.jpg'
niqiu_flag_img_path = os.path.join(flag_dir_path,niqiu_flag_img_name)
xianyu_flag_img_name = 'xianyu_flag.jpg'
xianyu_flag_img_path = os.path.join(flag_dir_path,xianyu_flag_img_name)
zhousi_flag_img_name = 'zhousi_flag.jpg'
zhousi_flag_img_path = os.path.join(flag_dir_path,zhousi_flag_img_name)
gaoda_flag_img_name = 'gaoda_flag.jpg'
gaoda_flag_img_path = os.path.join(flag_dir_path,gaoda_flag_img_name)
fengma_flag_img_name = 'fengma_flag.jpg'
fengma_flag_img_path = os.path.join(flag_dir_path,fengma_flag_img_name)
qijie_flag_img_name = 'qijie_flag.jpg'
qijie_flag_img_path = os.path.join(flag_dir_path,qijie_flag_img_name)
lu_flag_img_name = 'lu_flag.jpg'
lu_flag_img_path = os.path.join(flag_dir_path,lu_flag_img_name)



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