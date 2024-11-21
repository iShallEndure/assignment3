class AmortizedQueue:
    def __init__(self):
        self.queue = []
        self.front = 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.front == len(self.queue):
            return None  # Queue is empty
        item = self.queue[self.front]
        self.front += 1
        return item

    def move_to_front(self):
        self.queue = self.queue[self.front:]
        self.front = 0

    def display(self):
        print(f"Queue: {self.queue[self.front:]}")

# Example usage
queue = AmortizedQueue()
operations = ['enqueue'] * 10 + ['dequeue'] * 5 + ['move_to_front'] + ['enqueue'] * 5

for operation in operations:
    if operation == 'enqueue':
        queue.enqueue(1)  # Arbitrary value
    elif operation == 'dequeue':
        queue.dequeue()
    elif operation == 'move_to_front':
        queue.move_to_front()
    queue.display()

# Amortized cost calculation
num_operations = len(operations)
total_cost = 10 * 1 + 5 * 1 + 1 * 5  # 10 enqueue, 5 dequeue, 1 move_to_front with 5 items
amortized_cost = total_cost / num_operations
print(f"Amortized cost per operation: {amortized_cost}")