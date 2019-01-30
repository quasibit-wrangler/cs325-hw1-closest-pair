import helperLibrary as h



for i in range(10):
    h.createTestFile("./files/size1/file{}.txt".format(i),100,100)
for i in range(10):
    h.createTestFile("./files/size2/file{}.txt".format(i),1000,1000)
for i in range(10):
    h.createTestFile("./files/size3/file{}.txt".format(i),1000,10000)
for i in range(10):
    h.createTestFile("./files/size4/file{}.txt".format(i),1000,100000)
