try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys


if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print("Pass filename to process")
    else:
        file_to_process = sys.argv[1]
        print("*************************************")
        print("Printing file contents of " + file_to_process)
        print("*************************************")
        print(pytesseract.image_to_string(Image.open(file_to_process)))
        print("*************************************")



