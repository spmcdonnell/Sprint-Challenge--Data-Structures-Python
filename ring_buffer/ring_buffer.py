from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.__len__() == 0:
            # Add initial node
            self.storage.add_to_head(item)

        elif self.storage.__len__() < self.capacity:
            # Keep adding to tail
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        elif self.storage.__len__() == self.capacity:

            if self.current != self.storage.tail:
                # Add new one and set current
                self.current = self.current.next
                self.current.insert_before(item)
                self.current = self.current.prev

                # Delete oldest one
                self.storage.delete(self.current.next)

                # Account for deleting reducing the length in an unwanted way
                self.storage.length += 1

            else:
                # Replace head if the current one is the tail
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.storage.head

        while current.next != None:
            list_buffer_contents.append(current.value)
            current = current.next

        # Add last item to list
        list_buffer_contents.append(current.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
