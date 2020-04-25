import utility

def main():

    ############################### ENCODING ###############################

    sliding_window_size = 13
    look_ahead_size = 7
    imagePath = "test.jpg"
    encodedFile = "encoded.npy"

    utility.encode(sliding_window_size, look_ahead_size, imagePath, encodedFile)

    ############################### DECODING ###############################

    sliding_window_size = 13
    look_ahead_size = 7
    rows = 183  #height
    columns = 275 #width
    resultImage = "result.jpg"
    encodedFile = "encoded.npy"

    utility.decode(sliding_window_size,look_ahead_size,rows,columns,resultImage,encodedFile)


main()