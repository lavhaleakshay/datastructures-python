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

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s

            while p and q:
                if p.data <= q.data:
                    s.next = p
                    s = p
                    p = s.next
                else:
                    s.next = q
                    s = q
                    q = s.next
            
            if not p:
                s.next = q
            if not q:
                s.next = p
            
        return new_head


    def remove_duplicates(self):

        prev = None
        cur = self.head
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                #Remove Node
                prev.next = cur.next
                cur = None

            else:
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next




llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(1)
print("\n")
llist.remove_duplicates()
print("\n")
llist.print_list()

