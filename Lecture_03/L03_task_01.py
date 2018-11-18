# wyklad 3 zad 1

from math import gcd

class MyFraction():
  def __init__(self, numerator, denominator = 1):
        self.numerator = int(numerator / gcd(numerator, denominator))
        self.denominator = int(denominator / gcd(numerator, denominator))
  
  def __add__(self, other):
    if type(other) == int:
      n = self.numerator + self.denominator * other
      d = self.denominator
    else:
      n = self.numerator * other.denominator + self.denominator * other.numerator
      d = self.denominator * other.denominator
    return MyFraction(n, d)
    
  def __eq__(self, other):
    return((self.numerator==other.numerator)*(self.denominator==other.denominator))
  
  def __iadd__(self, other):
    if type(other) == int:
      n = self.numerator + self.denominator * other
      d = self.denominator
    else:
      sn = self.numerator 
      sd =  self.denominator 
      on = other.numerator 
      od = other.denominator
      n = (sn*od + sd*on)
      d = sd * od 
    self.numerator = n / gcd(n,d)
    self.denominator = d / gcd(n,d)
    return self
  
  def __radd__(self, other):
    if type(other) == int:
      n = self.numerator + self.denominator * other
      d = self.denominator
    else:
      n = self.numerator * other.denominator + self.denominator * other.numerator
      d = self.denominator * other.denominator
    return MyFraction(n,d)
  
  def __repr__(self):
    return '{}(numerator={}, denominator={})'.format(
    self.__class__.__name__, self.numerator, self.denominator)
    
  def __str__(self):        
    return '{}(numerator={}, denominator={})'.format(
    self.__class__.__name__, self.numerator, self.denominator)
##### model solution written by thee teacher 

import math


class MyFraction:
	def __init__(self, numerator, denominator=1):
		if isinstance(numerator, MyFraction):
			self.numerator = numerator.numerator
			self.denominator = numerator.denominator
		else:
			self.numerator = numerator
			self.denominator = denominator
		self._reduce()

	def _reduce(self):
		nd_gcd = math.gcd(
			self.numerator, self.denominator
		)
		self.numerator //= nd_gcd
		self.denominator //= nd_gcd

	def _inner_add(self, other):
		other = MyFraction(other)
		# a/b + c/d = (a*d + c*b)/(b*d) = g/h
		a = self.numerator
		b = self.denominator
		c = other.numerator
		d = other.denominator
		g = a*d + c*b
		h = b*d
		return g, h


	def __add__(self, other):
		g, h = self._inner_add(other)
		return MyFraction(g, h)

	def __eq__(self, other):
		return (
			self.numerator == other.numerator
			and self.denominator == other.denominator
		)

	def __iadd__(self, other):
		self.numerator, self.denominator = self._inner_add(other)
		self._reduce()
		return self

	def __radd__(self, other):
		return self + other

	def __repr__(self):
		return '{}(numerator={}, denominator={})'.format(
			self.__class__.__name__,
			self.numerator,
			self.denominator
		)
