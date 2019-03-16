
class Node:
    #tree node = left and right child + data which can be any object
    #создаем новый класс с именем Node с 3 атрибутами: Левый узел, Правый узел, Данные узла


    def __init__(self, data):

        self.left = None #
        self.right = None #все возможные numbers, которые вы, возможно, захотите написать, уже прикреплены к Noneобъекту.
        self.data = data


#Metods of additions

def insert(root, data):#insert new node with data

    node = Node(data)

    if root is None: #esli root mesto svobodno, to node ztanovitsya root
        root = node
    elif root.data >= data: #esli next number bolshe, chem root, to emu nujno vstat na levo
        if root.left is None: #esli left root is empty, to eto stanovitsya node
            root.left = node
        else:
            insert(root.left, data)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, data)

def print_insert(root): #functions of roots,if there is left root - it will addition, if there is a right root - it will addition, if there are no - it will be root with data

    if root:
        print_insert(root.left)
        print (root.data)
        print_insert(root.right)

    
root = Node(15)
insert(root, 8)
insert(root, 18)
insert(root, 24)
insert(root, 1)
insert(root, 41)
insert(root, 86)


print_insert(root)

 


