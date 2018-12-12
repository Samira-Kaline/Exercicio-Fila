class Fila:
  def __init__(self):
    self.queue = []
  
  def agendamento(self,item):
    if(self.lenfht()>20):
        self.queue.append(item)

  def atendimento(self):
    if not (self.isEmpty()):
      self.queue.pop(0)
  def isEmpty(self):
    return len(self.queue) == 0
  
  def lenght(self):
    return len(self.queue)
