class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        self.head=ListNode()
        self.sz=0
        """Create a new list with a Sentinel Node"""

    def insert(self,x,pos):
        temp=ListNode()
        temp.value=x
        temp.next=pos.next
        pos.next=temp
        self.sz=self.sz+1
        """Insert element x in the position after pos"""
        pass

    def delete(self,pos):
        x=pos.next
        pos.next=x.next
    
        """Delete the node following node pos in the linked list."""
        self.sz=self.sz-1
        pass

    def print(self):
        x=self.head
        x=x.next
        l=list()
        while x!=None:
            #print(x.value,end=" ")
            l.append(x.value)
            x=x.next
        #print ()
        return l
        """ Print all the elements of a list in a row."""
        pass

    def insertAtIndex(self,x,i):
        j=0
        y=self.head
        while True:
            if j==i:
                temp=ListNode(x,y.next)
                y.next=temp
                self.sz=self.sz+1
                break
            else:
                j=j+1
                y=y.next
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        pass

    def search(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        pass

    def len(self):
        """Return the length (the number of elements) in the Linked List."""
        return self.sz
        pass

    def isEmpty(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.sz==0:
            return True
        else:
            return False
        pass


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value, next. 
    """
    def __init__(self,val=None,nxt=None):
        self.value=val
        self.next=nxt

def main():
    #print("Something")
    L = LinkedList()
    L.insert(10,L.head)
    #L.insert(20,L.head)
    print('List is: ',L.print())
    L.insert(12,L.head.next)
    print('List is: ',L.print())
    L.insert(2,L.head)
    print('List is: ',L.print())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is: ',L.print())
    L.delete(L.head.next)
    print('List is: ',L.print())
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('List is: ',L.print())

if __name__ == '__main__':
    main()
