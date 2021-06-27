class vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return vector(self.a + other.a, self.b + other.b)

   def __sub__(self,other):
      return vector(self.a - other.a, self.b - other.b)
   
   def scalar_product(self,other):
      return  self.a * other.a + self.b * other.b
   
   def moldlen(self):
       return ( self.a**2 + self.b**2 ) ** 0.5

   def __lt__(self,other):
       tmp_1=vector.moldlen(self)
       tmp_2=vector.moldlen(other)
       if(tmp_1 < tmp_2):
           return True
       else:
           return False
   
   def __gt__(self, other):
       tmp_1=vector.moldlen(self)
       tmp_2=vector.moldlen(other)
       if(tmp_1 > tmp_2):
           return True
       else:
           return False
   
   def __eq__(self,other):
       if(self.a == other.a and self.b == other.b):
           return True
       else:
           return False
    