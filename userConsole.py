import utility


def main():

    ########################################### ENCODING ##########################################################

    mode = int(input("please choose mode:\n1.Encode then Decode the same files\n3.Encode only\n3.Decode only\n"))
    sliding_window_size = int(input("Sliding Window Size = (e.g. 12) "))
    look_ahead_size = int(input("Look Ahead Buffer Size = (e.g. 6) "))

    if mode != 3:
        imagePath = input("image name: (e.g. test.png) ")
        # name of the encoded file that will be created
        encodedFile = input("output encoded file name: (e.g. encoded.npy) ")
        # name of the file to save the probability 1D numpy array in it
    if mode == 2:
        utility.encode(sliding_window_size, look_ahead_size, imagePath, encodedFile)
        return
    ########################################### DECODING ##########################################################
    columns = int(input("number of columns (WIDTH) of the original image: (e.g. 256) "))
    rows = int(input("number of rows (HEIGHT) of the original image: (e.g. 256) "))
    resultImage = input("output image name: (e.g. result.png) ")
    # name of the encoded file to be decoded
    if mode == 3:
        encodedFile = input("encoded file name: ( e.g. encoded.npy) ")
    elif mode == 1:
        utility.encode(sliding_window_size, look_ahead_size, imagePath, encodedFile)
    utility.decode(sliding_window_size,look_ahead_size,rows,columns,resultImage,encodedFile)


main()
