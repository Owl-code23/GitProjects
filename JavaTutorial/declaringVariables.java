public class DeclaringVariables {
    public static void main(String[] args){
        String name = "name";
        System.out.println(name);

        int myNum = 15;
        System.out.println(myNum);

        myNum = 10;
        System.out.println(myNum);

        final int myNum2 = 1;
        System.out.println(myNum2);

        float myFloatNum = 5.99f;
        char myLetter = 'D';
        boolean myBool = true;
        String myText = "hello";
        if (myBool){
            System.out.println(myFloatNum + " " + myLetter + myText);
        }
    }
    
}
