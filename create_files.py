import helperLibrary as h
import os


if not os.path.exists("./files"):
    os.makedirs("./files")
if not os.path.exists("./files/size1"):
    os.makedirs("./files/size1")
if not os.path.exists("./files/size2"):
    os.makedirs("./files/size2")
if not os.path.exists("./files/size3"):
    os.makedirs("./files/size3")
if not os.path.exists("./files/size4"):
    os.makedirs("./files/size4")


for i in range(10):
    h.createTestFile("./files/size1/file{}.txt".format(i),10000,100)
for i in range(10):
    h.createTestFile("./files/size2/file{}.txt".format(i),10000,1000)
for i in range(10):
    h.createTestFile("./files/size3/file{}.txt".format(i),100000,10000)
for i in range(10):
    h.createTestFile("./files/size4/file{}.txt".format(i),100000,100000)
