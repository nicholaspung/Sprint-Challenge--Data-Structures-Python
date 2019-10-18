class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    if self.current == self.capacity - 1:
      self.current = 0
    else:
      self.current += 1

  def get(self):
    # If I can store an array
    # Doesn't work if storing 0
    result = []
    for i in range(self.capacity):
      if self.storage[i]:
        result.append(self.storage[i])
    return result