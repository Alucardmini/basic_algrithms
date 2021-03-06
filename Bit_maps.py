# -*- coding:utf-8 -*-
# @version: 1.0
# @date: '12/29/18'
import sys
class Pybitmap(object):
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
            return False, index, loc
        else:
            return True, index, loc

    def update_value(self, target_value, flag=1):

        is_exit, index, loc = self.query_value(target_value)

        if flag == 1 and not is_exit:
            self.values[index] = self.values[index] | (1 << loc)
        elif flag == 0 and is_exit:
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
                if value & 1 == 1:
                    yield count + i * (1<<self.div_num)
                    value = max(value >> 1, 0)
                    count += 1
                else:
                    count += 1
                    value = max(value >> 1, 0)


if __name__ == "__main__":
    bit_map = Pybitmap(1000)
    # print(" need bit memory_size {a} 个整数(s) \n".format(a=bit_map.bit_size))
    #
    import numpy as np
    #
    test_list = np.random.randint(0, 1000, 100)
    print(test_list)
    for _ in test_list:
        bit_map.add(_)
    # print("\n == sort == \n")
    # print(list(bit_map.sequence(reverse=False)))
    # # [814 679 105 957 217 638 663  89 895 842]
    # print("13 + bin " + bin(-9223372036854774784))

    print(bit_map.query_value(43))




