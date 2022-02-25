import random
MAXBOXSIZE = 1024
MAXSIZE = 64
MINSIZE = 0

class MemoryBox:
    def __init__ (self,bizy:bool,size:int,process:str = None):
        # Занятость процесса
        self.bizy = bizy
        # Название процесса 
        if process != None:
            self.process = process
        else:
            self.process = None
        self.id = random.randint(1,255)
        # Условие для веса ячейки памяти
        if (size >= MINSIZE)and(size <= MAXSIZE):
            self.size = size
        else:
            print(f"Неверно указан вес памяти ячейки.\nДиапазон веса ячейки {MINSIZE} - {MAXSIZE}")
            raise MemoryError
        # Указатель на следующую ячейку памяти
        self.nextbox = None
        # Указатель на следующую ячейку памяти
        self.lastbox = None

    def change_name(self,newname):
        self.process = self.newname

class MemoryStorage:
    def __init__(self):
        self.head = None
    # Поиск содержится ли
    def contains (self, process):
        lastbox = self.head
        while (lastbox):
            if process == lastbox.process:
                return True
            else:
                lastbox = lastbox.nextbox
        return False
    # Добавление в конец
    def addToEnd(self,bizy,size,process):
        newmem = MemoryBox(bizy,size,process)
        
        if self.head is None:
            self.head = newmem
            return

        lastbox = self.head
        while (lastbox.nextbox):
            lastbox = lastbox.nextbox   
        lastbox.nextbox = newmem
    
    def chooseBox(self,choose):
        boxnow = self.head
        i = 0
        while i != choose:
            i += 1
            boxnow = boxnow.nextbox
        print("Выбран блок, id = <",boxnow.id,'>')
        


    def memory_generate(self):
        size_now = 0
        while size_now != MAXBOXSIZE:
            size_now += MAXSIZE
            newmem = MemoryBox(bizy = False,size = 0,process= None)
            if self.head is None:
                self.head = newmem
                continue
            lastbox = self.head
            while lastbox.nextbox:  
                lastbox = lastbox.nextbox
            lastbox.nextbox = newmem
        

    # Вывод всех элементов
    def StorageOut(self):
        data = self.head
        print("\tMemory")
        print("Зарезервированно : {} mb".format(MAXBOXSIZE))
        while data is not None:
            print ("=========================\n<{0}> {3}|{2}/{4}|{1}".format(data.id,data.bizy,data.size,data.process,MAXSIZE))
            data = data.nextbox

mem = MemoryBox(bizy = True,size = 32,process="A")
MemoryDisk = MemoryStorage()
# MemoryDisk.addToEnd(False,44,"B")
MemoryDisk.memory_generate()
MemoryDisk.StorageOut()
MemoryDisk.chooseBox(2)
print()
