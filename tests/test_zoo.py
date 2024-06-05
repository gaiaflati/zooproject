import unittest
from unittest import TestCase
from src.zoo import Zoo,Zookeper,Fence,Animal

class TestZoo(TestCase):
    def test_animal_habitat(self):
      
      zookeeper_1: Zookeper= Zookeper(name="Gianni",surname="Rossi", id=1)
      fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
      animal_1: Animal = Animal(name="Pluto", species="Cane", age=5, height=5.0,width=1.0,preferred_habitat="giungla")
      zookeeper_1.add_animal(animal_1,fence_1)
      result: int =len(fence_1.animals)
      message: str= f"Error: the function add_animal should not add self.animal_1 into self.fence_1"

      self.assertEqual(result, 0, message)
    


    def test_animal_dimension(self):
       zookeeper_1: Zookeper= Zookeper(name="Gianni",surname="Rossi", id=1)
       fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
       animal_1: Animal = Animal(name="Pluto", species="Cane", age=5, height=300.0,width=1.0,preferred_habitat="savana")
       zookeeper_1.add_animal(animal_1,fence_1)
       result: int =len(fence_1.animals)
       message: str= f"Error: the function add_animal should not add self.animal_1 into self.fence_1"
       
       self.assertEqual(result, 0, message)
    

    def test_animal_remove(self):
       zookeeper_1: Zookeper= Zookeper(name="Gianni",surname="Rossi", id=1)
       fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
       animal_1: Animal = Animal(name="Pluto", species="Cane", age=5, height=300.0,width=1.0,preferred_habitat="savana")
       animal_2: Animal = Animal(name="Pippo", species="gatto", age=5, height=20.0,width=1.0,preferred_habitat="casa")
       zookeeper_1.add_animal(animal_2,fence_1)
       zookeeper_1.remove_animal(animal_2,fence_1)
       result: int = len(fence_1.animals)
       message: str= f"Error: the function remove_animal should remove animal_2 from fence_1 "

       self.assertEqual (result, 0, message)

    def test_animal_width(self):
        zookeeper_1: Zookeper= Zookeper(name="Gianni",surname="Rossi", id=1)
        fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
        animal_1: Animal = Animal(name="Pluto", species="Cane", age=5, height=100.0,width=1.0,preferred_habitat="savana")
        zookeeper_1.add_animal(animal_1,fence_1)
        zookeeper_1.feed(animal_1)
        result: int = animal_1.width
        message: str= f"Error: should not update animal_1.width cause there's no space in fence_1 to feed animal_1 "

        self.assertEqual(result, 1.0, message)

    def test_animal_height(self):
        zookeeper_1: Zookeper= Zookeper(name="Gianni",surname="Rossi", id=1)
        fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
        animal_1: Animal = Animal(name="Pluto", species="Cane", age=5, height=100.0,width=1.0,preferred_habitat="savana")
        zookeeper_1.add_animal(animal_1,fence_1)
        zookeeper_1.feed(animal_1)
        result: int = animal_1.height
        message: str= f"Error: should not update animal_1.height cause there's no space in fence_1 to feed animal_1 "

        self.assertEqual(result, 100.0, message)


if __name__ == '__main__' :
    unittest.main()