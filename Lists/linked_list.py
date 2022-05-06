"""
22/4/2022 - https://leetcode.com/problems/design-linked-list/

Accepted Solution at 200ms run-time and 14.7 MB memory usage - ~77% better than most python solutions.
"""

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def print_linked_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(f"{curr_node.val} -> ", end="")
            curr_node = curr_node.next

    def get(self, index: int) -> int:
        
        if index >= 0:
            count = 0
            node_to_return = self.head
            while node_to_return is not None:
                if count == index:
                    return node_to_return.val
                count += 1
                node_to_return = node_to_return.next

            #End of linked list reached, with element not being found.

            return -1
        else:
            return -1
        
    def addAtHead(self, val: int) -> None:

        if self.head is None:
            #Head doesn't exist 
            node_to_add = Node(val, self.head)

            self.head = node_to_add
            self.tail = node_to_add
        else:
            #Head exists
            self.head = Node(val, self.head)
        
        self.length += 1


    def addAtTail(self, val: int) -> None:
        
        if self.tail is None:
            #Tail doesn't exist (No element present)
            #Only possible when no element is present
            node_to_add = Node(val, None)
            self.head = node_to_add
            self.tail = node_to_add
        else:
            #Make the new tail point to None

            new_tail = Node(val, None)

            #Make the current tail next_ptr to the new tail to add.

            self.tail.next = new_tail  

            #Finally, make the new_tail the self.tail

            self.tail = new_tail
        
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:

        length_of_llist = self.length

        if index == 0:
            self.addAtHead(val)
        elif index == length_of_llist:
            self.addAtTail(val)
        elif index > length_of_llist:
            return None
        else:
            count = 0
            current_node = self.head
            node_to_add = Node(val, None)
            while count < index:
                if count + 1 == index:
                    #Temporarily save the next node's ptr of the node at the index to add. 
                    prev_next_ptr = current_node.next 

                    #Get the current node at the index, and point its next ptr to the new node to add.
                    current_node.next = node_to_add

                    #Point the new node next ptr, to the previous next ptr.
                    node_to_add.next = prev_next_ptr

                    self.length += 1
                    break

                #Move to next node
                current_node = current_node.next
                count += 1

    def deleteAtIndex(self, index: int) -> None:

        length_of_llist = self.length

        if index == 0:
            self.head = self.head.next
            self.length -= 1
        elif index >= length_of_llist:
            return None
        else:
            count = 0
            current_node = self.head

            while count < index:
                if count + 1 == index:
                    #The node before the index to delete at.
                    #E.g. 1 -> 2 -> 3 (To delete 2, we'll point the next ptr of 1 at 3 (which is 2 steps from 1 hence .next.next))
                    # print(f"Deleting {(current_node.next).val} at Index {index}")
                    
                    current_node.next = (current_node.next).next
                    
                    #If the next_ptr after deleting is None, then this current_node is the new tail. (Another way to check is via the index & length of llist)
                    if current_node.next is None:
                        self.tail = current_node
                    
                    self.length -= 1
                    break

                #Move to next node
                current_node = current_node.next
                count += 1

class Node:
    def __init__(self, val, next_ptr):
        self.val = val
        self.next = next_ptr
        
    def next(self):
        return self.next
        

if __name__ == "__main__":

    llist = MyLinkedList()

    input_methods = ["addAtHead","addAtTail","addAtTail","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","get","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtHead","addAtTail","get","addAtHead","get","addAtTail","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","get","addAtHead","addAtIndex","addAtTail","get","addAtIndex","get","addAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtTail","get","addAtIndex"]
    input_args = [[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]


    for method, args in zip(input_methods, input_args):
        print(f"\n{method} - {args}")
        if len(args) == 2:
            eval(f"llist.{method}({args[0]}, {args[1]})")
        else:
            eval(f"llist.{method}({args[0]})")
        
        llist.print_linked_list()


