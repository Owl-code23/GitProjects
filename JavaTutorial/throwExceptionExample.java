public class throwExceptionExample {
    static void chechAge(int age) {
        if (age < 18) {
            throw new ArithmeticException("Access denied - You must be at least 18 years old.");
        } else {
            System.out.println("Acces granted - You are old enough!");
        }
    }

    public static void main(String[] args) {
        chechAge(20);
        chechAge(15);
    }
}
