import ctypes

class Node(object):
    def __init__(self):
        self.node = {
            "recorder": None,
            "info": None,
            "index": 0,
            "next": None,
        }

    def info(self):
        return self.node["info"]
    def index(self):
        return self.node["index"]
    # def rec(self):
    #     return self.node["recorder"]
    # def next(self):
    #     return self.node["next"]

class Chain(Node):
    def init(self):
        self.node["recorder"] = id(self.node)
        return(self.node)
    
    def addnew(self,value):
        self.node["next"] = self.node["recorder"] 
        self.node["recorder"] = id(self.node)
        self.node = dict(self.node)
        self.node["info"] = value
        self.node["index"] += 1
        return self.node
    
    def removelast(self):
        val = ctypes.cast( self.node["next"],ctypes.py_object )
        print(' - ',val.value)
        # val2 = ctypes.cast( val.value["next"],ctypes.py_object )
        # print('сука - ',val2.value)
        # self.node["recorder"] = self.node["next"] 
        # self.node["info"] = val.value["info"]
        # val_back = ctypes.cast( val.value["next"],ctypes.py_object )
        # print(val_back.value)
        # self.node["next"] = val.value["next"]
        # self.node["index"] -= 1
        # return self.node
    
    # def readall(self):
    #     val = ctypes.cast( self.node["recorder"],ctypes.py_object )
    #     while val.value["index"] != 0:
    #         val = ctypes.cast( self.node["recorder"],ctypes.py_object )
    #         self.node["recorder"] = self.node["next"]
    #         print(val)
new = Chain()
print(new.init())
print(new.addnew(2))
print(new.addnew(8))
print(new.removelast())
# new.addnew(32)
# print(new.readall())


# ctypes.cast(id1,ctypes.py_object))