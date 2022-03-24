import time
from collections import deque
from io import StringIO  
strnomal=""
lstnomal=[]
lstnomal2=[]
strio=StringIO
nums=10000
def bech1(nums,d):
	start=time.time()
	for i in range(nums):
		d=d+str(i)
	end=time.time()
	print(end-start)
def bech2(nums,d):
	start=time.time()
	for i in range(nums):
		d.write(str(i))
	end=time.time()
	print(end-start)
def bech3(nums,d):
	start=time.time()
	for i in range(nums):
		d.append(i)
	end=time.time()
	print(end-start)
def bech4(nums,d):
	start=time.time()
	for i in range(nums):
		d.insert(i)
	end=time.time()
	print(end-start)
def bech5(nums,d):
	start=time.time()
	for i in range(nums):
		d.append(i)
	end=time.time()
	print(end-start)
def main()
	bech1()
	bech2()