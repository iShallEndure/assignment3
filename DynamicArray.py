class DynamicArray:
    def __init__(self):
        self.array = [None]
        self.size = 0
        self.capacity = 1
        self.total_cost = 0

    def insert(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1
        self.total_cost += 1  # Cost of insertion

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        self.total_cost += self.size  # Cost of copying elements to new array

    def get_amortized_cost(self):
        return self.total_cost / self.size if self.size else 0

# Simulate insertions
dynamic_array = DynamicArray()
posts = range(20)  # Simulate 20 posts

for post in posts:
    dynamic_array.insert(post)

print(f"Total Cost: {dynamic_array.total_cost}")
print(f"Amortized Cost per Insertion: {dynamic_array.get_amortized_cost()}")