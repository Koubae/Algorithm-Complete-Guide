import java.util.Scanner;

class SumTwoDigits {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();

        System.out.println(sumTwoDigits(a, b));
    }

    static int sumTwoDigits(int a, int b) {
        return a + b;
    }
}