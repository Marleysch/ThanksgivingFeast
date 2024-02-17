import platedecorator

class Turkey(platedecorator.Plate_Decorator):
  '''Extends platedecorator and adds item Turkey onto the plate, updating the description, area, weight, and count attributes'''
  def description(self):
    '''Updates description, checking to see if it is the first item added so the description looks good'''
    if super().description()[-1] == 'e':
      return super().description() + ' with Turkey'
    else:
      return super().description() + ', Turkey'

  def area(self):
    '''Updates the area remaining on the plate'''
    return super().area() - 15

  def weight(self):
    '''Updates the weight left that the plate can hold'''
    return super().weight() - 4

  def count(self):
    return super().count() + 1


class Stuffing(platedecorator.Plate_Decorator):
  '''Extends platedecorator and adds item stuffing onto the plate, updating the description, area, weight, and count attributes'''
  def description(self):
    '''Updates description, checking to see if it is the first item added so the description looks good'''
    if super().description()[-1] == 'e':
      return super().description() + 'with Stuffing'
    else:
      return super().description() + ', Stuffing'

  def area(self):
    '''Updates the area remaining on the plate'''
    return super().area() - 18

  def weight(self):
    '''Updates the weight left that the plate can hold'''
    return super().weight() - 7

  def count(self):
    return super().count() + 1


class Potatoes(platedecorator.Plate_Decorator):
  '''Extends platedecorator and adds item Potatoes onto the plate, updating the description, area, weight, and count attributes'''
  def description(self):
    '''Updates description, checking to see if it is the first item added so the description looks good'''
    if super().description()[-1] == 'e':
      return super().description() + ' with Potatoes'
    else:
      return super().description() + ', Potatoes'

  def area(self):
    '''Updates the area remaining on the plate'''
    return super().area() - 18

  def weight(self):
    '''Updates the weight left that the plate can hold'''
    return super().weight() - 6

  def count(self):
    return super().count() + 1


class GreenBeans(platedecorator.Plate_Decorator):
  '''Extends platedecorator and adds item Green Beans onto the plate, updating the description, area, weight, and count attributes'''
  def description(self):
    '''Updates description, checking to see if it is the first item added so the description looks good'''
    if super().description()[-1] == 'e':
      return super().description() + ' with Green Beans'
    else:
      return super().description() + ', Green Beans'

  def area(self):
    '''Updates the area remaining on the plate'''
    return super().area() - 20

  def weight(self):
    '''Updates the weight left that the plate can hold'''
    return super().weight() - 3

  def count(self):
    return super().count() + 1


class Pie(platedecorator.Plate_Decorator):
  '''Extends platedecorator and adds item Pie onto the plate, updating the description, area, weight, and count attributes'''
  def description(self):
    '''Updates description, checking to see if it is the first item added so the description looks good'''
    if super().description()[-1] == 'e':
      return super().description() + ' with Pie'
    else:
      return super().description() + ', Pie'

  def area(self):
    '''Updates the area remaining on the plate'''
    return super().area() - 19

  def weight(self):
    '''Updates the weight left that the plate can hold'''
    return super().weight() - 8

  def count(self):
    return super().count() + 1