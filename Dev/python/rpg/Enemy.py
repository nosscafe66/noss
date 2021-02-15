class Enemy :
    def info(self):
      return self.ename + "のHPは" + str(self.ep) + "で攻撃力は" + str(self.ea) + "です"

    def __init__(self , ename , ep , ea):
      

      self.ename = ename
      self.ep = ep
      self.ea = ea