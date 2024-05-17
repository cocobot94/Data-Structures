class minHeap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0

    def parentIndex(self, i):
        return int((i - 1) / 2)

    def leftChildIndex(self, i):
        return (i * 2) + 1

    def rigthChildIndex(self, i):
        return (i * 2) + 2

    def isLeaf(self, i):
        if self.leftChildIndex(i) >= self.size and self.rigthChildIndex(i) >= self.size:
            return True
        return False

    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp

    def insert(self, element):
        if element == None:
            return
        self.heap.append(element)
        current = self.size
        while self.heap[current] < self.heap[self.parentIndex(current)]:
            self.swap(current, self.parentIndex(current))
            current = self.parentIndex(current)
        self.size += 1
        return

    def extractMin(self):
        if self.size == 0:
            return
        popped = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.minHeapfy(0)
        self.heap.pop()
        return popped

    def minHeapfy(self, i):
        if not self.isLeaf(i):
            while (
                self.heap[i] > self.heap[self.leftChildIndex(i)]
                or self.heap[i] > self.heap[self.rigthChildIndex(i)]
            ):
                if (
                    self.heap[self.leftChildIndex(i)]
                    < self.heap[self.rigthChildIndex(i)]
                ):
                    self.swap(i, self.leftChildIndex(i))
                    self.minHeapfy(self.leftChildIndex(i))
                else:
                    self.swap(i, self.rigthChildIndex(i))
                    self.minHeapfy(self.rigthChildIndex(i))

    def extract_k_min(self, k):
        cont = 0
        popl = []
        while cont != k:
            popl.append(self.extractMin())
            cont += 1
        popped = popl.pop()
        if len(popl) > 0:
            for item in popl:
                self.insert(item)
        del popl
        return popped

    def __quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        rigth = [x for x in arr if x > pivot]
        return self.__quick_sort(left) + middle + self.__quick_sort(rigth)

    def sort(self):
        return self.__quick_sort(self.heap)

    def __str__(self) -> str:
        return str(self.heap)


if __name__ == "__main__":
    minheap = minHeap()
    minheap.insert(5)
    minheap.insert(10)
    minheap.insert(12)

    print()
    minheap.insert(9)
    minheap.insert(15)

    print()
    minheap.insert(1)
    minheap.insert(4)

    print()
    print(minheap.extractMin())
    # minheap.insert(44)

    print(minheap)
    print()
    print(minheap.extractMin())
    minheap.insert(44)
    minheap.insert(36)
    minheap.insert(77)
    minheap.insert(66)
    minheap.insert(6)
    print()
    print(minheap)
    print(minheap.extract_k_min(6))
    print(minheap)
    print(minheap.sort())
    print(minheap)
