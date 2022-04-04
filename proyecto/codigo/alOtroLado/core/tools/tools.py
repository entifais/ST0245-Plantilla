import os
def writetxt(name,content):
  """
  writetxt(name,content) , write in txt file something  
  """
  content=str(content)
  with open(name, "w") as file:
    file.write(content)
    file.close()

def readtxt(name):
  """
  readtxt(name) , return txt content as array ,element by line 
  """
  content = []
  with open(name, 'r') as file:
    for i in file.readlines():
      content.append(str(i).replace("\n",""))
  return content

def joinWebpage(direccions,webApp,actualapp,url=""):  
    for webroute in direccions:   
      @actualapp.route(url+webroute, endpoint=webroute , methods=['GET','POST'])
      def site():
        return webApp
    return site()

def genPreview(name,path="",salt="genMaps"):
  txt = f'\n\t@app.route("/{salt}/{name}")\n\tdef {str(name[:-5]).replace("/","")}():\n\t\treturn render_template("{salt}/{name}")'
  return txt

def initMap(dataDir):
    newCode = """from flask import Flask, render_template
app = Flask(__name__)
class maps():"""
    writetxt(dataDir,newCode)
    #tryng to move to emacs is ... a disasters with tabs 

def filesInFolders(path,tag = ".html"):
  folderFiles = os.listdir(path)
  files = []
  for i in folderFiles:
    if i[len(tag)*-1:] != tag:
      name =  [i+"/"+ii for ii in os.listdir(path+i)] 
      files += name
    else: 
      files +=  [i]
  return files

def blogsNames(path,tag = ".html"):
  blogs = os.listdir(path)
  names = []
  for i in blogs:
    if i[len(tag)*-1:] == tag:
      names.append(i[:len(tag)*-1])
    else:
      names.append(i)
  return names
def validData(txt,dicts):
  tmp=False
  for i in txt:
    print(i, not i in dicts)
    if not i in dicts:
      print("no pasa")
      tmp=False
      break
    else:
      print("pasa")
      tmp=True
  return tmp
#a in "asdf" yes, not flase, 1 in "asdfgh" ,no