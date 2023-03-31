import time
# values = ['1', '2', '3']

# with open("heartbeat.txt", "w") as output:
#     output.write(str(values))


# print(values)
# using a json file

def update_hearbeat(data):

    current_time = time.time()
    # print('Current time: {0}'.format(current_time))

    f = open("heartbeat.txt", "r")
    aList = f.read()
    aList = aList.replace('', '').split(" ")
    a_dict = {}
    for i in aList:
        if i:
            a_dict[i.split(":")[0]] = i.split(":")[1]
    # data = 'server5'

    # a_set = set()
    a_dict[data] = str(time.time())
    # if data not in a_dict.keys():
    #     a_dict[data] = str(time.time())
    # else:
    #      a_dict[data] = str(time.time())

    write_list = []
    print('------------------')
    # print(write_list)
    for k, v in a_dict.items():
        # If the server didn't get the signal from the chunk servers, POWER OFF! means, drop the server in the list.
        if (current_time - float(v) > 20):
            print('SERVER down')
        else:
            write_list.append(k+':'+v)

    print(' '.join(write_list))  # make a string
    print(write_list)
    with open("heartbeat.txt", "w") as output:
        output.write(' '.join(write_list))


# If data is not comning any more, remove it from the list.
# Add timestamp?

# Java no dictionary
# every language has a string.
# json. is a string.
# json understand.
# json is string
