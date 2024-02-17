import plate

class SmallPlate(plate.Plate):
  '''Extends interface Plate to make small plate with a description, area, weight, and count
  '''
  def description(self):
    '''Return description of plate'''
    return 'Sturdy 10 inch paper plate'

  def area(self):
    '''Returns area of plate'''
    return 78

  def weight(self):
    '''Returns weight of plate'''
    return 32

  def count(self):
    '''Returns number of items on plate'''
    return 0