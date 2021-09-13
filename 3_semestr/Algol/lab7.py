class SolidQueue:
    def __init__(self,queue = list(),head=int(),tail=int()):
        self.queue = list(queue)
        self.head = 1
        self.tail = 1
        self.queue[0] = 0
    
    def addin(self,arg):
        if self.queue[0] == len(self.queue)+1:
            return("Ошибка")
        else:
            self.queue[self.tail] = arg
            self.tail += 1
            self.queue[0] += 1
        if self.tail == len(self.queue + 1):
            self.tail = 1

    def remove(self):
        if self.queue[0] == 0:
            return("ОШИБКА")
        else:
            self.head += 1
            self.queue[0] += 1