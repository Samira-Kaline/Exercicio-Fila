class ControleAvioes:
  def __init__(self):
    self.fila = []
  
  def adcionaraviao(self,item):
    self.fila.append(item)

  def Autorizar_decolagem(self):
    if not (len(self.fila)==0):
      self.fila.pop(0)
  def PrimeiroAviao(self):
    return self.fila[0]
  
  def ListarAvioes(self):
    return len(self.fila)
