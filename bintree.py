# You are using Python
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.root=None
        
    def add_node(self,data):
        new_node=node(data)
        if self.root is None:
            self.root=new_node
        else:
            focus_node=self.root
            parent=None
            while True:
                parent=focus_node
                if data<focus_node.data:
                    focus_node=focus_node.left
                    if focus_node is None:
                        parent.left=new_node
                        return
                else:
                    focus_node=focus_node.right
                    if focus_node is None:
                        parent.right=new_node
                        return
    def pot(self,focus_node):
        if focus_node is not None:
            print(focus_node.data,end=" ")
            self.pot(focus_node.left)
            self.pot(focus_node.right)

if __name__ == "__main__":
    tree=BinaryTree()
    n=input().split(" ")
    for i in n:
        if int(i)<=0:
            break
        else:
            tree.add_node(int(i))
            
    tree.pot(tree.root)
