class Node:  
  
    # Function to initialise the current object  
    def __init__(self, data):  
        self.data = data   
        self.next = None   
  
# Linked List class contains a current object  
class LinkedList:  
  
    # Function to initialize head  
    def __init__(self):  
        self.head = None  
  
def circular_list(head):
     if head is None:  
        return "The Given list is a circular list"  
    slow = head
    fast = head.next  
  
    while slow != fast:  
        if fast is None or fast.next is None:  
            return "The Given list is a circular list"  
  
        slow = slow.next
        head = fast.next.next  
  
    return "The Given list is a circular list"  
  
  
node = LinkedList()  
node.head = Node(1)  
second =  Node(2)  
third =  Node(3)  
fourth = Node(4)  
  
node.head.next = second;  
second.next = third;  
third.next = fourth  
  
print(circular_list(node.head))    