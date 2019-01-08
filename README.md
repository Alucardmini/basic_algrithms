## pybitmap
### 安装:
    pip3 install pybitmap
#### 使用方法:
    bit_map = Pybitmap(1000000) # 1000000为指定size 表示存储最大的元素
#### 操作
    bit_map.add(32)  # 添加元素
    bit_map.remove(32)  # 删除元素
    print(list(bit_map.sequence(reverse=False)))  # 按序列输出元素, reverse 是否逆序

    #查找元素
    print(bit_map.query_value(43))
    返回: (False, 0, 43)
    False 表示不存在  (True 表示存在)
    0     表示应该存在的整型数字的序列
    43    整型数字中的位数


