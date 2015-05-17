#-*- coding:utf-8 -*-

import os, re
from bs4 import BeautifulSoup 

BOARD_ADDR = './app/templates/summary.html'


def getBoard(problem_num):
    if not os.path.exists(BOARD_ADDR):
        print 'path error, no summary.html'
    else:
        solve_list = []
        board = open(BOARD_ADDR, 'r')
        contents = board.read().decode('utf-8')
        soup = BeautifulSoup(contents)
        tr = soup.select('tr')
        for line in tr:
            record = [text for text in line.stripped_strings]
            # aa = u'2'  ＃这里测试都是True, 下面用record[0].isdigit()返回全是False
            # print aa.isdigit(), type(aa)
            if len(record) == problem_num + 5 and re.match(r'[0-9]+', record[0]): #不知道为啥record[0].isdigit()返回的全是False
                del record[0], record[2], record[problem_num + 2]
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

# 测试部分
# if __name__ == '__main__':
#     problem_num = raw_input('please input problem number')
#     getBoard(int(problem_num))