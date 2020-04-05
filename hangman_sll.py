class Node:
    def __init__(self, data=None, nexd=None, found = False):
        self.data = data
        self.next = nexd
        if data == " ":
            self.found = True
        else:
            self.found = found

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def find(self, char):
        curr = self.head
        ret_val = False
        while curr != None:
            if curr.data == char:
                curr.found = True
                ret_val = True
            curr = curr.next
        if ret_val:
            return True
        else:
            return False

    def check_win_con(self):
        curr = self.head
        while curr != None:
            if curr.found == False:
                return False
            curr = curr.next
        return True

    def __str__(self):
        return_str = ""
        node = self.head
        while node != None:
            if node.found:
                return_str += str(node.data)
                node = node.next
            else:
                return_str += "-"
                node = node.next
        return return_str