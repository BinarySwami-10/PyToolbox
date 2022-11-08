def images_to_pdf(folder,imgFormat='png',outFileName='output.pdf'):
	# images_to_pdf('test/') #----->USAGE
	from PIL import Image ; import os
	if folder.endswith('/'): pass
	else: print("please enter folder path with forwardslash /") ;return

	print("Starting merge Procedure")
	imgarr=[Image.open(f'{folder}{x}') for x in os.listdir(folder)]
	imgarr[0].save(outFileName, "PDF" ,resolution=100.0, save_all=True, append_images=imgarr[1:-1])
