f = open("demofile1.txt", "a") # Append to an existing file
f.write("The file will include more text..")
f.close()
f = open("demofile2.txt", "w") # Creating and writing to a new file
f.write("demofile2 file created, with this content in!")
f.close()