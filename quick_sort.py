#!/usr/bin/python
#coding:utf-8


import sys

def quick_sort(A):
    partion_sort(A, 0, len(A) - 1)

def partion_sort(A, begin, end):
    if begin > end:
        return
    pivot = A[begin]
    lo, hi = begin, end
    while lo < hi:
        while hi > lo and A[hi] >= pivot:
            hi -= 1
        while lo < hi and A[lo] <= pivot:
            lo += 1
        if lo < hi:
            A[lo], A[hi] = A[hi], A[lo]
    A[begin], A[lo] = A[lo], A[begin]
    partion_sort(A, begin, lo-1)
    partion_sort(A, lo+1, end)


if __name__ == "__main__":
    T = [9, 10, 7, 12, 19, 3, 2, 18, 25]
    quick_sort(T)
    print(T)