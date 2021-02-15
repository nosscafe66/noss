class Damage:
    def info(self):
      return self.dname + 'は攻撃力' + str(self.da) + 'です'


    def __init__(self , dname , da ):
      
      
       
       self.dname = dname
       self.da = da