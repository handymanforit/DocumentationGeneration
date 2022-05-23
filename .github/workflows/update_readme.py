import sys
import os

class CIHelper:
  def __init__(self,
			    readmetemplatefilename,
			    coveragefilename,
                readmefilename,
                branchname,
                owner_reponames,
                workflowfilename):
            self.readmetemplatefilename = readmetemplatefilename
            self.coveragefilename = coveragefilename
            self.readmefilename = readmefilename
            self.branchname = branchname
            self.owner_reponames = owner_reponames
            self.workflowfilename = workflowfilename
  
  def update_test_coverage(self):
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

  def insert_in_between(self,targetstring,startstring,endstring,stringinsert):
    startindex = targetstring.index(startstring) + len(startstring)
    endindex = targetstring.index(endstring)
    
    newdata = targetstring[0:startindex]
    newdata = newdata + "\n\n" + stringinsert + "\n\n" + targetstring[endindex:]
    
    return newdata
  
  def delete_in_between(self,targetstring,startstring,endstring):
    startindex = targetstring.index(startstring) + len(startstring)
    endindex = targetstring.index(endstring)
    
    newdata = targetstring[0:startindex]
    newdata = newdata + "\n\n" + targetstring[endindex:]
    
    return newdata
  
  def delete_between(self,targetstring,startstring,endstring):
    startindex = targetstring.index(startstring)
    endindex = targetstring.index(endstring) + len(endstring)
    
    newdata = targetstring[0:startindex]
    newdata = newdata + "\n\n" + targetstring[endindex:]
    
    return newdata
  
  
  def update_readme(self):
    startindexstring = "[comment]: <> (coverage details start)"
    endindexstring = "[comment]: <> (coverage details end)"
    
    start_build_status_string = "[comment]: <> (build status start)"
    end_build_status_string = "[comment]: <> (build status end)"
    
    newdata = self.update_readme_code_coverage()
    newdata = self.update_build_status_summary(newdata)
    
    text_file = open(readmefilename,"r", encoding='utf-8')
    
    readmedata = text_file.read()
    
    text_file.close()
    
    if startindexstring in readmedata:
    readmedata = self.delete_between(readmedata,startindexstring,endindexstring)
    
    if start_build_status_string in readmedata:
    readmedata = self.delete_between(readmedata,start_build_status_string,end_build_status_string)
    
    readmedata = newdata + "\n\n" + readmedata
    
    text_file = open(readmefilename,"w", encoding='utf-8')
    text_file.write(readmedata)
    text_file.close()
    
    
  def update_readme_code_coverage(self):
    startindexstring = "[comment]: <> (coverage details start)"
    endindexstring = "[comment]: <> (coverage details end)"
    
    text_file = open(self.readmetemplatefilename, 'r', encoding='utf-8')
    data = text_file.read() 
    
    covfile = open(self.coveragefilename, 'r', encoding='utf-8')
    covdata = covfile.read()
    
    newdata = self.insert_in_between(data,startindexstring,endindexstring,covdata)
    
    text_file.close()
    covfile.close()
    
    return newdata
  
  def update_build_status_summary(self,datastring):
    datastring = datastring.replace("<branch_name>",self.branchname)
    datastring = datastring.replace("<OWNER>/<REPOSITORY>",self.owner_reponames)
    datastring = datastring.replace("<WORKFLOW_FILE>",self.workflowfilename)
    return datastring
  
readmetemplatefilename = sys.argv[1] #"readme_template.md";
coveragefilename = sys.argv[2]#"code-coverage.md";
readmefilename = sys.argv[3] #"readme.md"
branchname = sys.argv[4] # main
owner_reponames = sys.argv[5] # handymanforit/DocumentationGeneration
workflowfilename = sys.argv[6] # ci-build.yml
p1 = CIHelper(readmetemplatefilename,
                coveragefilename,
                readmefilename,
                branchname,
                owner_reponames,
                workflowfilename)
p1.update_readme()
