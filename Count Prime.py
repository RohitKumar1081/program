def count_prime(num):
    c=0
    if num<2:
        print(c)
    for i in range (3,num+1,2):
        for j in range(3,i+1,2):
            print(i,j)
            if (j%i!=0):
                c+=1
                print("after the loop",j,i)


count_prime(9)