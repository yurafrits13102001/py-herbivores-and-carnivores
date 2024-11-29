class Animal:
    alive = []  # Class attribute to track all alive animals

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.hidden = False
        if self.health > 0:
            Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    @classmethod
    def update_alive(cls):
        cls.alive = [animal for animal in cls.alive if animal.health > 0]


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, prey):
        if isinstance(prey, Herbivore) and not prey.hidden:
            prey.health -= 50
            if prey.health <= 0:
                Animal.update_alive()



