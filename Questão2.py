class Queue:
  def __init__(self):
    self.queue = []
  
  def enqueue(self,item):
    self.queue.append(item)

  def desenqueue(self):
    if not (self.isEmpty()):
      self.queue.pop(0)
  def isEmpty(self):
    return len(self.queue) == 0
  
  def lenght(self):
    return len(self.queue)
