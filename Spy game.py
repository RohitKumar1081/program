l = list(map(int,input("Enter the array as a String : ")))

def spy_game(arr):
    c=0
    for i in range(0,len(arr)):
        if arr[i]==0:
            for j in range(i+1,len(arr)):
                if arr[j]==0:
                    for k in range(j+1,len(arr)):
                        if arr[k]==7:
                            c=1
    print(c==1)


spy_game(l)

def spy(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    print(len(code)==1)

spy(l)