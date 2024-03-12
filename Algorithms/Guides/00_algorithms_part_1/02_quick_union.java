/*
Quick Find: 
    * Initialize O(N) - Linear
    * Union O(N)      - Linear
    * Find O(N)       - Linear

Cons:
    * Trees can get too tal
    * Find too expensive (could be N array acceses)
*/
public class QuickUnionUF {
    private int[] id;

    QuickUnionUF(int N) { // O(N)
        id = new int[N];
        for (int i = 0; i < N; i++) 
            id[i] = i;
    }

    private int root(int i) { // O(N)
        while (i != id[i])
            i = id[i];
        return i;
    }

    public boolean connected(int p, int q) { // O(N)
        return root(p) == root(q);
    }

    public void union(int p, int q) { // O(N)
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }

}

public class QuickUnionWeightedUF {
    private int[] id;
    private int[] size;

    QuickUnionWeightedUF(int N) { // O(N) - Linear
        id = new int[N];
        size = new size[N]; 
        for (int i = 0; i < N; i++) 
            id[i] = i;
    }

    private int root(int i) { // O(N) - Linear
        while (i != id[i])
            i = id[i];
        return i;
    }

    public boolean connected(int p, int q) { // O(log N) - Logarithm
        return root(p) == root(q);
    }

    public void union(int p, int q) { // O(log N) - Logarithm
        int i = root(p);
        int j = root(q);

        if (i == j) return;

        if (size[i] < size[j]) {
            id[i] = j;
            size[j] += size[i];
        } else {
            id[j] = i;
            size[i] += size[j];
        }

    }

}


public class QuickUnionWeightedPathComporessionUF {
    private int[] id;
    private int[] size;

    QuickUnionWeightedUF(int N) { // O(N) - Linear
        id = new int[N];
        size = new size[N]; 
        for (int i = 0; i < N; i++) 
            id[i] = i;
    }

    private int root(int i) { // O(N) - Linear
        while (i != id[i])
            id[i] = id[id[i]]; // path compression
            i = id[i];
        return i;
    }

    public boolean connected(int p, int q) { // O(log N) - Logarithm
        return root(p) == root(q);
    }

    public void union(int p, int q) { // O(log N) - Logarithm
        int i = root(p);
        int j = root(q);

        if (i == j) return;

        if (size[i] < size[j]) {
            id[i] = j;
            size[j] += size[i];
        } else {
            id[j] = i;
            size[i] += size[j];
        }

    }

}
