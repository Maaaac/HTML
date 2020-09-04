#coding:utf-8
import os
import json
import sys
import time

path = r'D:\Common\editor\WeaknessEditor\bin'

def file_name(file_dir):
    L=[]
    for root,dirs,files in os.walk(file_dir):
        #print(files)
        for file in files:
            if os.path.splitext(file)[1] == '.json':
                L.append(os.path.join(root,file))
    return L

def find_armour(armour_dir):
    # f = open(armour_dir,"r",encoding='utf-8')
    # data = f.read()
    # armour_data = json.loads(data)
    try:
        with open(armour_dir,'r',encoding='utf-8') as fp:
            json_data = json.load(fp)
        return json_data
    except Exception as e:
        pass
            # fw = open(r"C:\Users\wb.madecheng\Desktop\Dante\wrongtrace.txt",'a')
            # fw.write(str(e))
            # fw.write('\n')
            # fw.close()

def get(json_dir):
    json_data = find_armour(json_dir)
    
    kk = json_data.values()
    k = list(kk)
    # print(k)
    # print(k[1])
    # print(len(k))
    a = len(k)
    i = 0
    json_armour = []
    while i < a :
        bbb = list(k[i].values())
        if bbb[0] == 1:
            json_armour.append(i)
        i+=1

    if len(json_armour) > 0:
        f = open(r"C:\Users\wb.madecheng\Desktop\Dante\wrong_armour.txt",'a')
        f.write(json_dir+"    "+str(json_armour)+'\n')
        f.close()

def isrookie(file_name):
    rookie = ['ru_mt_t64','ge_lt_th301','ge_mt_leopard_x','ge_mt_kpz70','ge_ht_maus',
    'us_mt_m60','us_lt_xm8','us_ht_t58','us_td_t95','us_spg_m110','ge_spg_sp70',
    'ru_ht_kv1s','ru_mt_t28','ru_spg_su26','us_mt_m4','ge_ht_tiger','ge_mt_pz3',
    'ru_lt_t26','ru_td_su76','ru_mt_t28','ru_spg_su26','ru_lt_bt7','cn_mt_type59']
    for a in rookie:
        try:
            file_name.index(a)
            return -1
        except :
            pass

if __name__ == "__main__":
    f = open(r"C:\Users\wb.madecheng\Desktop\Dante\wrong_armour.txt",'a')
    strtime = str(time.strftime("%Y-%m-%d  %I:%M:%S"))
    f.write("----------------------------------------------------------------------------------------")
    f.write(strtime)
    f.write("----------------------------------------------------------------------------------------"+'\n')
    f.close()
    print(path)

    if len(sys.argv)<2:
        LI = file_name(path)
    else :
        # print(sys.argv[1]) 
        # print(repr(sys.argv[1]))
        # print(os.path.abspath(sys.argv[1]))
        LI = file_name(os.path.abspath(sys.argv[1]))
    print(LI)
    for li in LI:
        i = isrookie(li)
        if i != -1:
            if li[-11:] == "armour.json":
                get(li)


        
