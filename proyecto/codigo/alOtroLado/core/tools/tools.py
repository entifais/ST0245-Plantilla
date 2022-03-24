from collections import deque
import pandas as pd

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