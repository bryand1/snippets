class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        """Add to start of list"""
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def length(self):
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        return count

    def delete(self, item):
        curr = self.head
        if curr and curr.data == item:
            self.head = curr.next
            del curr
            return
        while curr:
            prev = curr
            curr = curr.next
            if curr and curr.data == item:
                prev.next = curr.next
                del curr
                return

    def insert(self, index, item):
        newnode = Node(item)
        prev = None
        curr = self.head
        count = 0
        while curr:
            prev = curr
            curr = curr.next
            if count == index:
                prev.next = newnode
                newnode.next = curr
                break
            count += 1

    def __repr__(self):
        curr = self.head
        vals = []
        while curr:
            vals.append(curr.data)
            curr = curr.next
        return ' '.join(map(str, vals))


if __name__ == '__main__':
    L = LinkedList()
    L.push(50)
    L.push(40)
    L.push(30)
    L.push(20)
    print(repr(L))
    L.delete(20)
    L.insert(0, 10)
    print(L.length())
    print(repr(L))
