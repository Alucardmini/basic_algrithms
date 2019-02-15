#!/usr/bin/python
#coding:utf-8


# 按照建立大根堆的规则刷新节点
def update_node(A, root, end):
    while root * 2 + 1 <= end:
        child = 2*root + 1
        if child <= end and child + 1 <= end:
            if A[child + 1] > A[child]:
                child = child+1
        if child <= end and A[child] > A[root]:
            # 最大的子节点大于root则交换　交换后使用同样的规则刷新子树
            A[root], A[child] = A[child], A[root]
            root = child
        else:
            return


def heap_sort(A):

    # 1. 构建大根堆
    root = (len(A)-2)//2
    end = len(A)-1
    while root >= 0:
        update_node(A, root, end)
        root -= 1

    # 2. 堆排序
    end = len(A) - 1
    while end >= 0:
        A[0], A[end] = A[end], A[0]
        # print('A:', A)
        end -= 1
        update_node(A, 0, end)
    return A

if __name__ == '__main__':
    T = [9, 10, 7, 12, 19, 3, 2, 18, 25]
    print(heap_sort(T))
