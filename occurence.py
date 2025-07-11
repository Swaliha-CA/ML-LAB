s=input("enter a sentence:")
word=s.split()
occurence={}
for w in word:
	if w in occurence:
		occurence[w]=occurence[w]+1
	else:
		occurence[w]=1
print("word occurence")
for w,count in occurence.items():
	print(f"{word}:{count}")
	
