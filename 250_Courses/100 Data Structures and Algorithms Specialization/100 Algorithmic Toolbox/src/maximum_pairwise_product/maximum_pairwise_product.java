import java.util.*;
import java.io.*;

class MaximumPairWiseProduct {
    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);

        int n = scanner.nextInt();
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scanner.nextInt();
        }

        //System.out.println(Arrays.toString(numbers));
        int result = getMaxPairwiseProduct(n, numbers);
        System.out.println(result);

    }

    static int getMaxPairwiseProduct(int n, int[] numbers) {
        // sort array 
        Arrays.sort(numbers);

        int a = numbers[n - 1];
        int b = numbers[n - 2];
        return a * b; 
    }
 
    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new
                    InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

}