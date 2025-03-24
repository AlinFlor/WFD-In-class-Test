class Pet:
    def __init__(self, name: str, age: int, sex: str, pet_id: str, owner_name: str):
        self.name = name
        self.age = age
        self.sex = sex
        self.pet_id = pet_id
        self.owner_name = owner_name

    def print_attributes(self):
        """Prints all initialization attributes of the Pet."""
        print(f"Name: {self.name}, Age: {self.age}, Sex: {self.sex}, Pet ID: {self.pet_id}, Owner: {self.owner_name}")

    def update_name(self, new_name: str):
        if isinstance(new_name, str):
            self.name = new_name
        else:
            print("Type error: Name must be a string.")

    def update_age(self, new_age: int):
        if isinstance(new_age, int):
            self.age = new_age
        else:
            print("Type error: Age must be an integer.")

    def update_sex(self, new_sex: str):
        if isinstance(new_sex, str):
            self.sex = new_sex
        else:
            print("Type error: Sex must be a string.")

    def update_pet_id(self, new_pet_id: str):
        if isinstance(new_pet_id, str):
            self.pet_id = new_pet_id
        else:
            print("Type error: Pet ID must be a string.")

    def update_owner_name(self, new_owner_name: str):
        if isinstance(new_owner_name, str):
            self.owner_name = new_owner_name
        else:
            print("Type error: Owner name must be a string.")

class Dog(Pet):
    def __init__(self, name: str, age: int, sex: str, pet_id: str, owner_name: str, breed: str, is_service_dog: bool):
        super().__init__(name, age, sex, pet_id, owner_name)
        self.breed = breed
        self.is_service_dog = is_service_dog

    def print_attributes(self):
        """Prints all attributes of the Dog including inherited ones."""
        super().print_attributes()
        print(f"Breed: {self.breed}, Service Dog: {self.is_service_dog}")

    def update_breed(self, new_breed: str):
        if isinstance(new_breed, str):
            self.breed = new_breed
        else:
            print("Type error: Breed must be a string.")

    def update_is_service_dog(self, new_is_service_dog: bool):
        if isinstance(new_is_service_dog, bool):
            self.is_service_dog = new_is_service_dog
        else:
            print("Type error: is_service_dog must be a boolean.")

my_pet = Pet("Buddy", 3, "Male", "P001", "Alice")
my_dog = Dog("Max", 5, "Male", "D001", "Bob", "Golden Retriever", True)

print("Pet Attributes:")
my_pet.print_attributes()

print("\nDog Attributes:")
my_dog.print_attributes()

my_pet.update_name("Charlie")
my_pet.update_age(4)

my_dog.update_breed("Labrador")
my_dog.update_is_service_dog(False)

print("\nUpdated Pet Attributes:")
my_pet.print_attributes()

print("\nUpdated Dog Attributes:")
my_dog.print_attributes()