class Animal:
  def falar(self):
    print("Este animal faz um som!")
  
class Cachorro(Animal):
  def falar(self):
    print("O cachorro late!")

class Gato(Animal):
  def falar(self):
    print("O gato mia!")

cachorro = Cachorro()
cachorro.falar()

gato = Gato()
gato.falar()

