import math

class Cubic:
  def __init__(self, a, b, c, d):
    self.a = a
    self.b = b
    self.c = c
    self.d = d

  def getRoots(self):
    f = (3*self.c/self.a - self.b**2/self.a**2)/3

    g = (2*self.b**3/self.a**3 -   \              
         9*self.b*self.c/self.a**2 \
         + 27*self.d/self.a)/27

    h = g**2/4 + f**3/27

    if f == 0 and g == 0 and h == 0:
      x1, x2, x3 = [-(self.d/self.a)**(1/3)]*3

    elif h > 0:
      r = -(g/2) + h**0.5
      if r < 0:
        s = -abs(r)**(1/3)
      else:
        s = r**(1/3)
      t = -(g/2) - h**0.5
      if t < 0:
        u = -abs(t)**(1/3)
      else:
        u = t**(1/3)
      x1 = (s+u)-(self.b/(3*self.a))
      x2 = complex(-(s+u)/2 - (self.b/(3*self.a)),
                   ((s-u)*3**0.5)/2)
      x3 = complex(-(s+u)/2 - (self.b/(3*self.a)),
                   -((s-u)*3**0.5)/2)

    else:
      i = ((g**2/4)-h)**0.5
      j = i**(1/3)
      k = math.acos(-(g/(2*i)))
      m = math.cos(k/3)
      n = math.sqrt(3) * math.sin(k/3)
      p = -(self.b/(3*self.a))
      x1 = 2*j*math.cos(k/3)-(self.b/(3*self.a))
      x2 = -j*(m+n)+p
      x3 = -j*(m-n)+p

    return x1, x2, x3


def printRoots(cubic):
  for index, root in enumerate(cubic.getRoots()):
    print("x{0}: {1}".format(index+1, root))

printRoots(Cubic(2,  -4, -22, 24))
printRoots(Cubic(3, -10,  14, 27))
printRoots(Cubic(1,   6,  12,  8))
