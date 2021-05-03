class SolidQueue:
    def __init__(self,queue = list(),head=int(),tail=int()):
        self.queue = list(queue)
        self.head = int(head)
        self.tail = int(tail)
        self.queue[0] = 0
    
    def addin(self,arg,head,tail):
        if self.queue[0] == len(self.queue)-1:
            return("Ошибка")
        else:

