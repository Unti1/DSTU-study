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




print('--Цепное представлени стека--')
# MyChainStack = ChainStack([1,2,3,4,5])
# MyChainStack.create(len(MyChainStack.lys))
el = 90
# print(f"Добавленеи элемента {el} в конец : ",MyChainStack.addnew(el))
# print("Выбор(удаление) из стека последнего элемента : ",MyChainStack.removelast())
# print("Считывание конечного элемента :",MyChainStack.last())
# print("Считывание всех элементов в стеке : ")
# MyChainStack.readall()
