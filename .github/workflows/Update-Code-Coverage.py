import sys
import os

class CIHelper:
  def __init__(self,
			    readmetemplatefilename,
			    coveragefilename):
            self.readmetemplatefilename = readmetemplatefilename
            self.coveragefilename = coveragefilename
  
  def updatetestcoverage(self):
    startindexstring = "[comment]: <> (coverage details start)"
    endindexstring = "[comment]: <> (coverage details end)"
    text_file = open(readmetemplatefilename, 'r', encoding='utf-8')
    data = text_file.read()
    startindex = data.index(startindexstring) + len(startindexstring)
    endindex = data.index(endindexstring)
    text_file.close()
    
    covfile = open(coveragefilename, 'r', encoding='utf-8')
    covdata = covfile.read()
    
    newdata = data[0:startindex]
    newdata = newdata + "\n\n" + covdata + "\n\n" + data[endindex:]
    
    text_file = open(readmetemplatefilename,"w", encoding='utf-8')
    text_file.write(newdata)
    text_file.close()

readmetemplatefilename = sys.argv[1]; #"readme.md";
coveragefilename = sys.argv[2]#"code-coverage.md";
p1 = CIHelper(readmetemplatefilename,coveragefilename)
p1.updatetestcoverage()
