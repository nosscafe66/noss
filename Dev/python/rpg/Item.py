class Item :
    def info(self):
      return "武器は" + self.iname + "で攻撃力は" + str(self.ia) + "です"

    def __init__(self , iname , ia):
      

      self.iname = iname
      self.ia = ia