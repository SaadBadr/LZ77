import LZ77 as e
import cv2
import numpy


def encode(sliding_window_size, look_ahead_size, imagePath="test.jpg", encodedFile="encoded"):
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE).flatten()
    codes = numpy.array([])
    print("Encoding Started")
    numpy.save('original.npy', img)
    codes = e.encode(sliding_window_size,look_ahead_size, img)
    print("Encoding Done:")

    integer_type = 'uint64'

    if sliding_window_size < 256:
        integer_type = 'uint8'
    elif sliding_window_size < 65536:
        integer_type = 'uint16'
    elif sliding_window_size < 4294967296:
        integer_type = 'uint32'

    numpy.save(encodedFile, codes.astype(integer_type)) # save

    print(" ->" + encodedFile + " is created")

    return codes


def decode(sliding_window_size,look_ahead_size, rows, columns, resultImage="result.jpg", encodedFile="encoded.npy"):
    codes = numpy.load(encodedFile)
    # codes2 = numpy.load('original.npy')
    # lastexcluded = codes[-1] + 1
    # print(lastexcluded)
    # end = codes[len(codes)-lastexcluded:len(codes)-1]
    # codes = codes[0:len(codes)-lastexcluded]

    print("Decoding Started")
    img = e.decode(codes[0:sliding_window_size-look_ahead_size], codes[sliding_window_size-look_ahead_size:])
    print("Decoding Done:")
    # for i in range(0, 50320):
    #     print(img[i], codes2[i])
    img = img[:rows * columns]
    img = img.reshape(rows, columns)
    cv2.imwrite(resultImage, img)
    print(" ->" + resultImage + ' is created\n')


# decode(13,6,0,0)
# codes = numpy.array(['c', 'a', 'b', 'r', 'a', 'c', 'a', 0, 0, 'd', 7, 4, 'r', 3, 5, 'd'])
