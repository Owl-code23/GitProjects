using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace HelloWorld
{
    public class Vehicle
    {
        public string brand = "Ford";
        public void honk()
        {
            Console.WriteLine("Tuut, tuut!");
        }
    }
    public class Car : Vehicle
    {
        public string color = "red";
        public string model;
        public int maxspeed;
        private string test = "private";
        private string name;
        public string Name
        {
            get; set;
        }
        public Car()
        {
            model = "Mustang";
        }
        public Car(string modelName)
        {
            model = modelName;
            Console.WriteLine(test);
        }
        public void fullThrottle()
        {
            Console.WriteLine("The car is going as fast as it can!");
        }

    }
}