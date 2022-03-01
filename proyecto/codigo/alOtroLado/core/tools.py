def writetxt(name,content):
  """
  writetxt(name,content) , write in txt file something  
  """
  content=str(content)
  with open(name, "w") as file:
    file.write(content)
    file.close()
