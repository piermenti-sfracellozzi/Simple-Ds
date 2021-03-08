# Tree:


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.data))
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


# Binary Search Tree:

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def represent(self):
        if self.data is None:
            return "The tree is empty."
        else:
            print(f"[{self.data}]")
            if self.right:
                print("|_")
                self.right.represent()
            if self.left:
                print("_|")
                self.left.represent()

    def add_child(self, data):
        if data == self.data:
            return "Binary search tree cant have duplicates."

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class DoublyLinkedNode:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def represent(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        count = 0
        itr = self.head
        llstr = ""
        while itr:
            if count > 0:
                llstr += " --> " + "[" + str(itr.data) + "]"
            else:
                llstr += "[" + str(itr.data) + "]"
            itr = itr.next
            count += 1
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def toarray(self):
        output_array = []
        itr = self.head
        while itr:
            output_array.append(itr.data)
            itr = itr.next

        return output_array

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Invalid Index.")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_at_beginning(self):
        if self.head is None:
            return "Nothing to remove."
        else:
            self.remove_at(0)

    def remove_at_end(self):
        if self.head is None:
            return "Nothing to remove."

        count = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1

        self.remove_at(count)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError("Invalid Index.")

        elif index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def type_all(self):
        if self.head is None:
            print("The linked list is empty.")

        types = []
        count_int = 0
        count_str = 0
        count_bool = 0
        count_float = 0
        count_complex = 0
        count_list = 0
        count_tuple = 0
        count_dict = 0
        count_range = 0
        count_set = 0
        count_bytes = 0
        count_bytearray = 0
        count_memoryview = 0
        count_frozenset = 0

        itr = self.head
        while itr:
            types.append(type(itr.data))
            itr = itr.next
        for i in types:
            if i == int:
                count_int += 1
            elif i == str:
                count_str += 1
            elif i == bool:
                count_bool += 1
            elif i == float:
                count_float += 1
            elif i == complex:
                count_complex += 1
            elif i == list:
                count_list += 1
            elif i == tuple:
                count_tuple += 1
            elif i == dict:
                count_dict += 1
            elif i == range:
                count_range += 1
            elif i == set:
                count_set += 1
            elif i == frozenset:
                count_frozenset += 1
            elif i == bytes:
                count_bytes += 1
            elif i == bytearray:
                count_bytearray += 1
            elif i == memoryview:
                count_memoryview += 1

        if count_int == len(types):
            return "Integer"
        elif count_str == len(types):
            return "String"
        elif count_bool == len(types):
            return "Boolean"
        elif count_float == len(types):
            return "Float"
        elif count_complex == len(types):
            return "Complex"
        elif count_list == len(types):
            return "List"
        elif count_tuple == len(types):
            return "Tuple"
        elif count_dict == len(types):
            return "Dictionary"
        elif count_range == len(types):
            return "Range"
        elif count_set == len(types):
            return "Set"
        elif count_frozenset == len(types):
            return "Frozen Set"
        elif count_memoryview == len(types):
            return "MemoryView"
        elif count_bytes == len(types):
            return "Bytes"
        elif count_bytearray == len(types):
            return "ByteArray"
        else:
            return "Various"

    def type_each(self):
        if self.head is None:
            print("The linked list is empty.")

        types = []
        types2 = []
        itr = self.head
        while itr:
            types.append(type(itr.data))
            itr = itr.next
        for i in types:
            if i == int:
                types2.append("Integer")
            elif i == str:
                types2.append("String")
            elif i == bool:
                types2.append("Boolean")
            elif i == float:
                types2.append("Float")
            elif i == complex:
                types2.append("Complex")
            elif i == list:
                types2.append("List")
            elif i == tuple:
                types2.append("Tuple")
            elif i == dict:
                types2.append("Dict")
            elif i == range:
                types2.append("Range")
            elif i == set:
                types2.append("Set")
            elif i == frozenset:
                types2.append("frozenset")
            elif i == bytes:
                types2.append("bytes")
            elif i == bytearray:
                types2.append("bytearray")
            elif i == memoryview:
                types2.append("Memoryview")
        print(types2)


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = DoublyLinkedNode(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = DoublyLinkedNode(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = DoublyLinkedNode(data, None, itr.previous)

    def type_all(self):
        if self.head is None:
            print("The linked list is empty.")

        types = []
        count_int = 0
        count_str = 0
        count_bool = 0
        count_float = 0
        count_complex = 0
        count_list = 0
        count_tuple = 0
        count_dict = 0
        count_range = 0
        count_set = 0
        count_bytes = 0
        count_bytearray = 0
        count_memoryview = 0
        count_frozenset = 0

        itr = self.head
        while itr:
            types.append(type(itr.data))
            itr = itr.next
        for i in types:
            if i == int:
                count_int += 1
            elif i == str:
                count_str += 1
            elif i == bool:
                count_bool += 1
            elif i == float:
                count_float += 1
            elif i == complex:
                count_complex += 1
            elif i == list:
                count_list += 1
            elif i == tuple:
                count_tuple += 1
            elif i == dict:
                count_dict += 1
            elif i == range:
                count_range += 1
            elif i == set:
                count_set += 1
            elif i == frozenset:
                count_frozenset += 1
            elif i == bytes:
                count_bytes += 1
            elif i == bytearray:
                count_bytearray += 1
            elif i == memoryview:
                count_memoryview += 1

        if count_int == len(types):
            return "Integer"
        elif count_str == len(types):
            return "String"
        elif count_bool == len(types):
            return "Boolean"
        elif count_float == len(types):
            return "Float"
        elif count_complex == len(types):
            return "Complex"
        elif count_list == len(types):
            return "List"
        elif count_tuple == len(types):
            return "Tuple"
        elif count_dict == len(types):
            return "Dictionary"
        elif count_range == len(types):
            return "Range"
        elif count_set == len(types):
            return "Set"
        elif count_frozenset == len(types):
            return "Frozen Set"
        elif count_memoryview == len(types):
            return "MemoryView"
        elif count_bytes == len(types):
            return "Bytes"
        elif count_bytearray == len(types):
            return "ByteArray"
        else:
            return "Various"

    def type_each(self):
        if self.head is None:
            print("The linked list is empty.")

        types = []
        types2 = []
        itr = self.head
        while itr:
            types.append(type(itr.data))
            itr = itr.next
        for i in types:
            if i == int:
                types2.append("Integer")
            elif i == str:
                types2.append("String")
            elif i == bool:
                types2.append("Boolean")
            elif i == float:
                types2.append("Float")
            elif i == complex:
                types2.append("Complex")
            elif i == list:
                types2.append("List")
            elif i == tuple:
                types2.append("Tuple")
            elif i == dict:
                types2.append("Dict")
            elif i == range:
                types2.append("Range")
            elif i == set:
                types2.append("Set")
            elif i == frozenset:
                types2.append("frozenset")
            elif i == bytes:
                types2.append("bytes")
            elif i == bytearray:
                types2.append("bytearray")
            elif i == memoryview:
                types2.append("Memoryview")
        print(types2)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def represent(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        count = 0
        itr = self.head
        dllstr = ""
        while itr:
            if count > 0:
                dllstr += " --- " + "[" + str(itr.data) + "]"
            else:
                dllstr += "[" + str(itr.data) + "]"
            itr = itr.next
            count += 1
        print(dllstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Invalid Index.")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.previous = itr.previous.previous
                break
            itr = itr.next
            count += 1

    def remove_at_beginning(self):
        if self.head is None:
            return "Nothing to remove."
        else:
            self.remove_at(0)

    def remove_at_end(self):
        if self.head is None:
            return "Nothing to remove."

        count = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count += 1

        self.remove_at(count)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise IndexError("Invalid Index.")

        elif index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = DoublyLinkedNode(data, itr.next, itr.previous)
                itr.next = node
                break

            itr = itr.next
            count += 1


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


# Stacks:


class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def push_many(self, itemarray):
        if type(itemarray) != list:
            raise Exception("The data type of the second parameter should be a list.")
        for element in itemarray:
            self.stack.append(element)

    def clear(self):
        self.stack.clear()

    def size(self):
        return len(self.stack)

    def print_stack(self):
        if len(self.stack) == 0:
            return "The stack is empty."
        stack = ""
        for element in self.stack:
            stack += f"\n [{element}] "

        print(stack)

    def to_array(self):
        if len(self.stack) == 0:
            return "The stack is empty."

        return self.stack

    def to_string(self):
        if len(self.stack) == 0:
            return "The stack is empty."
        string_output = ""
        for i in range(len(self.stack)):
            if i < len(self.stack) - 1:
                string_output += f" {self.stack[i]} ,"
            else:
                string_output += f" {self.stack[i]} "

        return string_output


# Queues:


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def enqueue_many(self, itemarray):
        if type(itemarray) != list:
            raise Exception("The data type of the second parameter should be a list.")
        for element in itemarray:
            self.queue.append(element)

    def dequeue_all(self):
        self.queue.clear()

    def size(self):
        return len(self.queue)

    def print_queue(self):
        if len(self.queue) == 0:
            return "The queue is empty."
        queue = ""
        for element in self.queue:
            queue += f"\n [{element}]"

        print(queue)

    def to_array(self):
        if len(self.queue) == 0:
            return "The queue is empty."

        return self.queue

    def to_string(self):
        if len(self.queue) == 0:
            return "The queue is empty."
        string_output = ""
        for i in range(len(self.queue)):
            if i < len(self.queue) - 1:
                string_output += f" {self.queue[i]} ,"
            else:
                string_output += f" {self.queue[i]} "

        return string_output
