import sys

def run():

    round = int(input())

    for i in range(round):
        gold_prime(int(input()))



def gold_prime(input):

    mid = int(input/2)

    for i in range(mid):
        if check_prime(mid-i) * check_prime(mid+i) == 1:
            print(str(mid-i) +' '+ str(mid+i))
            return 1
    else:
        print("There is no gold prime")
        return -1

    # # round = int(input())
    # #
    # # num_list = list(map(int, input().split(' ')))
    #
    # # print(num_list)
    #
    # start = int(input())
    # end = int(input())
    #
    # list=[]
    #
    # for i in range(start,end+1):
    #     if check_prime(i) == 1:
    #        list.append(i)
    #
    # # print(list)
    #
    # if len(list) == 0:
    #     print(-1)
    # else:
    #     print(sum(list))
    #     print(list[0])
    #
    # # sum = 0
    # #
    # # if len(num_list) == round:
    # #
    # #     for i in num_list:
    # #         sum += check_prime(i)
    # #
    # #     print(sum)



def check_prime(input):

    if input == 1:
        return 0

    for i in range(2,int(input/2 +1)):
        if input%i == 0:
            return 0

    return 1


if __name__== "__main__" :
    run()