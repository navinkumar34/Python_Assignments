# 1 2 3 4 5....
def natural_number(N):
    for i in range(1,N+1):
        print(i, end=" ")

# 1 2 3 6 9 18 27 54...
def Series2(N):
    additive=1
    count=0
    sum=1
    print(sum, end=" ")
    for i in range(1,N):
        count+=1
        sum+=additive
        print(sum, end=" ")
        if(count==2):
            additive=sum
            count=0

#1 4 9 16 25.....
def squares(N):
    for i in range(1, N+1):
        print(i**2, end=" ")

#1 2 9 4 25 6 49.....
def Series4(N):
    for i in range(1, N+1):
        if i%2==0:
            print(i, end=" ")
        else:
            print(i**2, end=" ")

#1 5 9 6 25 8 49 .....
def Series5(N):
    print("1 5", end=" ")
    for i in range(3, N+1):
        if i%2==0:
            print(i+2, end=" ")
        else:
            print(i**2, end=" ")

#1 4 27 16 125.....
def Series6(N):
    for i in range(1, N+1):
        if i%2==0:
            print(i**2, end=" ")
        else:
            print(i**3, end=" ")

def num_series(series_type, N):
    if series_type=='1':
        natural_number(N)
    elif series_type=='2':
        Series2(N)
    elif series_type=='3':
        squares(N)
    elif series_type=='4':
        Series4(N)
    elif series_type=='5':
        Series5(N)
    elif series_type=='6':
        Series6(N)

series_type=input("Which series you want to print ? \nEnter '1' for 1 2 3 4 5....\nEnter '2' for 1 2 3 6 9 18 27 54...\nEnter '3' for"
                  "1 4 9 16 25..... \nEnter '4' for 1 2 9 4 25 6 49.....\nEnter'5' for 1 5 9 6 25 8 49 .....\nEnter '6' for 1 4 27 16 125.....\n:")
Number_Of_Elements=int(input("Enter the required number of elements :"))
num_series(series_type,Number_Of_Elements)


