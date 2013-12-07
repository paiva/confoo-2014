  def getRoots(self):
    self._f()
    self._g()
    self._h()


    def __getattr__(self, name):
    calcName = "_" + name

    if hasattr(self, calcName):
      getattr(self, calcName)()
      return getattr(self, name)
    else:
      raise AttributeError
    
    def _f(self):
    self.f = (3*self.c/self.a - self.b**2/self.a**2)/3

    def _g(self):
    self.g = (2*self.b**3/self.a**3 - 9*self.b*self.c/self.a**2 + 27*self.d/self.a)/27

    def _h(self):
    self.h = self.g**2/4 + self.f**3/27

    def _r(self):
    self.r = -(self.g/2) + self.h**0.5
    return x1, x2, x3
