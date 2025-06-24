using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace HelloWorld
{
    abstract public class Animal
    {
        public abstract void animalSound();
        public void sleep()
        {
            Console.WriteLine("Zzz");
        }
    }
    public class Pig : Animal
    {
        public override void animalSound()
        {
            Console.WriteLine("The Pig says: wee wee");
        }
    }
    public class Dog : Animal
    {
        public override void animalSound()
        {
            Console.WriteLine("The dog says: bow wow");
        }
    }
    interface IAnimal
    {
        void animalSound();
    }
    public class Cat : IAnimal
    {
        public void animalSound()
        {
            Console.WriteLine("The cat says: MMMMMMM");
        }
    }
}