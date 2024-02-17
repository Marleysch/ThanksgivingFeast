import plate

class LargePlate(plate.Plate):
  '''Extends interface Plate to make large plate with a description, area, weight, and count
  '''
  def description(self):
    '''Return description of plate'''
    return 'Flimsy 12 inch paper plate'

  def area(self):
    '''Returns area of plate'''
    return 113

  def weight(self):
    '''Returns weight of plate'''
    return 24

  def count(self):
    '''Returns number of items on plate'''
    return 0