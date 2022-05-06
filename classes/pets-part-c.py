
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


class Dog(Pet):
  def __init__(self, n, a, h, p, breed, favorite_toy) -> None:
      super().__init__(n, a, h, p)

      self.breed = breed
      self.favorite_toy = favorite_toy

  def wants_to_play(self):
    if self.playful:
      return f"Dog wants to play with {self.favorite_toy}"
    else:
      return f"Dog does not want to play"


class Cat(Pet):
  def __init__(self, n, a, h, p, place) -> None:
      super().__init__(n, a, h, p)
      self.favorite_place_to_sit = place

  def wants_to_sit(self):
    if not self.playful:
      print("The cat wants to sit", self.favorite_place_to_sit)
    else:
      print("The cat wants to play")

dog = Dog("Lee", 12, False, True, "German Shephard", "Bone Stick")
print(dog.wants_to_play())
cat = Cat("Fluffy", 10, False, False, "Couch")
cat.wants_to_sit()