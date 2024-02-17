import plate

class Small_Plate(plate.Plate):
  '''Extends interface Plate to make small plate with a description, area, weight, and count
  '''
  def description(self):
    '''Return description of plate'''
    return "Small Sturdy plate"

  def area(self):
    return 78

  def weight(self):
    return 32

  def count(self):
    return 0

class Large_Plate(plate.Plate):
  '''Extends interface Plate to make large plate with a description, area, weight, and count
  '''
  def description(self):
    '''Return description of plate'''
    return "Large Flimsy Plate"

  def area(self):
    return 113

  def weight(self):
    return 24

  def count(self):
    return 0