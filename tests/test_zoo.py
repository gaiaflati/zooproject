import unittest
from unittest import TestCase
from src.zoo import Zoo,Zookeper,Fence,Animal

class TestZoo(TestCase):

   def test_animal_habitat(self):
      
      zookeeper_1: Zookeper= Zookeper(name="Gianni",surname="Rossi", id=1)
      fence_1: Fence = Fence(area=100, temperature=25.0, habitat="savana")
      animal_1: Animal = Animal(name="Pluto", species="Cane", age=5, height=5.0,width=1.0,preferred_habitat="savana")
      zookeeper_1.add_animal(animal_1,fence_1)
      result: int =len(fence_1.animals)
      message: str= f"Error: the function add_animal should not add self.animal_1 into self.fence_1"

      self.assertEqual(result, 0, message)


      