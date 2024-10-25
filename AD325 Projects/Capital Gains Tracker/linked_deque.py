
class DLNode:
    def __init__(self, previous_node=None, data_portion=None, next_node=None):
        self.data_portion = data_portion    # the data the node holds
        self.next_node = next_node          # the next node in the list
        self.previous_node = previous_node  # the previous node in the list

    # all of these are self explanatory
    def get_data(self):return self.data_portion
    def set_data(self, new_data):self.data_portion = new_data
    def get_next_node(self):return self.next_node
    def set_next_node(self, next_node):self.next_node = next_node 
    def get_previous_node(self):return self.previous_node
    def set_previous_node(self, previous_node):self.previous_node = previous_node
    

class LinkedDeque:
    def __init__(self):
        self.head = None    # the head of the linked deque
        self.tail = None    # the tail of the linked deque
    
    def add_to_back(self, new_entry):
        if self.is_empty():         # if there are no nodes in the list
            new_node = DLNode(data_portion = new_entry) # make a new node
            self.tail = new_node    # make the new node the tail
            self.head = new_node    # and make it the head too
        # make a new DL node and set it's prev to be the current tail
        else: # need to add an else here or it makes 2 nodes oops
            new_node = DLNode(previous_node = self.tail, data_portion = new_entry)
            self.tail.set_next_node(new_node)   # link the current tail.next to the new node
            self.tail = new_node                # make the new node the new tail

    def add_to_front(self, new_entry):
        if self.is_empty():         # if there are no nodes in the list
            new_node = DLNode(data_portion = new_entry) # make a new node
            self.head = new_node    # make the new node the head
            self.tail = new_node    # and make it the tail too
        # make a new DL node and set it's next to be the current head
        new_node = DLNode(next_node = self.head, data_portion = new_entry)
        self.head.set_previous_node(new_node)# set current head.prev to be new node
        self.head = new_node                # make the new node the new head

    def get_back(self):
        return self.tail # return tail
    def get_front(self):
        return self.head # return head
    
    def remove_front(self):
        if (self.head == self.tail):    # if the head is also the tail
            self.tail = None            # clear tail
        self.head = self.head.get_next_node()   # make head.next the new head
        if self.head: # make sure head isn't none, cause that causes malarkey
            self.head.set_previous_node(None)       # clear new head's previous node

    def remove_back(self):
        if (self.tail == self.head):    # if the tail is also the head
            self.head = None            # clear head
        self.tail = self.tail.get_previous_node()   # make tail.prev the new tail
        self.tail.set_next_node(None)               # clear tail's next pointer

    def clear(self):
        self.head = None    # clear head
        self.tail = None    # clear tail

    def is_empty(self):
        if (self.head == None and self.tail == None):   # if both head and tail are clear
            return True     # return True
        else: return False  # If they're not empty, return False
        
    def display(self):
        if self.is_empty(): # if the deque is empty
            return None     # return none
        else:
            current = self.head # a pointer to travers the deque
            outputList = []     # a list to return
            while current:      # while there are elements left in deque
                outputList.append(current.get_data()) # append the current element for output
                current = current.get_next_node()     # move to the next node in deque
            return outputList   # return the list
        # might have to change this later so that it prints instead of returning a list
    
    # Some Extra Methods:
    def size(self):
        count = 0           # an int to count with
        current = self.head # a pointer to travers the deque
        while current:      # while there are nodes left
            count +=1       # count em and move the pointer
            current = current.get_next_node()
        return count    # return the count
    
    # I should've been a history major