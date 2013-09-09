#!/usr/bin/python

import random
import sys

def list_generator(int_count,line_count,lower_lim,upper_lim):
    random.seed()
    number_list = []
    for line in range(line_count):
        number_list.append([])
        for element in range(int_count):
            number_list[line].append(random.randint(lower_lim,upper_lim))
    return number_list

def list_to_string(group,delim,end_char):
    s_group = map(str,group)
    string = delim.join(s_group)
    string += end_char
    return string

def file_generator(number_list,filename):
    final_text = ''
    for li in number_list:
        final_text += list_to_string(li,' ','\n')
    fid = open(filename,'w')
    fid.write(final_text)
    print fid
    fid.close()

if __name__ == '__main__':
    #arg1 = number of integers per line
    #arg2 = number of lines
    #arg3 = lower limit of integers
    #arg4 = upper limit of integers
    #arg5 = filename

    args = sys.argv[1:]
    argc = len(args)
    filename = args[-1]
    
    if argc == 5:
        argi = []
        for i in range(argc-1):
            if not args[i].isalpha():
                if args[i][0] == '-' and args[i][1:].isdigit() or args[i].isdigit():
                    argi.append(int(args[i]))
                else:
                    print "This program requires 4 integers!"
                    exit()
            else:
                print "This program requires 4 integers!"
                exit()
        if argi[3] < argi[2]:
            temp = argi[2]
            argi[2] = argi[3]
            argi[3] = temp
        file_generator(list_generator(argi[0],argi[1],argi[2],argi[3]),filename)
    else:
        print "This program requires 4 integer arguments and 1 filename"
        exit()
