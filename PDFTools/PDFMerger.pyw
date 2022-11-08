from PyPDF2 import PdfFileMerger
import os
pdfs = list(filter(lambda x: x.endswith('.pdf'), os.listdir('./'))) 
print(pdfs)

merger = PdfFileMerger()
[merger.append(pdf) for pdf in pdfs]    
os.makedirs('Merged',exist_ok=True)
merger.write("Merged/result.pdf")
merger.close()