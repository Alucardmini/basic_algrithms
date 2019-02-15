#!/usr/bin/python
#coding:utf-8


def HeapSort(A):

    def heapify(A):
        start = (len(A) - 2) // 2
        while start >= 0:
            siftDown(A, start, len(A) - 1)
            start -= 1

    def siftDown(A, root, end):

        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                # 遍历子节点
                child += 1
            if child <= end and A[root] < A[child]:
                # 交换
                print('A: ', A)
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return
    heapify(A)
    print('--------')
    end = len(A) - 1
    while end > 0:
        A[end], A[0] = A[0], A[end]
        print('><A', A)

        siftDown(A, 0, end - 1)
        end -= 1

if __name__ == '__main__':

    # T = [13, 14, 94, 33, 82, 25, 59, 94, 65, 23, 45, 27, 73, 25, 39, 10]
    T = [9, 10, 7, 12, 19, 3, 2, 18, 25]
    HeapSort(T)
