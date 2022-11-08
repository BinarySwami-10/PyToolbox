import os
import filecmp
import glob

def bulkcmp(d1,d2,glob1='',glob2=''):

	os.chdir(d1)
	globlist1=set (glob.glob(glob1))

	os.chdir(d2)
	globlist2=set (glob.glob(glob2))

	comm=set(globlist1) & set(globlist2)
	diff=set(globlist1) ^ set(globlist2)
	print(diff)

	for x in globlist1:
		f1=d1+x
		f2=d2+x
		try:
			data1=open(f1,'rb').read()
			data2=open(f2,'rb').read()
			if data1!=data2:
				print(False,x)
		except Exception as e:
			# print('err in file',x)
			...

	# [print(x) for x in globPatternA]



if __name__ == '__main__':
	a=r"C:\GAMES\Galactic Civilizations III\data"+'\\'
	b=r"C:\GAMES\Galactic Civilizations III (new)\data"+'\\'

	bulkcmp(a,b,glob1='../*/*',glob2='../*/*')
	# print(len(globPatternA),len(globPatternB))
	# for a,b in zip(globPatternA , globPatternB):
		# print(a,b)