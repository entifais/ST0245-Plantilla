import os
def writetxt(name,content,mode="w"):
  """
  writetxt(name,content) , write in txt file something  
  """
  content=str(content)
  with open(name, mode) as file:
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
    
def genPreview(name,path):
  txt = f'\n\t@app.route("/{name}")\n\tdef {str(name[:-5]).replace("/","")}():\n\t\treturn render_template("{path}/{name}")'
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
    if not i in dicts:
      tmp=False
      break
    else:
      tmp=True
  return tmp
def doCallBacks(funcs,args):
    print(funcs,args)
    for f,i in zip(funcs,range(len(funcs))):
      print(f,args[i])
      f(args[i])
      print("gencallback")
def do2CallBacks(f1,f2,args1,args2):
    f1(args1[0],args1[1],args1[2])
    f2(args2[0],args2[1])

"""docstring description
        :param arg: parametro
        :type arg:tipo del argumento
        :return: retorno
        :rtype: (tipo de dato al retonar)
"""
