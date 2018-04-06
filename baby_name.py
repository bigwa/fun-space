# coding=utf-8
import string
import re

SECTION_COUNT = 7

def getcharbycount(lines, char_count):
    char_map = [[],[],[],[],[]]
    for i in range(6):
        if i == 0 :
            continue
        num = (char_count - 1) * SECTION_COUNT + i
        tmp = lines[num].split(':')[1]
        char_map[i-1] = tmp

    return char_map

def init_dic(file_name):
    content = open(file_name, 'r').read().decode('gbk')
    lines = content.split('\n');

    return lines

def main_count(lines):
    wuxing_map = ['金','木','水','火','土']
    result_file = 'namelist.txt'
    result_handle = open(result_file, 'w')
    
    name = '邢'
    tiange = 12
    dige_list =  [1,3,5,6,8,11,15,16,21,24,31,37,41,47,48,52,63,65,67,81]
    renge_list = [1,3,5,6,8,11,15,16,21,24,31,37,41,47,48,52,63,65,67,81]

    for renge in renge_list:
        second_char_num = renge - tiange + 1
        third_char_num = 0
        if second_char_num <= 0 or second_char_num > 26:
            continue
        print "second:%d"%second_char_num
        char_map_second = getcharbycount(lines, second_char_num)

        for dige in dige_list:
            third_char_num = dige - second_char_num
            if third_char_num <= 0 or third_char_num > 26:
                continue

            print "third:%d"%third_char_num
            char_map_third = getcharbycount(lines, third_char_num)
    
            for i in range(5):
                for j in range(5):
                    if i!=0 and j!=0 :
                        continue

                    wuxingname = wuxing_map[i] + wuxing_map[j]

                    char_list_second = char_map_second[i]
                    char_list_third  = char_map_third[j]

                    for char2 in char_list_second:
                        for char3 in char_list_third:
                            result_handle.write(name+char2+char3 +'  '+ wuxingname + "%d,%d"%(second_char_num,third_char_num) + "\n")             
        
        result_handle.close

if __name__ == '__main__' :
    f_name = 'zhouyi.txt'
    lines = init_dic(f_name)
    main_count(lines)

        
            
            
