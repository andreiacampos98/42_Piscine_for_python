from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
print(King.__mro__)
print(Joffrey.family_name)
print(Joffrey.is_alive)
Joffrey.die()
print(Joffrey.is_alive)

Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)


Eu = King("Joffrey", "Campos")
print(Eu.is_alive)
print(Eu.first_name)
