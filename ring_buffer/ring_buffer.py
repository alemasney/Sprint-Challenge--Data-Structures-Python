from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        index = 0
        self.current = item
        if self.current is not None:
            self.get()
        # if self.storage < self.capacity
        if self.storage.length < self.capacity:
            # append to tail
            self.storage.add_to_tail(self.current)
        # else:
        else:
            if index is 0:
                #append to head
                self.storage.add_to_head(self.current)
            # else:
            else:
                # insert after self.storage[index]
                pass


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        print(self.current)
        # TODO: 
        if self.current is None:
            return
        else:
            list_buffer_contents.append(self.current)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capcity = capacity
        pass

    def append(self, item):
        pass

    def get(self):
        pass
