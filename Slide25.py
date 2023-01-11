name = open("filename", "w")  # write new
name = open("filename", "a")  # append

out = open("text/output.txt", "w")
out.write("Hello, world!\n")
out.write("How are you?")
out.close()
text = open("text/output.txt").read()
print(text)
