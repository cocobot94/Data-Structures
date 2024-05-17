from Node import Node


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.isEmpty():
            return
        return self.head

    def __add_to_start(self, node: Node):
        if self.isEmpty():
            self.head = self.last = node
            self.size += 1
            return True
        return False

    def __add_to_end(self, node: Node):
        self.last.next = node
        self.last = node
        self.size += 1
        return self.peek()

    def append(self, node: Node):
        if not isinstance(node, Node):
            return TypeError
        if self.__add_to_start(node):
            return self.peek()
        else:
            return self.__add_to_end(node)

    def insert_before(self, node: Node, data):
        if not isinstance(node, Node):
            return TypeError
        if self.__add_to_start(node):
            return self.peek()
        elif data == self.head.value:
            node.next = self.head
            self.head = node
            self.size += 1
            return self.peek()
        else:
            current = self.head
            while current.next != None:
                if current.next.value == data:
                    node.next = current.next
                    current.next = node
                    self.size += 1
                    return self.peek()
                current = current.next
            return self.__add_to_end(node)

    def insert_after(self, node: Node, data):
        if not isinstance(node, Node):
            return TypeError
        if self.__add_to_start(node):
            return self.peek()
        else:
            current = self.head
            while current != None:
                if current.value == data:
                    if current == self.last:
                        self.last = node
                    node.next = current.next
                    current.next = node
                    self.size += 1
                    return self.peek()
                current = current.next
            return self.__add_to_end(node)

    def remove_head(self):
        if self.isEmpty():
            return
        else:
            popped = self.head
            if self.last == self.head:
                self.last = None
            self.head = self.head.next
            self.size -= 1
            popped.next = None
            return popped

    def remove(self, data):
        if self.isEmpty():
            return
        elif self.head.value == data:
            return self.remove_head()
        else:
            current = self.head
            while current != None and current.next != None:
                if current.next.value == data:
                    popped = current.next
                    if current.next == self.last:
                        self.last = current
                    current.next = current.next.next
                    self.size -= 1
                    popped.next = None
                    return popped
                current = current.next
            return "Not found"

    def __quicksort(self, arr: list):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.__quicksort(left) + middle + self.__quicksort(right)

    def __get_dict_and_clean_list(self, attr=None):
        nodes = {}
        while self.head is not None:
            popped = self.remove_head()
            popped.next = None
            if attr is not None:
                nodes[popped.value.attr] = popped
            else:
                nodes[popped.value] = popped
        return nodes

    def sort(self, attr=None):
        """
        ordena la lista enlazada por un attributo del nodo
        o por el mismo valor del nodo si no se pasa ningun parametro
        """
        nodes = self.__get_dict_and_clean_list(attr)
        arr = [item for item in nodes.keys()]
        array_values = self.__quicksort(arr)
        for value in array_values:
            self.append(nodes.get(value))
        return


# algoritmo para eliminar elementos duplicados en una lista enlazada
class RemoveDups:
    def removeDups(self, lista: SingleLinkedList):
        if not isinstance(lista, SingleLinkedList):
            raise TypeError("Input must be an instance of SingleLinkedList")
        cont = 0
        foundValues = {}
        current = lista.peek()
        while current != None:
            if current.value in foundValues.keys():
                lista.remove_node(current)
                cont += 1
            else:
                foundValues[current.value] = current
            current = current.next
        return f"{cont} nodes duplicated deleted"


# combinar dos listas enlazadas en una solo ordenada
class MergeTwoList:

    def __is_sorted_linked_list(sll):
        current = sll.head

        while current and current.next:
            if current.value > current.next.value:
                return False
            current = current.next

        return True

    def mergeTwoList(self, list1: SingleLinkedList, list2: SingleLinkedList):
        if not (
            isinstance(list1, SingleLinkedList) and isinstance(list2, SingleLinkedList)
        ):
            raise TypeError(
                "Both list1 and list2 must be instances of SingleLinkedList"
            )
        # Si list1 está vacía, retornar una copia de list 2 y viceversa
        if list1.isEmpty():
            return list2.copy()
        elif list2.isEmpty():
            return list1.copy()

        if not self.__is_sorted_linked_list(list1):
            list1.sort()
        if not self.__is_sorted_linked_list(list2):
            list2.sort()

        resul_list = SingleLinkedList()

        while not (list1.isEmpty() or list2.isEmpty()):
            current_list1 = list1.peek()
            current_list2 = list2.peek()
            if current_list1.value < current_list2.value:
                resul_list.append(list1.remove_head())
            else:
                resul_list.append(list2.remove_head())

        while not list1.isEmpty():
            resul_list.append(list1.remove_head())

        while not list2.isEmpty():
            resul_list.append(list2.remove_head())

        return resul_list


# sort dos listas ordenadas
"""
def merge_sort(arr):
    # Si la lista es de tamaño 0 o 1, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Ordenar cada mitad recursivamente
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combinar las dos mitades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Comparar los elementos de las dos mitades y combinarlos en orden
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Agregar los elementos restantes (si hay) de cada mitad
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Ejemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
"""


"""


class RemoveDups:
    def removeDups(self, lista: SingleLinkedList):
        if not isinstance(lista, SingleLinkedList):
            raise TypeError("Input must be an instance of SingleLinkedList")

        unique_values = set()
        current = lista.peek()
        prev = None
        duplicates_removed = 0

        while current is not None:
            if current.value in unique_values:
                prev.next = current.next
                lista.size -= 1  # Reducir el tamaño de la lista
                duplicates_removed += 1
            else:
                unique_values.add(current.value)
                prev = current
            current = current.next

        return f"{duplicates_removed} duplicated nodes deleted"



class MergeTwoList:
    def mergeTwoList(self, list1: SingleLinkedList, list2: SingleLinkedList):
        if not (isinstance(list1, SingleLinkedList) and isinstance(list2, SingleLinkedList)):
            raise TypeError("Both list1 and list2 must be instances of SingleLinkedList")

        if list1.isEmpty():
            return list2.copy()  # Si list1 está vacía, retornar una copia de list2
        elif list2.isEmpty():
            return list1.copy()  # Si list2 está vacía, retornar una copia de list1

        # Si ambas listas no están vacías, continuar con la fusión
        resul_list = SingleLinkedList()
        current_list1 = list1.peek()
        current_list2 = list2.peek()

        while current_list1 is not None and current_list2 is not None:
            if current_list1.value < current_list2.value:
                resul_list.append(list1.remove_head())
                current_list1 = list1.peek()  # Actualizar el puntero
            else:
                resul_list.append(list2.remove_head())
                current_list2 = list2.peek()  # Actualizar el puntero

        # Agregar los elementos restantes de list1
        while not list1.isEmpty():
            resul_list.append(list1.remove_head())

        # Agregar los elementos restantes de list2
        while not list2.isEmpty():
            resul_list.append(list2.remove_head())

        return resul_list

"""
