#-*- coding:utf-8 -*-

import re
import os

BOARD_ADDR = './app/templates/summary.html'


def getBoard(problem_num):
    if not os.path.exists(BOARD_ADDR):
        print 'path error, no summary.html'
    else:
        solve_list = []
        board = open(BOARD_ADDR, 'r')
        contents = board.read().decode('utf-8')
        pattern = re.compile(r'<tr>(.*?)</tr>', re.S)
        lines = re.findall(pattern, contents)
        pattern = ''
        for i in range(problem_num + 5):  #summary里td标签除题目个数以外是5个
            pattern += '<td>(.*?)</td>'
        # print pattern
        pattern = re.compile(pattern, re.S)
        for line in lines:
            # print line
            info = re.findall(pattern, line)
            # print info
            if info and info[0][0] != '':
                # print info, len(info)
                record = []
                record = [info[0][1], info[0][2]]   #队伍名和总共解决的题数
                for i in range(4, problem_num + 4):
                        record.append(info[0][i][2])
                # print record
                solve_list.append(record)
        board.close()
        # output = open('./app/data/solve_list.txt', 'w') #如果需要保存信息到文件可以去掉注释
        # for data in solve_list:
        #     for info in data:
        #         output.write(info.encode('utf-8')+' ')
        #     output.write('\n')
        # output.close()
        return solve_list

#测试部分
# if __name__ == '__main__':
#     problem_num = raw_input('please input problem number')
#     getBoard(int(problem_num))