 #****************************************************************************************
 #***                                                                                  ***
 #***  Date: 29/8/2023  Time: 4:23 Pm     Author:  Shiraz Mazhar                       ***
 #***                                                                                  ***
 #***  Working On :  Merging pdf file                                                  ***
 #***                                                                                  ***
 #****************************************************************************************

from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("new_shiraz.pdf")
merger.close()