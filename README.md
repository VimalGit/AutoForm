# AutoForm

Sample project folder structure

--firstocr.py
--\input
----inputfile.jpg
--\output
----outputfile.txt

The main code is firstocr.py
The input images are stored in "input" directory.
The scanned image's output text file is stored in "output" directory.

Usage:

In command line type

python firstocr.py input/bankletter.jpg

The program will run and read the input image and scan using Tesseract. Then it will ask for output file name. Just give file name without any folder or extension. 
eg. formswetha

This will save the scanned image in the "output" folder under the name "formswetha.txt"
