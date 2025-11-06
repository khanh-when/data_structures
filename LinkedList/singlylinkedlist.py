import random

class Node():
    
    def __init__(self, value):
        self.data = value
        self.next = None


def main():
    
    random.seed(8)
    data = list((random.randint(1, 10) for i in range(10)))
    print(data)
    head = Node(data[0])
    curr_node = head

    for val in data[1:]:
        curr_node.next = Node(val)
        curr_node = curr_node.next


    print('\nPrinting Nodes:')
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

        


    # for item in data:
    #     curr_node = curr_node.next
    #     curr_node.next = Node(item)
    #     print(curr_node.data)
        

if __name__ == "__main__":
    main()