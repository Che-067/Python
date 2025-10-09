
'''
 Assignment 1: Design Your Own Class! 🏗️


1) Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
2) Add attributes and methods to bring the class to life!
3) Use constructors to initialize each object with unique values.
4) Add an inheritance layer to explore polymorphism or encapsulation.

Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()).
 However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗,
   while Plane.move() prints "Flying" ✈️).

'''

class oppo_A53S:
  def my_phone(self):
    print('I love oppo-A53S!')

  def __init__(self,Ram,Rom):
    self.Ram = Ram
    self.Rom = Rom

my_oppo = oppo_A53S("8_GB","256_GB")

print(f'I like oppo_A53S because of it Ram and Rom: {my_oppo.Ram} and {my_oppo.Rom}')

my_oppo.my_phone()

class ferrari:
  def move(self):
    return 'das ferrari ist zu klein auch fast'

class hund:
  def move(self):
    return 'der is hund ist fast und schon'

for cologne in [ferrari(),hund()]:
  print(cologne.move())
   

class zakiru:
  counter = 5000

  def wazeefa(self):
    print('zakiru yana wazeefa kullum')

dala_ilu = zakiru()
print(f"zakiru yana karanta dala_ilu sau {dala_ilu.counter} a sa'a daya")
dala_ilu.wazeefa()
