class Node:
    """a class for node in a single list."""
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """a class for the single list."""
    def init(self):
        self.head = None

    def append(self, data):
        """Append new node with the  data to  end of  list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        """print the  list"""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("->".join(map(str, elements)))

    def delete_nodes(self, m, n):
        """delete n nodes after skip m nodes"""
        if m < 0 or n < 0:
            raise ValueError("m and n must be non-negative integers.")
        if self.head is None:
            print("The linked list is empty.")
            return

        current = self.head

        while current:
            # Skip m nodes
            for _ in range(m):
                if current is None:
                    return
                current = current.next
                
          
            for _ in range(n):
                if current is None:
                    return
             
                to_delete = current
                current = current.next  
                del to_delete  

def main():
    """imp function to execute  linked list manipulate"""
    linked_list = LinkedList()
    
    # example input: You can modify this list or take input from the user
    input_list = [9, 1, 3, 5, 9, 4, 10, 1]
    
    for value in input_list:
        linked_list.append(value)
    
    print("Original Linked List:")
    linked_list.print_list()
    
   
    try:
        m = int(input("Enter the number of nodes to skip (m): "))
        n = int(input("Enter the number of nodes to delete (n): "))
        
        if m < 0 or n < 0:
            raise ValueError("m and n must be non-negative integers.")
        
        linked_list.delete_nodes(m, n)

        print("Linked List after deleting nodes:")
        linked_list.print_list()
    except ValueError as e:
        print(f"Error: {e}")

if name == "main":
    main()