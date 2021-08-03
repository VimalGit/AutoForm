try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys
import os


if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print("Pass filename to process")
    else:
        file_to_process = sys.argv[1]

        print("*************************************")
        print("Scanning file " + file_to_process)
        print("*************************************")

        scanned_text = pytesseract.image_to_string(Image.open(file_to_process))

        out_file = input("Enter output file name...")
        output_file_path_and_name = os.path.join("output", out_file+".txt")

        out_file = open(output_file_path_and_name, "w+")
        out_file.write(scanned_text)
        out_file.close()





