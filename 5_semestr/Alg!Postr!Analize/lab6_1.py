class Node(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=0
class AVL_Tree(object):

    def __init__(self):
        self.root=None
    
    def find(self,key):
        if self.root is None:
            return None
        else:
            return self._find(key,self.root)
    
    def _find(self,key,node):
        if node is None:
            return None
        elif key<node.key:
            return self._find(key,self.left)
        elif key>node.key:
            return self._find(key,self.right)
        else:
            return node
    
    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)
    def _findMin(self,node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node
    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)
    def _findMax(self,node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    
    def height(self,node):
        if node is None:
            return -1
        else:
            return node.height
    
    def singleLeftRotate(self,node):
        k1=node.left
        node.left=k1.right
        k1.right=node
        node.height=max(self.height(node.right),self.height(node.left))+1
        k1.height=max(self.height(k1.left),node.height)+1
        return k1
    
    def singleRightRotate(self,node):
        k1=node.right
        node.right=k1.left
        k1.left=node
        node.height=max(self.height(node.right),self.height(node.left))+1
        k1.height=max(self.height(k1.right),node.height)+1
        return k1
    
    def doubleLeftRotate(self,node):
        node.left=self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)
   
    def doubleRightRotate(self,node):
        node.right=self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)
    
    def put(self,key):
        if not self.root:
            self.root=Node(key)
        else:
            self.root=self._put(key,self.root)
    
    def _put(self,key,node):
        if node is None:
            node=Node(key)
        elif key<node.key:
            node.left=self._put(key,node.left)
            if (self.height(node.left)-self.height(node.right))==2:
                if key<node.left.key:
                    node=self.singleLeftRotate(node)
                else:
                    node=self.doubleLeftRotate(node)
            
        elif key>node.key:
            node.right=self._put(key,node.right)
            if (self.height(node.right)-self.height(node.left))==2:
                if key<node.right.key:
                    node=self.doubleRightRotate(node)
                else:
                    node=self.singleRightRotate(node)
        
        
        node.height=max(self.height(node.right),self.height(node.left))+1
        return node
        
    def delete(self,key):
        self.root=self.remove(key,self.root)
    
    def remove(self,key,node):
        if node is None:
            raise KeyError
        elif key<node.key:
            node.left=self.remove(key,node.left)
            if (self.height(node.right)-self.height(node.left))==2:
                if self.height(node.right.right)>=self.height(node.right.left):
                    node=self.singleRightRotate(node)
                else:
                    node=self.doubleRightRotate(node)
            node.height=max(self.height(node.left),self.height(node.right))+1
            
                
        elif key>node.key:
            node.right=self.remove(key,node.right)
            if (self.height(node.left)-self.height(node.right))==2:
                if self.height(node.left.left)>=self.height(node.left.right):
                    node=self.singleLeftRotate(node)
                else:
                    node=self.doubleLeftRotate(node)
            node.height=max(self.height(node.left),self.height(node.right))+1
        
        elif node.left and node.right:
            if node.left.height<=node.right.height:
                minNode=self._findMin(node.right)
                node.key=minNode.key
                node.right=self.remove(node.key,node.right)
            else:
                maxNode=self._findMax(node.left)
                node.key=maxNode.key
                node.left=self.remove(node.key,node.left)
            node.height=max(self.height(node.left),self.height(node.right))+1
        else:
            if node.right:
                node=node.right
            else:
                node=node.left
        return(node)

    def tree_out(self, node):
            print("----"*40)
            print("\n")
            thislevel = [node]
            a = ' '*82
            while thislevel:
                nextlevel = list()
                a = a[:len(a)//2]
                for n in thislevel:
                    if n is not None:
                        print(a+str(n.key)+a,end="")
                        if node.left:
                            nextlevel.append(n.left)
                        if node.right:
                            nextlevel.append(n.right)
                    else:
                        print(a+"--"+a,end="")
                    thislevel = nextlevel
                print("\n\n")
            print("----"*40)
                

# Введите массив как элемент, в котором должен храниться каждый узел дерева
start = False
tree = AVL_Tree()
while start == True:
    ans = int(input("Выберите действие:\n>>>1.Добавить узел\n>>>2.Удалить узел по значению\n>>>3.Поиск по значению\n>>>4.Вывод дерева\n>>>5.Завершить работу\n"))
    if ans == 1:
        start_1 = True
        inp = int(input("Введите значение для вставки: "))
        tree.put(inp)
        tree.tree_out(tree.root)
        while start_1 == True:
            ans1 = int(input("1. Добавить еще\n2. Остановить добавление\n>>>>>"))
            if ans1 == 1:
                inp = int(input("Введите значение для вставки: \n>"))
                tree.put(inp)
                tree.tree_out(tree.root)
            elif ans1 == 2:
                start_1 = False
            
    elif ans == 2:
        inp = int(input("Введите значение узла , чтобы удалить его: ")) 
        tree.delete(inp)
    elif ans == 3:
        inp = int(input("Введите значение узла , чтобы найти его: ")) 
    elif ans == 4:
        tree.tree_out(tree.root)
    elif ans == 5:
        print("Завершаю работу...")
        start = False
n = list(map(int,"10 1 2 3 3 5 7 15 27 35" .split(" ")))
print(n)
 #   avl   Экземпляр
 # Вставить элементы списка в сбалансированное двоичное дерево один за другим
for i in range(len(n)):
    tree.put(n[i])
    tree.tree_out(tree.root)
# Сначала пройдемся по бинарному сбалансированному дереву
tree.tree_out(tree.root)
n1 = [27,35]
for i in range(len(n1)):
    tree.delete(n1[i])
tree.tree_out(tree.root)