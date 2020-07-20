class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def append_front(self, data):
        new_node = Node(data)
        old_head_next = self.head.next
        self.head.next = new_node
        new_node.next = old_head_next

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        data_list = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            data_list.append(cur_node.data)
        print(data_list)

    def get(self, index):
        if index >= self.length() or index < 0:
            return -1
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    # Bracket Get: a[0]
    def __getitem__(self, index):
        return self.get(index)

    def delete(self, index):
        if index >= self.length() or index < 0:
            return -1
        cur_idx = 0
        cur_node = self.head
        while True:
            prev_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                prev_node.next = cur_node.next
                return
            cur_idx += 1

    def insert(self, index, data):
        if index >= self.length() or index < 0:
            return self.append(data)
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = Node(data)
                prior_node.next = new_node
                new_node.next = cur_node
                return
            prior_node = cur_node
            cur_idx += 1

    def set(self, index, data):
        if index >= self.length() or index < 0:
            return -1
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.data = data
                return cur_node.data
            cur_idx += 1

# MAIN
a = LinkedList()
a.display()
a.append("Hello")
a.append("World")
a.append("LL")
a.display()
print("Length: " + str(a.length()))
a.append_front("VS")
a.display()
a.delete(0)
a.display()
print(a[1])
a.insert(3, "Insert")
a.set(1, "Set")
a.display()
a.delete(2)
a.display()
