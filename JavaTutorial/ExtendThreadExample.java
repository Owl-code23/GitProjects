public class ExtendThreadExample extends Thread {
    public static void main(String[] args) {
        ExtendThreadExample thread = new ExtendThreadExample();
        thread.start();
        System.out.println("This code is outside of the thread");
    }

    public void run() {
        System.out.println("This code is running in a thread");
    }
}
