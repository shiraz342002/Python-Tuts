# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x): This mode creates a file and gives an error if the file already exists.
# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b): used to handle binary files (images, pdfs, etc).

##Imp note move the files outside of current folder cuz they were not working for some reason

##Reading a file
# f = open('D:\Coding With Shiraz\Python\hello.txt', 'a')
# contents = f.read()
# print(contents)
# f.close()  # Make sure to close the file after reading

##Writing a file

# f = open('D:\Coding With Shiraz\Python\hello_write.txt', 'w')
# f.write(" xD Yo you can write in a file from a freaking Ide That's awsome")
# f.close()

##Appending a file
# f = open('D:\Coding With Shiraz\Python\hello_write.txt', 'a')
# f.write(" xD Yo you can write in a file from a freaking Ide That's awsome")
# f.close()

## with canb used if you dont want to close it you fucking nerd
# with open('hello_write.txt', 'r') as f:
#   text=f.read()
#   print(text)
