import utility

def main():

    ############################### ENCODING ###############################

    sliding_window_size = 12
    look_ahead_size = 7
    imagePath = "test2.png"
    encodedFile = "encoded.npy"

    utility.encode(sliding_window_size, look_ahead_size, imagePath, encodedFile)

    ############################### DECODING ###############################

    sliding_window_size = 12
    look_ahead_size = 7
    rows = 256  #height
    columns = 256 #width
    resultImage = "result2.png"
    encodedFile = "encoded.npy"

    utility.decode(sliding_window_size,look_ahead_size,rows,columns,resultImage,encodedFile)


main()