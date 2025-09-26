"""
    
    @Author: Federico Baù
    @Creation Date: 25 - Jan - 2021
    @Updated: N/a

    Resources: StackOverflow: https://stackoverflow.com/questions/65844996/covert-binary-tree-to-doubly-linked-list-microsoft-interview/65864149#65864149
    
"""

# ========================= < Version 1 > ========================= #

class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.prev = None
        self.visited = False

    def create_tree(self, show_tree=False):
        """Creating the Tree with a Depth-First Search Algorithm"""
            
        root = self # Set Current Node        
        stack = [root]

        while True:

            if not stack:
                break

            current = stack.pop() # Remove Current From Stack

            if current.right:
                current.right.prev = current
                stack.append(current.right)            
            if current.left:
                current.left.prev = current
                stack.append(current.left)

            if show_tree:
                print(f'{current.data} --> ', end='')


def create_dll(root_head):
    """Algorithm to Conver Binary Tree to Doubly Linked List"""

    doubly_linked_list = []

    # --- Find DLL Head NOTE: Just need to go left till hit NONE
    head = None
    current = root_head 
    while True:
        if current.left:
            current = current.left
        else:
            head = current
       
            break
    
    stack = [head]
    visited = set()

    def add_visited(*args):
        for item in args:
            visited.add(item)

    # --- Crawls back up, following each Triangle Shape from left Vertices to Right
    while True:

        try:
            current = stack.pop()
        except IndexError:
            pass

        if current in doubly_linked_list:
            break
        
   
        if current.left and  current.left not in visited: # Goes Down to Next Triangle Shape        
            stack.append(current.left)
            continue

        elif current.prev and current.prev.right:     
            if current not in visited: 
                doubly_linked_list.append(current)

            if current.prev.right.left and current.prev.right.left not in visited: # If finds a Left Vertices, Goes down 
  
                add_visited(current, current.prev, current.prev.right)
                doubly_linked_list.append(current.prev)

                if current.prev.prev:
                    stack.append(current.prev.prev)
                stack.append(current.prev.right.left)    
                continue

            elif current.prev.right.right:  # Checks if Right Vertices Has Left or right
                if current.prev.right.right.left:
                    stack.append(current.right.right.left)    
                    continue
                doubly_linked_list.append(current.prev.right.right)                
            else:     
                doubly_linked_list.append(current.prev)
                doubly_linked_list.append(current.prev.right)              
        
                add_visited(current, current.prev, current.prev.right)
                if current.prev.prev and current.prev.prev not in visited:
                    stack.append(current.prev.prev)


        elif current.prev:     
            doubly_linked_list.append(current.prev)
            add_visited(current)
            if current.prev.prev:
                stack.append(current.prev.prev)

        elif current.right:

            doubly_linked_list.append(current)
            add_visited(current)
            if current.right.left:
                stack.append(current.right.left)    
                continue
            elif current.right.right:       
                if current.right.right.left:
                    stack.append(current.right.right.left)    
                    continue
                doubly_linked_list.append(current.right)
                doubly_linked_list.append(current.right.right)
                add_visited(current.right, current.right.right)                
            else:    
                add_visited(current.right)  
                doubly_linked_list.append(current.right)       
    
    return doubly_linked_list

    
def show_ddl(ddl):

    for node in ddl:
        print(f'{node.data} --> ', end='')


# --------->  Creating The Binary Tree >

root = BinaryTree(10)
root.left = BinaryTree(12)
root.right = BinaryTree(15)
root.left.left = BinaryTree(25)
root.left.right = BinaryTree(30)
root.left.right.left = BinaryTree(60)           
root.left.right.right = BinaryTree(77)
root.right.right = BinaryTree(40)
root.right.left = BinaryTree(36)
root.right.left.left = BinaryTree(50)
root.right.left.right = BinaryTree(13)

print('\nBynary Tree:\n')
root.create_tree(show_tree=True)
print()
print('==='*15)
print()
# --------->  Creating The Doubly Linked List >
print('Doubly Linked List:\n')
dll = create_dll(root)
show_ddl(dll)


# ---------- > OUTPUT >
# 10 --> 12 --> 25 --> 30 --> 60 --> 77 --> 15 --> 36 --> 50 --> 13 --> 40 --> 
# =============================================
# 25 --> 12 --> 60 --> 30 --> 77 --> 10 --> 50 --> 36 --> 13 --> 15 --> 40 -->


# ========================= < Version 2 > ========================= #

class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.prev = None
        self.visited = False

    def create_tree(self, show_tree=False):
        """Creating the Tree with a Depth-First Search Algorithm"""
            
        root = self # Set Current Node        
        stack = [root]

        while True:

            if not stack:
                break

            current = stack.pop() # Remove Current From Stack

            if current.right:
                current.right.prev = current
                stack.append(current.right)            
            if current.left:
                current.left.prev = current
                stack.append(current.left)

            if show_tree:
                print(f'{current.data} --> ', end='')


def create_dll(root_head):
    """Algorithm to Conver Binary Tree to Doubly Linked List"""

    doubly_linked_list = []

    # --- Find DLL Head NOTE: Just need to go left from Binary Tree till hit NONE
    head = None
    current = root_head 
    while True:
        if current.left:
            current = current.left
        else:
            head = current       
            break
    
    stack = [head]
    visited = set()

    def add_node(*args, add_dll=None):
        """Helper Function, Add Node to the Visited Set."""
        for item in args:
            visited.add(item)
        if add_dll:
            for node in add_dll:
                doubly_linked_list.append(node)

    # --- Crawls back up, following each Triangle Shape from left Vertices to Right
    while True:

        try:
            current = stack.pop()
        except IndexError:
            pass

        if current in doubly_linked_list:
            break
        
   
        if current.left and current.left not in visited: # NOTE: Goes Down to Next Triangle Shape        
            stack.append(current.left)
            continue
        elif current.prev: # NOTE: Goes Up one Node
            add_node(add_dll=[current])

            # ---------------  Check if we can go to the left.
            if current.prev.right.left and current.prev.right.left not in visited: # NOTE: Goes deeper 
                add_node(current.prev, current.prev.right, add_dll=[current.prev])

                if current.prev.prev: # NOTE: Backtracking
                    stack.append(current.prev.prev)
                stack.append(current.prev.right.left)    
                continue

            # ------------- Here We Handle in case previous Node Has ONLY Right path
            elif current.prev.right.right:  
                if current.prev.right.right.left:  # If has Left Node we go deeper
                    stack.append(current.right.right.left)    
                    continue
                add_node(add_dll=[current.prev.right.right])              
            else:     
                add_node(current.prev, add_dll=[current.prev])

                if current.prev.right: # DOES the Prev node have a Right node?
                    add_node(current.prev.right, add_dll=[current.prev.right])
                
        
                if current.prev.prev and current.prev.prev not in visited: # NOTE: BackTrackin
                    stack.append(current.prev.prev)
        #  -------------- >N OTE: Here Handle The 'Root node' (i.e. 10), only option is to go to right
        elif current.right: 
            add_node(current, add_dll=[current])
            if current.right.left: # Going Deeper
                stack.append(current.right.left)    
                continue
            elif current.right.right:   
                if current.right.right.left:
                    stack.append(current.right.right.left)    
                    continue
                add_node(current.right, current.right.right, add_dll=[current.right, current.right.right])                
            else:    
                add_node(current.right, add_dll=[current.right])  
    
    return doubly_linked_list

    
def show_ddl(ddl):
    """Helper function, used to print the Doubly Linked List"""
    for node in ddl:
        print(f'{node.data} --> ', end='')


# --------->  Creating The Binary Tree >

root = BinaryTree(10)
root.left = BinaryTree(12)
root.right = BinaryTree(15)
root.left.left = BinaryTree(25)
root.left.right = BinaryTree(30)
root.left.right.left = BinaryTree(60)           
root.left.right.right = BinaryTree(77)
root.right.right = BinaryTree(40)
root.right.left = BinaryTree(36)
root.right.left.left = BinaryTree(50)
root.right.left.right = BinaryTree(13)

print('\nBynary Tree:\n')
root.create_tree(show_tree=True)
print()
print('==='*15)
print()
# --------->  Creating The Doubly Linked List >
print('Doubly Linked List:\n')
dll = create_dll(root)
show_ddl(dll)
test = []
for n in dll:
    test.append(n.data)
test_ = [25, 12, 60, 30, 77, 10, 50, 36, 13, 15, 40]
assert test == test_
# 10 --> 12 --> 25 --> 30 --> 60 --> 77 --> 15 --> 36 --> 50 --> 13 --> 40 --> 
# =============================================
# 25 --> 12 --> 60 --> 30 --> 77 --> 10 --> 50 --> 36 --> 13 --> 15 --> 40 -->
