
class Plant:  # Растение
  edible = False

  def __init__(self, name):
    self.name = name

class Animal:  # Животное
  alive = True
  fed = False

  def __init__(self, name ):
    self.name = name

  def eat(self, food:Plant):

    if food.edible:
      self.fed = True
      print(f'{self.name} съел {food.name}')
    else:
      self.alive = False
      print(f"{self.name} не стал есть {food.name}" )


class Mammal(Animal):  # Млекопитающее

  pass

class Predator(Animal):  # Хищник

  pass


class Flower(Plant):
  pass

class Fruit(Plant):

  def __init__(self, name):
    super().__init__(name)
    self.edible = True




a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)



# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.


