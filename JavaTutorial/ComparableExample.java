import java.util.ArrayList;
import java.util.Collections;

public class ComparableExample {
    public static void main(String[] args) {
        ArrayList<Car> myCars = new ArrayList<Car>();
        myCars.add(new Car("BMW", "X5", 1999));
        myCars.add(new Car("Honda", "Accord", 2006));
        myCars.add(new Car("Ford", "Mustang", 1970));

        Collections.sort(myCars);

        for (Car c : myCars) {
            System.out.println(c.brand + " " + c.model + " " + c.year);
        }
    }
}

class Car implements Comparable {
    public String brand;
    public String model;
    public int year;

    public Car(String b, String m, int y) {
        brand = b;
        model = m;
        year = y;
    }

    public int compareTo(Object obj) {
        Car other = (Car) obj;
        if (year < other.year)
            return -1;
        if (year > other.year)
            return 1;
        return 0;
    }
}