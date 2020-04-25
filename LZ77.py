import numpy as np

def getToken(sliding_window_data, look_ahead_size):

    token = [0, 0, 0]
    # index of the 1st element in look ahead buffer
    look_ahead_index = len(sliding_window_data) - look_ahead_size;
    token[2] = sliding_window_data[look_ahead_index]
    # loop starting from the element before look ahead "the 1st one in our search buffer"
    # till 0 "last element in search buffer"

    for i in range(look_ahead_index-1, -1, -1):
        j = i
        k = look_ahead_index
        temp = [look_ahead_index - i, 0]
        while k+1<len(sliding_window_data) and sliding_window_data[k] == sliding_window_data[j]:
            j += 1
            k += 1

        temp[1] = k - look_ahead_index

        if temp[1] > token[1]:
            token = temp + [sliding_window_data[k]]

    return token


def encode(sliding_window_size, look_ahead_size,data):

    # sliding_window_limits = [0, sliding_window_size - 1]
    # sliding_window_size = 13
    # look_ahead_size = 6
    output = np.array(data[0:look_ahead_size-1])
    while sliding_window_size <= len(data):
        sliding_window_data = data[:sliding_window_size]
        token = getToken(sliding_window_data, look_ahead_size)
        data = data[1 + token[1]:]
        output = np.append(output, token)
        x = sliding_window_size - len(data)
        if x > 0:
            data = np.append(data, [0]*x)
        x = [0]*sliding_window_size
        if(np.array_equal(data,x)):
            break
    return output


# encode(13,6,["a","d","a","c","a","d"])


def resolveToken(sliding_window_data, token):

    # start_index = len(sliding_window_data) - look_ahead_size + 1 - token[0];
    original_length = len(sliding_window_data)
    start_index = len(sliding_window_data) - int(token[0]);
    for i in range(0,int(token[1])):
        sliding_window_data = np.append(sliding_window_data,sliding_window_data[i+start_index])
    sliding_window_data = np.append(sliding_window_data,token[2])
    return sliding_window_data[original_length:]


def decode(search_buffer, tokens):
    data = search_buffer
    search_buffer_size = len(search_buffer)
    # search_buffer = data
    # tokens = [0, 0, 'd', 7, 4, 'r', 3, 5, 'd']

    for i in range(0, int(len(tokens)),3):
        data = np.append(data, resolveToken(data[len(data)-search_buffer_size:],tokens[i:(i+3)]))
    return data
