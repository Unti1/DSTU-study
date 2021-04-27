import heapq

class SolidStack: # Сплошное представление
    def __init__(self,lys=list()):
        self.lys = lys
        self.index = 0    
    
    def addit(self,arg,index = int()):
        if index == len(self.lys):
            return('ОШИБКА')
        else:
            index += 1
            self.lys.insert(index,arg)
            return(self.lys)
    
    def deleteit(self,index = int()):
        if index == 0:
            return("ОШИБКА")
        else:
            self.lys.remove(self.lys[index])
            index -= 1
            return(self.lys)

#Пример вывода стека
MySolidStack = SolidStack([4,5,6])
print('--Сплошное представление стека--')
print("Добавление элемента в стек : ",MySolidStack.addit('s',1))
print("Удаление из стека 1 : ",MySolidStack.deleteit(1))


class ChainStack: # Цепное представление
    def __init__(self,lys=list()):
        self.lys = lys
        self.top = 0
        self.ukaz = 0
    
    def create(self,ind):
        self.ukaz = ind

    def addnew(self,value):
        self.lys.insert(self.top,None)
        self.lys[self.top] = value
        return(self.lys)
    
    def removelast(self,error = False):
        if self.ukaz != 0 :
            info = self.lys[self.ukaz]
            self.ukaz -= 1
            return(info)
        else:
            error = True
            return("Стек пустой",error)
    
    def last(self,error = False):
        if self.top == self.ukaz:
            print('Стек пуст')
            error = True
            exit(-1)
        else:
            return('Вершина - ', self.lys[self.ukaz])

    def readall(self):
        while self.top != self.ukaz:
            print(self.lys[self.top])
            self.top += 1
        
print('--Цепное представлени стека--')
MyChainStack = ChainStack([1,2,3,4,4,5])
MyChainStack.create(6)
print("Добавленеи элемента в конец : ",MyChainStack.addnew(2))
print("Выбор(удаление) из стека последнего элемента : ",MyChainStack.removelast())
print("Считывание последнего элемента :",MyChainStack.last())
print("Считывание всех элементов в стеке : ")
MyChainStack.readall()

