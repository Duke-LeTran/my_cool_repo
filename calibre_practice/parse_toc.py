#!/home/dletran/anaconda3/bin/python
import sys

# Testing of args
#print("The name of the script is: ", sys.argv[0])
#print("Number of arguments: ", len(sys.argv))
#print("The arguments are: ", str(sys.argv))
#print(type(sys.argv))

print(f"Now running {sys.argv[0]} script on file {sys.argv[1]}...")

# This parses the toc for the content
with open(sys.argv[1]) as f:
	data = [x.strip().strip('<text>').strip('</') for x in f.readlines() if \
	('<text>' in x) and ('Answers' not in x)]

# This prints to a text file for post-parse manipulation
with open('toc_output.txt', 'w') as f:
	for line in data:
		f.write(line + '\n')
	print("Success.")
