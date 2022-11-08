import fileinput
import time
 #THIS PROGRAM CONVERTS ALL WORDS TO WORD COUNTS.. STREAM THEM TO DESIRED OUTPUT
filename = 'text.txt'
file = open(filename, 'rt')
text = file.read()
para=''

wordtokens=[]
def p(a,*args):
	print(a,*args,sep='_')
def checker(needle,haystack):
	return needle in haystack
def content(biglist):
	# this concatenates all the words in our text one by one
	global para
	global wordtokens
	for i in biglist:
		if (i != ''):
			para=para+i+' '
			wordtokens.append(i)

# timer=time.monotonic_ns()
splitted=text.split()
for i in range(0,len(splitted)):
	check = checker('00',splitted[i]) or checker('--',splitted[i]) 
	# store in vector array
	if (check==True):
		splitted[i]=''
		splitted[i-1]=''

content(splitted)

vectormap=[]
repeatmap=[]

b=0
for i in range (len(wordtokens)):
	try:
		a=vectormap.index(wordtokens[i])
		repeatmap[a]+=1
		pass

	except ValueError :

		vectormap.append(wordtokens[i])
		repeatmap.append(1)
word_occurences=[]
for i in range(len(vectormap)):
	word_occurences.append((vectormap[i],repeatmap[i]))


p(len(vectormap),len(wordtokens),len(repeatmap))
for i in range(len(word_occurences)) : p(word_occurences[i][0],word_occurences[i][1]);
# p('total time',(time.monotonic_ns()-timer)/10**6,'millisec' )


# file = open('boos23w.txt','w+')
# file.write("asdffff")

