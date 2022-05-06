
class Pet:
  def __init__(self, n, a, h, p) -> None:
      self.name = n
      self.age = a
      self.hunger = h
      self.playful = p

  # getters
  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_hunger(self):
    return self.hunger

  def get_playful(self):
    return self.playful

  # setters

  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age

  def set_hunger(self, hunger):
    self.hunger = hunger

  def set_playful(self, play):
    self.playful = play