# Image Compression
## using LZ77
- Author: Saad Eldeen Mohamed Mohamed
- SEC: 1
- BN: 28
------------
#### User interaction files:
------------
There is two options for user to use this program:
1. Run **consoleUser.py**
	- The program will run and take the needed input from the user from console during running.
2. Run **main.py**
	- Before running user should enter the data manualy in **main.py** then run it.

- **Note**: User shouldn't interact with (utility.py, LZ77.py) files.

------------

#### **consoleUser.py** modes:
------------
There is three modes and the user will be asked to choose one from them after running **consoleUser.py**
1. Encode then Decode the same files
2. Encode only
3. Decode only
------------
#### The program input:
------------
1. Encoding:
    - Sliding window size
    - Look Ahead buffer size
	- Image name (e.g. test.png)
	- Output encoded file name (e.g. encoded.npy)
2. Decoding:
    - Sliding window size
    - Look Ahead buffer size
    - Input encoded file name (e.g. encoded.npy)
	- Width of the original image in pixels (e.g. 256)
	- Height of the original image in pixels (e.g. 256)
	- Output image name (e.g. result.png)
------------
#### The program output:
------------
1. Encoding:
	- original.npy
		- The original image data before encoding
	- The encoded file (e.g. encoded.npy)
2. Decoding:
	- Resulted Image (e.g. result.png)


