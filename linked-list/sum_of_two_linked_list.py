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

    def sum_two_list(self, llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            print("S:" +str(s))

            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
            sum_list.print_list()

llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(9)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

llist1.print_list()
print("\n")
llist2.print_list()
print("\n")
print(365 + 246)
llist1.sum_two_list(llist2)