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