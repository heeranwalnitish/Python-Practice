class Node:
    def __init__(self, data=None, next =None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    
    def print(self):
        if self.head is None:
            print('Linked List is empty ')
            return
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + '--->' if itr.next else str(itr.data)
            itr = itr.next
        print(listr)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return count   


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node 


    def insert_at_end(self, data):
        if self.head is None :
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)


    def insert_at(self, index, data):
        if index <0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0 :
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr :
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1

    def remove(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr :
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



if __name__ =='__main__' :
    l1 = LinkedList()
    l1.insert_values(["NITISH","DIVYA","PRIYANKA","SHIVAM","POOJA"])
    l1.insert_at(4, "AKASH")
    l1.insert_at_end("NAMAN")
    l1.insert_at(4,"VASIM")
    l1.remove(5)
    l1.print()