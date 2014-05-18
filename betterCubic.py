# Credits: Peter Sutton, The University of Manchester

import math

class Cubic: 

"""
    Constructor
"""
  def __init__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d

"""
    getRoots Method
"""
  def getRoots(self):
    
    if self.f == 0 and self.g == 0 and self.h == 0:
      x1, x2, x3 = [-(self.d/self.a)**(1/3)]*3

    elif self.h > 0:
      x1 = (self.s+self.u)-(self.b/(3*self.a))
      x2 = complex(-(self.s+self.u)/2 - (self.b/(3*self.a)),
                   ((self.s-self.u)*3**0.5)/2)
      x3 = complex(-(self.s+self.u)/2 - (self.b/(3*self.a)),
                   -((self.s-self.u)*3**0.5)/2)

    else:
      x1 = 2*self.j*math.cos(self.k/3)-(self.b/(3*self.a))
      x2 = -self.j*(self.m+self.n)+self.p
      x3 = -self.j*(self.m-self.n)+self.p

    return x1, x2, x3

"""
    getAttribute Class Customization
"""
  def __getattr__(self, name):
    calcName = "_" + name

  if hasattr(self, calcName):
    getattr(self, calcName)()
    return getattr(self, name)
  else:
    raise AttributeError
    
"""
    f Calculation Method
"""    
  def _f(self):
    self.f = (3*self.c/self.a - self.b**2/self.a**2)/3

"""
    g Calculation Method
"""
  def _g(self):
    self.g = (2*self.b**3/self.a**3 - 9*self.b*self.c/self.a**2 + 27*self.d/self.a)/27

"""
    h Calculation Method
"""
  def _h(self):
    self.h = self.g**2/4 + self.f**3/27

"""
    r Calculation Method
"""
  def _r(self):
    self.r = -(self.g/2) + self.h**0.5

"""
    s Calculation Method
"""
  def _s(self):
    self.s = -abs(self.r)**(1/3) if self.r < 0 else self.r**(1/3)

"""
    t Calculation Method
"""
  def _t(self):
    self.t = -(self.g/2) - self.h**0.5

"""
    u Calculation Method
"""
  def _u(self):
    self.u = -abs(self.t)**(1/3) if self.t < 0 else self.t**(1/3)

"""
    i Calculation Method
"""
  def _i(self):
    self.i = ((self.g**2/4)-self.h)**0.5

"""
    j Calculation Method
"""
  def _j(self):
    self.j = self.i**(1/3)
