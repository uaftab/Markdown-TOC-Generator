# Table of contents generator
import sys
toc = ""
delimiter = "#"
insertion = "- "
linkappend = str(sys.argv[2])

with open(sys.argv[1],'r') as fh:
  filecontents = fh.readlines()
  for line in filecontents:
    if line.find(delimiter)==0:
      pos = line.rfind(delimiter)
      line = line.replace(delimiter," ")
      link = line.lower()
      link = link.lstrip()
      link = link.replace(" ","-")
      link = "".join(char for char in link if (char.isalnum() or char is "-"))
      link = linkappend+"#"+link
      indentation = ""
      for i in range(pos):
        indentation += " "
      md = indentation+insertion+"["+line.lstrip().rstrip()+"]"+"("+link+")"

      toc = toc + (md+"\n")


print (toc)
