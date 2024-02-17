import abc
import plate

class Plate_Decorator(plate.Plate, abc.ABC):
  def __init__(self, p):
    self._plate = p

  def description(self):
    return self._plate.description()

  def area(self):
    return self._plate.area()

  def weight(self):
    return self._plate.weight()

  def count(self):
    return self._plate.count()