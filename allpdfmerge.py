import os
from PyPDF2 import PdfFileMerger
location = os.getcwd()
files_in_dir = []
for file in os.listdir(location):
    if file.endswith(".pdf") and not file.startswith("merged_PDF_AB"):
        files_in_dir.append (file)

print ("Merging PDF files in this order", files_in_dir)
merger = PdfFileMerger()

for pdf in files_in_dir:
    merger.append(pdf)

merger.write("merged_PDF_AB.pdf")
merger.close()
input ("Press Enter...")