using System;
using System.Linq;
using System.IO;

namespace HelloWorld
{
    class Program
    {
        static void MyMethod(string fname)
        {
            Console.WriteLine(fname + " Refsnes");
        }
        static void DefaultValue(string country = "Norway")
        {
            Console.WriteLine(country);
        }
        static int Add(int x, int y)
        {
            return x + y;
        }
        static void NamedArg(string child1, string child2, string child3)
        {
            Console.WriteLine("The youngest child is: " + child3);
        }
        static int PlusMethod(int x, int y)
        {
            return x + y;
        }
        static double PlusMethod(double x, double y)
        {
            return x + y;
        }
        static void checkAge(int age)
        {
            if (age < 18)
            {
                throw new ArithmeticException("Acces denied - You must be at least 18 years old.");
            }
            else
            {
                Console.WriteLine("Access granted - You old enough!");
            }
        }
        static void Main(string[] args)
        {
            // This is a comment
            // Console.WriteLine("Hello World!"); // This is a comment
            // Console.WriteLine("I am Learning C#");
            // Console.WriteLine("It is awesome!");
            // Console.WriteLine(3 + 3);

            /* The code below will print the words Hello World
            to the screen, and it is amazing */
            // Console.Write("Hello World! ");
            // Console.Write("I will print on the same line.");

            // Variables
            // string name = "John";
            // Console.WriteLine(name);
            // Console.WriteLine("Hello " + name);

            // int myNum = 15;
            // Console.WriteLine(myNum);
            // myNum = 20;
            // Console.WriteLine(myNum);

            // int myNum2;
            // myNum2 = 15;
            // Console.WriteLine(myNum2);

            //double myDoubleNum = 5.99D;
            //char myLetter = 'D';
            //bool myBool = true;

            //const int myNum3 = 11;
            //myNum3 = 20; // error

            // string firstName = "John ";
            // string lastName = "Doe";
            // string fullName = firstName + lastName;
            // Console.WriteLine(fullName);

            // int x = 5;
            // int y = 6;
            // Console.WriteLine(x + y);

            // int a = 1, b = 2, c = 3;
            // Console.WriteLine(a + b + c);
            // a = b = c = 1;
            // Console.WriteLine(a + b + c);

            /*
            Names can contain letters, digits and the underscore character
            Names must begin with a letter or underscore
            Names should start with a lowercase letter, and cannot contain whitespace
            Names are case-sensitive
            Reserved words cannot be used as names
            */

            // long l = 21L; float f = 5.75F; double d = 19.99D;
            // float f1 = 35e3F; double d1 = 12E4D;
            // Console.WriteLine(f1);
            // Console.WriteLine(d1);

            // Type Casting
            // Implicit Casting
            // int myInt = 9;
            // double myDouble = myInt;
            // Console.WriteLine(myInt);
            // Console.WriteLine(myDouble);

            // Explicit Casting
            // double myDouble = 9.78;
            // int myInt = (int)myDouble;
            // Console.WriteLine(myDouble);
            // Console.WriteLine(myInt);

            // Type Conversion Methods
            // int myInt = 10;
            // double myDouble = 5.25;
            // bool myBool = true;

            // Console.WriteLine(Convert.ToString(myInt));
            // Console.WriteLine(Convert.ToDouble(myInt));
            // Console.WriteLine(Convert.ToInt32(myDouble));
            // Console.WriteLine(Convert.ToString(myBool));

            // User Input
            // Console.WriteLine("Enter username: ");
            // string userName = Console.ReadLine();
            // Console.WriteLine("Username is : " + userName);

            // C# Math
            // Console.WriteLine(Math.Max(5, 10));
            // Console.WriteLine(Math.Min(5, 10));
            // Console.WriteLine(Math.Sqrt(64));
            // Console.WriteLine(Math.Abs(-4.7));
            // Console.WriteLine(Math.Round(9.99));

            // C# Strings
            // string txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            // Console.WriteLine("The length of the txt string is: " + txt.Length);
            // string txt2 = "Hello World";
            // Console.WriteLine(txt2.ToUpper());
            // Console.WriteLine(txt2.ToLower());

            // C# String Concatenation
            // string firstName = "John ";
            // string lastName = "Doe";
            // string name = firstName + lastName;
            // string nameCon = string.Concat(firstName, lastName);
            // Console.WriteLine(name);
            // Console.WriteLine(nameCon);

            // String Interpolation
            // string firstName = "John";
            // string lastName = "Doe";
            // string name = $"My full name is: {firstName} {lastName}";
            // Console.WriteLine(name);

            // Access Strings
            // string myString = "Hello";
            // Console.WriteLine(myString[0]);
            // Console.WriteLine(myString.IndexOf("e"));

            // string name = "John Doe";
            // int charPos = name.IndexOf("D");
            // string lastName = name.Substring(charPos);
            // Console.WriteLine(lastName);

            // C# Special Characters
            // string txt = "We are the so-called \"Vikings\" from the north.";
            // Console.WriteLine(txt);
            // txt = "It\'s alright.";
            // Console.WriteLine(txt);
            // txt = "The character \\ is called backslash.";
            // Console.WriteLine(txt);

            // C# If .. Else
            // if (20 > 18)
            // {
            //     Console.WriteLine("20 is greater than 18");
            // }

            // // C# The else Statement
            // int time = 20;
            // if (time < 18)
            // {
            //     Console.WriteLine("Good day.");
            // }
            // else
            // {
            //     Console.WriteLine("Good evening.");
            // }

            // C# The else if Statement
            // int time = 22;
            // if (time < 10)
            // {
            //     Console.WriteLine("Good morning.");
            // }
            // else if (time < 20)
            // {
            //     Console.WriteLine("Good day.");
            // }
            // else
            // {
            //     Console.WriteLine("Good evening.");
            // }

            // C# Short Hand If .. Else
            // variable = (condition) ? expressionTrue : expressionFalse;
            // int time = 20;
            // string result = (time < 18) ? "Good day." : "Good evening.";
            // Console.WriteLine(result);

            // C# Switch Statements
            // int day = 4;
            // switch (day)
            // {
            //     case 1:
            //         Console.WriteLine("Monday");
            //         break;
            //     case 2:
            //         Console.WriteLine("Tuesday");
            //         break;
            //     case 3:
            //         Console.WriteLine("Wednesday");
            //         break;
            //     case 4:
            //         Console.WriteLine("Thursday");
            //         break;
            //     case 5:
            //         Console.WriteLine("Friday");
            //         break;
            //     case 6:
            //         Console.WriteLine("Saturday");
            //         break;
            //     case 7:
            //         Console.WriteLine("Sunday");
            //         break;
            //     default:
            //         Console.WriteLine("Looking forward to the Weekend.");
            //         break;
            // }

            // C# While Loop
            // int i = 0;
            // while (i < 5)
            // {
            //     Console.WriteLine(i);
            //     i++;
            // }

            // Do/While Loop
            // int i = 0;
            // do
            // {
            //     Console.WriteLine(i);
            //     i++;
            // }
            // while (i < 5);

            // C# For Loop
            // for (int i = 0; i < 5; i++)
            // {
            //     Console.WriteLine(i);
            // }
            // for (int i = 0; i <= 10; i = i + 2)
            // {
            //     Console.WriteLine(i);
            // }

            // Nested Loops
            // for (int i = 1; i <= 2; ++i)
            // {
            //     Console.WriteLine("Outer: " + i);

            //     for (int j = 1; j <= 3; j++)
            //     {
            //         Console.WriteLine(" Inner: " + j);
            //     }
            // }

            // C# Foreach Loop
            // string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
            // foreach (string i in cars)
            // {
            //     Console.WriteLine(i);
            // }

            // C# Break and Continue
            // for (int i = 0; i < 10; i++)
            // {
            //     if (i == 4)
            //     {
            //         break;
            //     }
            //     Console.WriteLine(i);
            // }
            // for (int i = 0; i < 10; i++)
            // {
            //     if (i == 4)
            //     {
            //         continue;
            //     }
            //     Console.WriteLine(i);
            // }

            // C# Arrays
            // string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
            // int[] myNum = { 10, 20, 30, 40 };
            // Console.WriteLine(cars[0]);
            // cars[0] = "Opel";
            // Console.WriteLine(cars[0]);
            // Console.WriteLine(myNum.Length);

            // Create an array of four elements, and add values later
            // string[] cars = new string[4];

            // // Create an array of four elements and add values right away
            // string[] cars2 = new string[4] { "Volvo", "BMW", "Ford", "Mazda" };

            // // Create an array of four elements without specifying the size
            // string[] cars3 = new string[] { "Volvo", "BMW", "Ford", "Mazda" };

            // // Create an array of four elements, omitting the new keyword, and without specifying the size
            // string[] cars4 = { "Volvo", "BMW", "Ford", "Mazda" };

            // string[] cars5;
            // cars5 = new string[] { "Volvo", "BMW", "Ford" };

            // C# Loop Through Arrays
            // string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
            // for (int i = 0; i < cars.Length; i++)
            // {
            //     Console.WriteLine(cars[i]);
            // }

            // foreach (string i in cars)
            // {
            //     Console.WriteLine(i);    
            // }

            //C# Sort Arrays
            // string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
            // Array.Sort(cars);
            // foreach (string i in cars)
            // {
            //     Console.WriteLine(i);
            // }

            // int[] myNumbers = { 5, 1, 8, 9 };
            // Array.Sort(myNumbers);
            // foreach (int i in myNumbers)
            // {
            //     Console.WriteLine(i);
            // }

            // int[] myNumbers = { 5, 1, 8, 9 };
            // Console.WriteLine(myNumbers.Max());
            // Console.WriteLine(myNumbers.Min());
            // Console.WriteLine(myNumbers.Sum());

            // C# Multidimensional Arrays
            // int[,] numbers = { { 1, 4, 2 }, { 3, 6, 8 } };
            // Console.WriteLine(numbers[0, 2]);
            // numbers[0, 0] = 5;
            // Console.WriteLine(numbers[0, 0]);

            // foreach (int i in numbers)
            // {
            //     Console.WriteLine(i);
            // }

            // for (int i = 0; i < numbers.GetLength(0); i++)
            // {
            //     for (int j = 0; j < numbers.GetLength(1); j++)
            //     {
            //         Console.WriteLine(numbers[i, j]);
            //     }
            // }

            // C# Methods
            // MyMethod("Liam");

            // C# Default Parameter Value
            // DefaultValue("Sweden");
            // DefaultValue("India");
            // DefaultValue();

            // C# Return Values
            // Console.WriteLine(Add(5, 3));

            // C# Named Arguments
            // NamedArg(child3: "John", child1: "Liam", child2: "Liam");

            // C# Method Overloading
            // int myNum1 = PlusMethod(8, 5);
            // double myNum2 = PlusMethod(4.3, 6.25);
            // Console.WriteLine($"Int: {myNum1} Double: {myNum2}");

            // C# Classes and Objects
            // Car myObj = new Car();
            // Console.WriteLine(myObj.color);

            // // C# Class Members
            // myObj.maxspeed = 200;
            // Console.WriteLine(myObj.maxspeed);
            // myObj.fullThrottle();

            // // C# Constructors
            // Console.WriteLine(myObj.model);
            // Car Ford = new Car("Mustang");
            // Console.WriteLine(Ford.model);

            // C# Properties (Get and Set)
            // Car myObj = new Car();
            // myObj.Name = "Liam";
            // Console.WriteLine(myObj.Name);

            // // C# Inheritance
            // myObj.honk();

            // C# Polymorphism
            // Animal myAnimal = new Animal();
            // Animal myPig = new Pig();
            // Animal myDog = new Dog();
            // myAnimal.animalSound();
            // myPig.animalSound();
            // myDog.animalSound();

            // C# Abstraction
            // Pig myPig = new Pig();
            // myPig.animalSound();
            // myPig.sleep();

            // C# Interfaces
            // Cat myCat = new Cat();
            // myCat.animalSound();

            // C# Enum
            // Level myVar = Level.Medium;
            // Console.WriteLine(myVar);

            // int myNum = (int) Level.Medium;
            // Console.WriteLine(myNum);

            // C# Files
            // string writeText = "Hello World!";
            // File.WriteAllText("filename.txt", writeText);

            // string readText = File.ReadAllText("filename.txt");
            // Console.WriteLine(readText);

            // C# Excpetions - Try..Catch
            try
            {
                int[] myNumbers = { 1, 2, 3 };
                Console.WriteLine(myNumbers[10]);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                Console.WriteLine("Something went wrong.");
            }
            finally
            {
                Console.WriteLine("The 'try catch' is finished.");
            }

            checkAge(15);
        }
    }
}
