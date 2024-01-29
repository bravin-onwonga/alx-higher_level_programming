## Python - Classes and Objects
Python is programming created by Guido vas Rossum in 1991 on the principle of '```first-class everything```'.
This principle means that every object in python is treated the same way.
In his words: Everything is treated the same way, eveything is a class: function and methods are values just like lists, integers or floats. Each of these are instances of their corresponding classes.

The example used in the resources is list.
- When you use append or pop, this are all instances of the list class.
- Similar to exceptions where TypeError, NameError are all instances of the Exception Class.
- When you initialize and integer you are creating an instance of the ```int``` class.

### NOTES
**Why Python programming is awesome**
- *Python is simple*: The language structure is in such a way that it encourages readability by using white spaces. This is contrary to structured language such as C that maybe hard to read and use more lines of code.
A good example is when reading input from the terminal. I c you would have to use a variadic function while in python you only need the args key word.
- *Beginner friendly*: The first language I learnt was python and to be precise using the django framework to build we applications. It is easy to learn since its principle design was to be easy and enjotable to use
- *Versatile*: Python is an ever growing language and has different frameworks to use the language to achieve various concepts i.e. ```django``` and ```flask``` for web app development, ```Pygame``` and ```Pyglet``` for game development, ```Pandas and Matplotlib``` for Data Analysis and Visualization. It is also used in ```Machine Learning and AI``` and ```Automation and Scripting```

**Class**
A ```class``` is code template which wraps and combines your data and functionality inside and ```object```.
An ```object``` is an instance of a class. The contain data (```fields```) and functions (```methods```) which manipulates the data.
An ```instance``` is used to refer to an individual object of a certain class.

Very confusing right? An analogy to help is think of a fruit. That is our class, and all the different fruits (e.g. Mango, Pineapple, Oranges) are considered instances of fruit.

Now lets say our fruit is an orange and it has it characteristics. Let's call these characteristics ```attributes```. This attributes can be color, size, taste.

class Fruits:
	def __init__(self, name, color, number):
		self.name = name
		self.color = color
		self.number = number

	total_fruits = 0

Similarly our class and its objects can have their own attributes.

**Class attribute**
This are attributes of the class. This attributes are ```sharable``` and changing them in one object will have an effect on all other objects in that specific class.
In the example above ```total_fruits``` is a class attribute

***NOTE ABOUT SELF AND INIT***

 The ```___init____``` method is used in initializing the values you want to pass to your ```object```.

The ```self``` is a variable that refers to the object itself. You will have to use it in all your ```objects```(instances of the class you have created). You don't need to pass a value for it as the intepreter will provide value for it.

If I create an object ```def orange(self)``` the ```self``` variable will expand it to ```Fruits(orange(name, color, number))```

def orange(self):
	print("My type is", self.name)
	print("My color is", self.color)
	print("There are " + self.number + " " + self.name + "s.")

This way I can create an instance of the class ```Fruits```

o = Fruits(orange, orange, 12)
o.orange()

**Instance attributes**
This are attributes of an instance of the class(```object```).
They are not sharable and and example are the attributes initialized in the ```__init__``` object

**Setters**
If you notices I

