from collections import deque
 
stack = deque()

def solution(t, input_arr):
    # your code goes here

    mayor = 0
    time = 0

    for element in input_arr:
        if len(stack)<t:
            stack.append(element)

        else:
            if (element in stack): 
                time = time + 1
                
            else:    
                stack.popleft()
                stack.append(element)
                if time > mayor:
                    mayor = time
                
                time = 0


    return mayor

def main():
    t = int(input().strip())
    _ = int(input().strip())
    input_arr = [int(n) for n in input().strip().split()]

    result = solution(t,input_arr)

    print(result)

if __name__=="__main__":
    main()