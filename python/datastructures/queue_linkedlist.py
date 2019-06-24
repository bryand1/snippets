class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None
    
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return
        else:
            data = self.head.data
            self.head = self.head.next
            return data


def main():
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print(q.dequeue())  # 5
    print(q.dequeue())  # 6

if __name__ == '__main__':
    main()

