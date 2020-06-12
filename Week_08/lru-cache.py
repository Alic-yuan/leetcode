class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.hash = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = capacity

    def add_node_to_tail(self, key):
        node = self.hash[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.tail.prev
        node.next = self.tail

        node.prev.next = node
        self.tail.prev = node

    def del_node(self):
        key = self.head.next.key
        self.hash.pop(key)
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.add_node_to_tail(key)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].value = value
            self.add_node_to_tail(key)
        else:
            if len(self.hash) == self.size:
                self.del_node()
            node = Node(key, value)
            self.hash[key] = node
            node.prev = self.tail.prev
            node.next = self.tail

            node.prev.next = node
            self.tail.prev = node