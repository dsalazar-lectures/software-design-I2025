# Laboratory #3

- Student: Josué Badilla Paredes
- Software Design Patter: Singleton


**Description:**

Singleton is a creational software design pattern first defined in the original
23 set of software design patterns by the Gang of Four (GoF). It insures
that during the execution of a program, there will exist just 1 instance of a 
certain class. It is used in cases when by any means, there must not exist more 
than 1 instance of such class.


To access this single instance, the class must provide a global access point to
it. Normally this point is a static method named `get_instance()`. This is quite
useful, because this single instance can be accessed in multiple parts of
a program, making some services more accecible.


# Implementation:

Using concepts of Object-Orient Programming, it is possible to implement the
behavior of this pattern.


First, the class constructor must be private, so it is only available to use by
the class members, limiting creating instances by other entities because only
this class can create instances of itself.


The only way to create a new instance is by using a public class method called 
`get_instance()`. Because it is a class member, it can call the private constructor.
When calling this method, it checks an instance of the class has been created before.
If not, it created that instance first, else, it will only return that instance.
Normally this instance is stored in a static variable inside the class.


**Advantages:**
- Resource efficiency of main memory by just providing a single instance of a certain class.
- Centralized control and consistency by providing a single access point to certain data and resources of a program. 


**Disadvantages:**
- It may be considered controversial because basically the singleton instance is a global variable.
- Can increase the complexity of unit testing because the instances are created by teh class itself.
- Can introduce concurrency issues in multi-threaded applications (shared resources).
