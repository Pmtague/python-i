"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open('/Users/pmtag/Documents/python-i/src/foo.txt') as f:
	read_foo = f.read()
	print(read_foo)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

b = open('/Users/pmtag/Documents/python-i/src/bar.txt', 'w+')
b.write("Python is fantastic! \r\nBut I am so sleepy \r\nI think I'll do this later")
b.close()

with open('/Users/pmtag/Documents/python-i/src/bar.txt') as b:
	read_bar = b.read()
	print(read_bar)