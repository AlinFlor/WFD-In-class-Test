import unittest
from PartA import Pet, Dog

class TestInstanceOfClass(unittest.TestCase):
    def test_pet_instance(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        self.assertIsInstance(pet, Pet)

    def test_dog_instance(self):
        dog = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        self.assertIsInstance(dog, Dog)

    def test_dog_not_pet_instance(self):
        dog = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        self.assertNotIsInstance(dog, Pet)

class TestNotInstanceOfClass(unittest.TestCase):
    def test_pet_not_dog_instance(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        self.assertNotIsInstance(pet, Dog)

    def test_dog_not_pet_instance(self):
        dog = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        self.assertNotIsInstance(dog, Pet)

    def test_pet_not_list_instance(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        self.assertNotIsInstance(pet, list)

class TestIdenticalObjects(unittest.TestCase):
    def test_identical_pet_objects(self):
        pet1 = Pet("Buddy", 3, "Male", "P001", "Alice")
        pet2 = Pet("Buddy", 3, "Male", "P001", "Alice")
        self.assertEqual(pet1, pet2)

    def test_identical_dog_objects(self):
        dog1 = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        dog2 = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        self.assertEqual(dog1, dog2)

    def test_non_identical_pet_objects(self):
        pet1 = Pet("Buddy", 3, "Male", "P001", "Alice")
        pet2 = Pet("Buddy", 4, "Male", "P001", "Alice")
        self.assertNotEqual(pet1, pet2)

class TestUpdateMethods(unittest.TestCase):
    def test_update_pet_name(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        new_name = "Max"
        pet.update_name(new_name)
        self.assertEqual(pet.name, new_name)

    def test_update_pet_age(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        new_age = 5
        pet.update_age(new_age)
        self.assertEqual(pet.age, new_age)

    def test_update_pet_gender(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        new_gender = "Female"
        pet.update_gender(new_gender)
        self.assertEqual(pet.gender, new_gender)

    def test_update_pet_id(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        new_id = "P002"
        pet.update_id(new_id)
        self.assertEqual(pet.id, new_id)

    def test_update_pet_owner(self):
        pet = Pet("Buddy", 3, "Male", "P001", "Alice")
        new_owner = "Bob"
        pet.update_owner(new_owner)
        self.assertEqual(pet.owner, new_owner)

    def test_update_dog_breed(self):
        dog = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        new_breed = "Labrador"
        dog.update_breed(new_breed)
        self.assertEqual(dog.breed, new_breed)

    def test_update_dog_is_hypoallergenic(self):
        dog = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)
        new_is_hypoallergenic = False
        dog.update_is_hypoallergenic(new_is_hypoallergenic)
        self.assertEqual(dog.is_hypoallergenic, new_is_hypoallergenic)

def main():
    unittest.main()

if __name__ == '__main__':
    main()