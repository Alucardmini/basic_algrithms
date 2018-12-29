# -*- coding:utf-8 -*-
# @version: 1.0
# @date: '12/29/18'
import sys
import math
class XC_bitmap(object):
    def __init__(self, capacity):
        self.capacity = capacity  # 需要存数据的数量
        self.max_bits_per_int = len(bin(sys.maxsize)) - 2
        self.div_num = self.div_num(self.max_bits_per_int)  # 6: 1<<6 = 64
        self.bit_size = (capacity >> self.div_num) + 1  # 需要分配的字节个数: 1个整数 4个字节, 1个字节 8个位 => 1个整数32个位置
        self.values = [0 for i in range(self.bit_size)]  # 分配字节

    def add(self, num):
        if num > self.capacity:
            print("你超纲了啊\n")
            return

        index, loc = self.find_location(num)

        self.values[index] = self.values[index] | (1<<loc)

    def div_num(self, num):
        n = 0
        while 1<<n < num:
            n +=1
        return n

    def remove(self, num):
        if num > self.capacity:
            print("你超纲了啊\n")

    def find_location(self, target_value):
        # 1. 找到在第几个整数上
        index_of_bit = (target_value >> self.div_num)
        # 2. 在字节上的位置
        loc_in_bit = target_value % self.div_num
        return index_of_bit, loc_in_bit

    def query_value(self, target_value):
        index, loc = self.find_location(target_value)
        tmp = sys.maxsize  # 全1的整数
        tmp_1_others_0 = 1<< ((loc-1) if loc>=1 else 0)
        if self.values[index] & tmp_1_others_0 == 0:
            return False
        else:
            return True

    def update_value(self, target_value, flag=1):
        # 1. 找到在第几个整数上
        index_of_bit = (target_value >> self.div_num)
        # 2. 在字节上的位置
        loc_in_bit = target_value % self.div_num
        if flag == 1:
            pass
        else:
            pass


if __name__ == "__main__":
    bit_map = XC_bitmap(1000)
    print(" need bit memory_size {a} 个整数(s) \n".format(a=bit_map.bit_size))
    num_list = [0, 1, 2, 3, 6, 8, 19, 31, 32,36, 63, 64, 65, 125, 126, 126, 128, 129, 98, 999]
    for _ in num_list:
        print(str(_) + " location " + str(bit_map.find_location(_)))

        bit_map.add(_)

    # for v in bit_map.values:
    #     print(bit_map.find_location(v))
    #     print(bin(v))
    #
    # print("\n test _data \n")
    #
    # test_num_list = [1, 2, 3, 6, 8, 19, 31, 32,36, 63, 64, 65, 125, 126, 126, 128, 129, 98, 999]
    # for _ in test_num_list:
    #     print(str(_) + " res " + str(bit_map.query_value(_)))
