from typing import Any


class SolidStack: # Сплошное представление
    def __init__(self,lys=list()):
        self.lys = lys
        self.index = 0    
    
    def create(self,lys=list()):
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
        
    def create(self,lys=list()):
        self.lys = lys
        return(lys)
    
    def push(self,value):
        self.lys.append(value)
        return(self.lys)
    
    def pop(self):
        if self.lys != []:
            item = self.lys.pop()
            return(item)
        else:
            return("Стек пустой")
    
    def readlast(self):
        return(self.lys[-1])

    def readall(self):
        for i in self.lys[::-1]:
            print(i)
        return
print('--Цепное представлени стека--')
MyChainStack = ChainStack([1,2,3])
print("Добавленеи элемента в конец : ",MyChainStack.push(2))
print("Выбор из стека последнего элемента : ",MyChainStack.pop())
print("Считывание последнего элемента :",MyChainStack.readlast())
print("Считывание всех элементов в стеке : ")
MyChainStack.readall()

