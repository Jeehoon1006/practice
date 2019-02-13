import sys


def run():

    round = int(input())
    list=[]

    for i in range(round):
        data=input()
        list.clear()
        check=1
        # list = list(map(str,input().split()))
        for i in data:
            # print("input=",i)
            if i =='(':
                list.append(1)

            elif i == ')':
                if(len(list)==0):
                    check=0
                    # print("error")
                    continue

                else:
                    # print(list)
                    list.pop()

        if len(list) == 0 and check == 1:
            print("YES")
        else:
            print("NO")

        # print(list)



# def check()


    # list = []
    #
    # for i in range(round):
    #
    #     get_command(list)
    #


def get_command(list):
    input_data = input().split(' ')
    # print(input_data)
    # print(input_data[0])

    if input_data[0] == 'push':
        # print("push")
        # print(input_data[1])
        list.append(int(input_data[1]))

    elif input_data[0] == 'pop':
        # print("pop")
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])
            list.pop()

    elif input_data[0] == 'size':
        # print('size')
        print(len(list))

    elif input_data[0] == 'empty':
        # print('empty')
        if len(list) == 0:
            print(1)
        else:
            print(0)

    elif input_data[0] == 'top':
        # print("top")
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])

    else:
        print('Command error')

    return list


if __name__=="__main__":
    run()