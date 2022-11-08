'''
WORKS BETTER FOR IMAGE PDF BOOKS
PLEASE TRY PDF TEXT READER IF THE CONTENT OF UR PDF ARE TEXT
SINCE THIS PROGRAM CONVERTS INDIVIDUAL PAGES TO IMAGES AND READS TEXT
'''
import modulex as mx
from PIL import Image
import os
import pytesseract
from pytesseract import image_to_string
from pdf2image import convert_from_path 
import multiprocessing as mp

popplerpath='.\\poppler-0.67.0\\bin'
os.environ["PATH"] += os.pathsep + popplerpath
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

def split_pdf(path):
	from PyPDF2 import PdfFileWriter, PdfFileReader
	inputpdf = PdfFileReader(open(path, "rb"))
	for i in range(inputpdf.numPages):
	    output = PdfFileWriter()
	    output.addPage(inputpdf.getPage(i))
	    with open(f"./my_pdfs/workjob/p{i}.pdf", "wb") as outputStream:
	        output.write(outputStream)

def get_text_from_pdf(iterpath):
	global txtpath
	pages = convert_from_path(iterpath,200)
	for page in pages:
		text=image_to_string(page)
		os.remove(iterpath)
		if len(text.split()) < 30: return '\nPAGE SKIP < 30 WORDS\n'
		mx.fappend(f'{txtpath}',text)

	mx.fappend('logs.txt',f'Processed {iterpath}')

def list_files_by_time(folder):
	jobFileQueue=[folder+x for x in os.listdir(folder)]
	jobFileQueue.sort(key=os.path.getmtime)
	return (jobFileQueue)



#DECLARE FILE CONSTANTS
path='my_pdfs/DIP MAIN.pdf'
txtpath =path+'.txt'

if __name__ == '__main__':
	'''DO THIS ONLY ONCE PER PDF
	split_pdf(path); os.remove(txtpath)
	'''
	currentJobs=list_files_by_time('my_pdfs/workjob/')	# print(currentJobs) abs Path from current folder

	POOL=mp.Pool(4)
	x=POOL.map(get_text_from_pdf,currentJobs,chunksize=1)
