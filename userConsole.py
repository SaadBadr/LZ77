import utility


def main():

    ############################### ENCODING ###############################
    mode = int(input("please choose mode:\n1.Encode then Decode the same files\n2.Encode only\n3.Decode only\n"))
    sliding_window_size = int(input("Sliding Window Size = (e.g. 13) "))
    look_ahead_size = int(input("Look Ahead Buffer Size = (e.g. 7) "))
    if mode != 3:
        imagePath = input("image name: (e.g. test.png) ")
        encodedFile = input("output encoded file name: (e.g. encoded.npy) ")

    if mode == 2:
        utility.encode(sliding_window_size, look_ahead_size, imagePath, encodedFile)
        return
    ############################### DECODING ###############################

    columns = int(input("number of columns (WIDTH) of the original image: (e.g. 256) "))
    rows = int(input("number of rows (HEIGHT) of the original image: (e.g. 256) "))
    resultImage = input("output image name: (e.g. result.png) ")
    if mode == 3:
        encodedFile = input("encoded file name: ( e.g. encoded.npy) ")
    elif mode == 1:
        utility.encode(sliding_window_size, look_ahead_size, imagePath, encodedFile)
    utility.decode(sliding_window_size,look_ahead_size,rows,columns,resultImage,encodedFile)



main()
