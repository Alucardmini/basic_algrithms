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
        self.update_value(target_value=num, flag=1)

    def div_num(self, num):
        n = 0
        while 1<<n < num:
            n +=1
        return n

    def remove(self, num):
        if num > self.capacity:
            print("你超纲了啊\n")
        self.update_value(target_value=num, flag=0)

    def find_location(self, target_value):
        # 1. 找到在第几个整数上
        index_of_bit = (target_value >> self.div_num)
        # 2. 在字节上的位置
        loc_in_bit = target_value % (self.max_bits_per_int + 1)
        return index_of_bit, loc_in_bit

    def query_value(self, target_value):
        index, loc = self.find_location(target_value)
        tmp_1_others_0 = 1<< loc
        # values_bin = bin(self.values[index])
        # tmp_1_others_0_str = bin(tmp_1_others_0)
        if self.values[index] & tmp_1_others_0 == 0:
            return False
        else:
            return True

    def update_value(self, target_value, flag=1):

        if flag == 1 and not self.query_value(target_value):
            index, loc = self.find_location(target_value)
            self.values[index] = self.values[index] | (1 << loc)
        elif flag == 0 and self.query_value(target_value):
            index, loc = self.find_location(target_value)
            self.values[index] = self.values[index] ^ (1 << loc)
        else:
            pass

    def sequence(self, reverse=False):
        if not reverse:
            start, end, step = 0, len(self.values), 1
        else:
            start, end, step = len(self.values)-1, -1, -1

        for i in range(start, end, step):
            value = self.values[i]
            count = 0
            while value != 0:
                values_bin = bin(value)
                if value & 1 == 1:
                    yield count + i * (1<<self.div_num)
                    value = value >> 1
                    count += 1
                else:
                    count += 1
                    value = value >> 1

if __name__ == "__main__":
    bit_map = XC_bitmap(1000)
    print(" need bit memory_size {a} 个整数(s) \n".format(a=bit_map.bit_size))
    num_list = [32, 63, 64, 65, 125, 126, 126, 128, 129, 98, 999]
    for _ in num_list:
        bit_map.add(_)
        # print("\n test _data \n")
    test_num_list = [1, 2, 3, 6, 8, 19, 31, 32,36, 63, 64, 65, 125, 126, 126, 128, 129, 98, 999]
    for _ in num_list:
        print(str(_) + " is_in " + str(bit_map.find_location(_)))

    print("\n == sort == \n")
    for _ in bit_map.sequence(reverse=True):
        print(_)




