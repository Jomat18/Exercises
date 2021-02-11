from heapq import heappush, heappop

def solution(t, input_arr):
    # your code goes here

    input_arr_sort = []
    size = len(input_arr)

    for element in input_arr:
        heappush(input_arr_sort, element)
    
    input_arr_sort = [heappop(input_arr_sort) for i in range(size)]

    for i in range(size-1, -1, -1):
        if t - input_arr_sort[i] >= 0:
            t = t - input_arr_sort[i]

    return t==0

def main():
    t = int(input().strip())
    _ = int(input().strip())
    input_arr = [int(n) for n in input().strip().split()]

    result = solution(t,input_arr)

    print(result)

if __name__=="__main__":
    main()