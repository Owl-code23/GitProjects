fun myFunction(fname: String) {
        println(fname + " Doe")
    }

fun myFunction2(x: Int): Int {
    return (x + 5)
}

fun myFunctions3(x: Int, y: Int) = x + y

class Car {
    var brand = ""
    var model = ""
    var year = 0
}

class Car2 (var brand: String, var model: String, var year: Int) {
    fun drive() {
        println("Wrooom!")
    }

    fun speed(maxSpeed: Int) {
        println("Max speed is: " + maxSpeed)
    }
}

open class MyParentClass {
    val x = 5
}

class MyChildClass: MyParentClass() {
    fun myFunction() {
        println(x)
    }
}

fun main() {

    // This is a comment
    /* The code below will print the words Hello World
    to the screen, and it is amazing */
    // print("Hello, World!")
    // println("I am learing Kotlin.") // This is a comment

    // var name: String = "John" // var can be changed/modified
    // val birthyear = 1975 // val cannot be changed
    // println(name)
    // println(birthyear)

    // var test: String
    // test = "test"
    // println(test)

    /*
    Names can contain letters, digits, underscores, and dollar signs
    Names should start with a letter
    Names can also begin with $ and _
    Names are case sensitive
    Names should start with a lowercase letter and it cannot contain whitespace
    Reserved words cannot be used as names */

    // Kotlin Data Types
    // val myNum: Int = 5
    // val myDoubleNum = 5.99
    // val myLetter: Char = 'D'
    // val myBoolean = true
    // val myText = "Hello"

    // Type conversion
    // val x: Int = 5
    // val y: Long = x.toLong()
    // println(y)

    // Kotlin Strings
    // var txt: String = "Hello"
    // println(txt[0])
    // println(txt[2])
    // println(txt.length)
    // println(txt.uppercase())
    // println(txt.lowercase())
    // println(txt.indexOf("l"))

    // var txt1 = "Hello World";
    // var txt2 = "Hello World";
    // println(txt1.compareTo(txt2));

    // var firstName = "John "
    // var lastName = "Doe"
    // println(firstName.plus(lastName))
    // println("My name is $firstName $lastName")

    // Kotlin If ... Else
    // val time = 22
    // if (time < 10) {
    //     println("Good morning.")
    // } else if (time < 20) {
    //     println("Good day.")
    // } else {
    //     println("Good evening.")
    // }

    // val greeting = if (time < 18) {
    //     "Good day."
    // } else {
    //     "Good evening."
    // }
    // println(greeting)

    // val greeting2 = if (time < 18) "Good day." else "Good evening."
    // println(greeting2)

    // Kotlin When
    // val day = 4
    // val result = when (day) {
    //     1 -> "Monday"
    //     2 -> "Tuesday"
    //     3 -> "Wednesday"
    //     4 -> "Thursday"
    //     5 -> "Friday"
    //     6 -> "Saturday"
    //     7 -> "Sunday"
    //     else -> "Invalid day."
    // }
    // println(result)

    //Kotlin While Loop
    // var i = 0
    // while (i < 5) {
    //     println(i)
    //     i++
    // }

    // // Do..While Loop
    // i = 0
    // do {
    //     println(i)
    //     i++
    // } while (i < 5)

    //Kotlin Break and Continue
    // var i = 0
    // while (i < 10) {
    //     println(i)
    //     i++
    //     if (i == 4){
    //         break
    //     }
    // }
    // i = 0
    // while (i < 10) {
    //     if (i == 4) {
    //         i++
    //         continue
    //     }
    //     println(i)
    //     i++
    // }

    // Kotlin Arrays
    // val cars = arrayOf("Volvo", "BMW", "Ford", "Mazda")
    // println(cars[0])
    // cars[0] = "Opel"
    // println(cars[0])
    // println(cars.size)
    // if ("Volvo" in cars) {
    //     println("It exists!")
    // } else {
    //     println("It does not exist.")
    // }

    // for (x in cars) {
    //     println(x)
    // }

    // for (chars in 'a'..'x'){
    //     println(chars)
    // }

    // for (nums in 5..15) {
    //     println(nums)
    // }

    // val nums = arrayOf(2, 4, 6, 8)
    // if (2 in nums) {
    //     println("It exists!")
    // } else {
    //     println("It does not exists.")
    // }

    // Kotlin Functions
    // myFunction("John")
    // var result = myFunction2(3)
    // println(result)
    // result = myFunctions3(3, 5)
    // println(result)

    // Kotlin Classes and Objects
    // val c1 = Car()
    // c1.brand = "Ford"
    // c1.model = "Mustang"
    // c1.year = 1969

    // println(c1.brand)
    // println(c1.model)
    // println(c1.year)

    // Kotlin Constructors / functions
    // val c2 = Car2("Ford", "Mustang", 1961)
    // println(c2.brand)
    // c2.drive()
    // c2.speed(200)

    // Kotlin Inheritance
    val myObj = MyChildClass()
    myObj.myFunction()
}