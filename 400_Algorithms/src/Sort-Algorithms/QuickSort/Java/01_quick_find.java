/*
Quick Find: 
    * Initialize O(N) - Linear
    * Union O(N)      - Linear
    * Find O(1)       - Constant

Cons:
    * Union too expensive (N array accesses)
    * Trees are flat, but too expensive to keep them flat

*/


public class QuickFindUF {
    private int[] id;

    public QuickFindUF(int N) {  // O(N)
        id = new int[n];
        for (int i = 0; i < N; i++) 
            id[i] = i;
    }

    public boolean connected(int p, int q) { // O(1)
        return id[p] == id[q];
    }

    public void union(int p, int q) { // O(N)
        int pid = id[p];
        int qid = id[q];

        for (int i = 0; i < id.length; i ++)
            if (id[i] == pid) id[i] = qid;
    }

}