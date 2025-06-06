public class RealLifeExample {
    public static void main(String[] args) {
        int items = 50;
        float costPerItem = 9.99f;
        float totalCost = items * costPerItem;
        char currency = '$';

        System.out.println("Number of items: " + items);
        System.out.println("Cost per item: " + costPerItem + currency);
        System.out.println("Total cost = " + totalCost + currency);

        int maxScore = 500;
        int userScore = 423;
        float percentage = (float) userScore / maxScore * 100.0f;

        System.out.println("User's percentage is " + percentage);

        int myAge = 25;
        int votingAge = 18;
        System.out.println(myAge >= votingAge);

        if (myAge >= votingAge) {
            System.out.println("Old enough to vote!");
        } else {
            System.out.println("Not old enough to vote.");
        }

        String ternaryOperatorTest = (myAge == 12) ? "true" : "false";
        System.out.println(ternaryOperatorTest);

        int doorCode = 1337;

        if (doorCode == 1337) {
            System.out.println("Correct code. The door is now open");
        } else {
            System.out.println("Wrong code. The door remains closed.");
        }

        int myNum = 10;

        if (myNum > 0) {
            System.out.println("The value is a positive number.");
        } else if (myNum < 0) {
            System.out.println("The value is a negative number.");
        } else {
            System.out.println("The value is 0.");
        }

        if (myNum % 2 == 0) {
            System.out.println(myNum + " is even");
        } else {
            System.out.println(myNum + " is odd");
        }

        int day = 4;
        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
            default:
                System.out.println("Looking forward to the Weekend");
        }

        int countdown = 3;

        while (countdown > 0) {
            System.out.println(countdown);
            countdown--;
        }

        System.out.println("Happy New Year!!");

        int dice = 1;

        while (dice <= 6) {
            if (dice < 6) {
                System.out.println("No Yatzy.");
            } else {
                System.out.println("Yatzy!");
            }
            dice = dice + 1;
        }

        for (int i = 0; i <= 100; i += 10) {
            System.out.println(i);
        }

        for (int i = 0; i <= 10; i = i + 2) {
            System.out.println(i);
        }

        int number = 2;

        for (int i = 1; i <= 10; i++) {
            System.out.println(number + " x " + i + " = " + (number * i));
        }

        int ages[] = { 20, 22, 18, 35, 48, 26, 87, 70 };

        float avg, sum = 0;

        int length = ages.length;

        for (int age : ages) {
            sum += age;
        }

        avg = sum / length;

        System.out.println("The average age is: " + avg);

        int lowestAge = ages[0];

        for (int age : ages) {
            if (lowestAge > age) {
                lowestAge = age;
            }
        }

        System.out.println("The lowest age in the array is: " + lowestAge);
    }
}
