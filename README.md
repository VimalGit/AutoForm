# AutoForm

## Sample project folder structure

--firstocr.py<br>
--\input<br>
----bankletter.jpg<br>
--\output<br>
----bankletter.txt (This will be generated from program)<br>

The main code is firstocr.py
The input images are stored in "input" directory.
The scanned image's output text file is stored in "output" directory.

### Usage:

In command line type

`python firstocr.py input/bankletter.jpg`

The program will run and read the input image and scan using Tesseract. Then it will ask for output file name. Just give file name without any folder or extension. 
eg. bankletter

This will save the scanned image in the "output" folder under the name "bankletter.txt"

### Example:


![image](https://user-images.githubusercontent.com/5920239/127966984-bbdbc032-5cb4-4a1c-9457-a177c869f4f4.png)

