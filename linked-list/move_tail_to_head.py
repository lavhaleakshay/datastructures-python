class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def len_iterative(self):

        count = 0 
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def move_tail_to_head(self):
        
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next

        last.next = self.head
        second_to_last.next = None
        self.head = last

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")

llist.print_list()
print("\n")
llist.move_tail_to_head()
print("\n")
llist.print_list()