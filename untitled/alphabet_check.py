

def run():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    my_dic={}

    for i in alphabet:
        my_dic[i]= -1

    input_data = input()

    check_list=[]

    for i in range(0,len(input_data)):
        if input_data[i] not in check_list:
            check_list.append(input_data[i])
            my_dic[input_data[i]] = i

    my_string = ''
    my_list=[]

    for i in alphabet:
        my_string += str(my_dic[i]) + ' '

    print(my_string)


if __name__ == "__main__":
    run()
