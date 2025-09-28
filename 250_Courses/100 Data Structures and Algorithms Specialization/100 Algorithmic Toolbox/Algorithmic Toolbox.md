---
tags:
  - algorithm
  - data-structure
  - course
  - python
  - java
  - c/cpp
date: 2025-09-27
---
Algorithmic Toolbox
=========

* [Algorithmic Toolbox](https://www.coursera.org/learn/algorithmic-toolbox?specialization=data-structures-algorithms)

Content
---------------

### Resources

* [ToolBocx Statements](./toolbox_statements.pdf)
	* [# course1_algorithmic_toolbox](https://disk.yandex.ru/d/o8E3OPP7rKjXP)

Scripts
----------------------------

* [josephus_problem.py](./src/josephus_problem/josephus_problem.py)
    * [Josephus Calculator](https://www.geogebra.org/m/ExvvrBbR)
    * https://rosettacode.org/wiki/Josephus_problem


#### Sum of Two Digits

* [sum_two_digits.py](./src/sum_of_two_digits/sum_two_digits.py)
* [sum_two_digits.java](./src/sum_of_two_digits/sum_two_digits.java)

#### Maximum Pairwise Product

* [maximum_pairwise_product.py](./src/maximum_pairwise_product/maximum_pairwise_product.py)
* [maximum_pairwise_product_fastest.py](./src/maximum_pairwise_product/maximum_pairwise_product_fastest.py)

#### Fibonacci Sequence

* [fibonacci_number_algorithms.py](./src/fibonacci_sequence/fibonacci_number_algorithms.py)
* [Computing Fibonacci numbers](http://www.cs.usfca.edu/~galles/visualization/DPFib.html) by David Galles

#### GCDs 

* [gcd_algo.py](./src/gcd/gcd_algo.py)

* GCDs -- greatest common divisor problem

For integers **a** and **b** their _GCD -- greatest common divisor_ or gcd(a, b)
is the largest integer **d** so that d divides both **a** and **b**.

```bash
input: int a, b > 0
output: gcd(a, b)
gcd(10, 4) == 2
gcd(3_918_848, 1_653_264) == 61_232
```

* [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)

#### Big-O Plots

* [1_big_o_notation.py](./src/bigO_Notations_Plots/1_big_o_notation.py)


#### Graded Assignment 1

* 1 [fibonacci.py](./src/graded_assignment_1/fibonacci.py)
* 2 [fibonacci_last_digit.py](./src/graded_assignment_1/fibonacci_last_digit.py)
* 3 [gcd.py](./src/graded_assignment_1/gcd.py)
* 4 [lcm.py](./src/graded_assignment_1/lcm.py)
* 5 [fibonacci_huge.py](./src/graded_assignment_1/fibonacci_huge.py)
* 6 [fibonacci_sum_last_digit.py](./src/graded_assignment_1/fibonacci_sum_last_digit.py)
* 7 [fibonacci_partial_sum.py](./src/graded_assignment_1/fibonacci_partial_sum.py)
* 8 [fibonacci_sum_squares.py](./src/graded_assignment_1/fibonacci_sum_squares.py)

Notes
-----------

* Greedy Algorithms
* Divide-and-Conquer
* Dynamic Programming

* [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)

* Pisano periods

### Asymptotic notation

* Bachmann–Landau notation or asymptotic notation.
* [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
* [Asymptotic Analysis (geeksforgeeks)](https://www.geeksforgeeks.org/dsa/asymptotic-notation-and-analysis-based-on-input-size-of-algorithms/)
* [Asymptotic Notations for Analysis of Algorithms (geeksforgeeks)](https://www.geeksforgeeks.org/dsa/types-of-asymptotic-notations-in-complexity-analysis-of-algorithms/)
* [Simple explanation of Asymptotic Notation!](https://www.youtube.com/watch?v=5O6f1GTLLeQ)
* [KhanAcademi Asymptotic Notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/asymptotic-notation)

* **asymptotic growth comparison** --> ⪯ vs **exact inequality** (math) ≤

![[o_annotation_hierachy_example.png]]
![[big_o_hierachy_2.png]]
#### Big-O Notation

``` bash
if you have 2 functions , f and g
f(n) = O(g(n))
(f is Big-O of g) or f <= g

if there exist constant N and c sso that for 
all :

n >= N
f(n) <= c * g(n)

f is bounded above by some constant multiple of g

```

![[big_o_common_rules.png]]


Perfect question 👍 Let me break this down **super simple** so Big-O makes sense without the scary math.

Big-O is a way of saying **how fast an algorithm grows** as the input `n` gets really, really big. It ignores small details (like constants, or small extra terms), and just keeps the "biggest" factor that dominates the growth.

1. **Multiplicative constants can be omitted**:  
   $c \cdot f \preceq f$.  
   Examples: $5n^2 \preceq n^2,\; \frac{n^2}{3} \preceq n^2$.

2. **Out of two polynomials, the one with larger degree grows faster**:  
   $n^a \preceq n^b$ for $0 \leq a \leq b$.  
   Examples: $n \prec n^2,\; \sqrt{n} \prec n^{2/3},\; n^2 \prec n^3,\; n^0 \prec \sqrt{n}$.

3. **Any polynomial grows slower than any exponential**:  
   $n^a \prec b^n$ for $a \geq 0,\; b > 1$.  
   Examples: $n^3 \prec 2^n,\; n^{10} \prec 1.1^n$.

4. **Any polylogarithm grows slower than any polynomial**:  
   $(\log n)^a \prec n^b$ for $a, b > 0$.  
   Examples: $(\log n)^3 \prec \sqrt{n},\; n \log n \prec n^2$.

5. **Smaller terms can be omitted**:  
   If $f \prec g$, then $f + g \preceq g$.  
   Examples: $n^2 + n \preceq n^2,\; 2^n + n^9 \preceq 2^n$.


![[big_o_common_reuls.png]]

**NOTE**
when you see written ⪯ is really the same as write a equal --> `=` because 
`f(n) = O(g)`

is weird but it is what it is. 
example
 5n2⪯n2 -->  5n2 = n2
 n2 /3 ⪯n2 --> n2/3 = n2

##### 🚀 Big-O Rules Cheat Sheet

###### 1. **Strictly slower vs. no faster**

- `f < g` (aka `f = o(g)`) → f grows **strictly slower** than g.  
    👉 Example: `n < n²`.
    
- `f ⪯ g` (aka `f = O(g)`) → f grows **no faster** than g (could be the same, could be slower).  
    👉 Example: `n² ⪯ n²` and also `n ⪯ n²`.
    

---

###### 2. **Slower automatically means no faster**

- If f grows slower, then obviously it also grows no faster.  
    👉 If `n < n²`, then also `n ⪯ n²`.
    

Think: if a donkey 🫏 is slower than a car 🚗, then of course the donkey is also **no faster** than the car.

---

###### 3. **Don’t confuse math ≤ with Big-O ⪯**

- Normal math: `f ≤ g` means **always smaller** for every n.  
    👉 `5n² ≤ n²` ❌ (not true).
    
- Big-O: `f ⪯ g` means **f is bounded by g up to a constant factor**.  
    👉 `5n² ⪯ n²` ✅ (because multiplying `n²` by 5 covers `5n²`).

---

### 📝 Rules shown in your slide

#### 1. **Multiplicative constants can be omitted**

- Example:
    
    - `7n³ = O(n³)        
    - `n² / 3 = O(n²)`
        
- Why? Because multiplying/dividing by a constant doesn’t change the growth trend.  
    Think: if it takes 7 minutes vs 1 minute, **both still grow like `n³`**.
    
---

#### 2. **Comparing powers of `n`**

- Rule: `nᵃ < nᵇ` for `0 < a < b`.
    
- Example:
    
    - `n = O(n²)`        
    - `√n = O(n)`
        
- Why? Because `n²` grows faster than `n`. Same for `n` growing faster than `√n`.  
    👉 Bigger exponent = faster growth.
    
---

#### 3. **Exponential vs polynomial**

- Rule: `nᵃ < bⁿ` for `a > 0, b > 1`.
    
- Example:
    
    - `n⁵ = O(√2ⁿ)`        
    - `n¹⁰⁰ = O(1.1ⁿ)`
        
- Why? **Exponentials beat polynomials**. Even `n¹⁰⁰` is nothing compared to `1.1ⁿ` when `n` is huge.
    
---

#### 4. **Logs vs powers of n**

- Rule: `(log n)ᵃ < nᵇ` for `a, b > 0`.
    
- Example:
    
    - `(log n)³ = O(√n)`        
    - `n log n = O(n²)`
        
- Why? Logs grow **super slowly** compared to powers of `n`.  
    Even `(log n)³` is tiny compared to `√n`.
    
---

#### 5. **Smaller terms can be omitted**

- Example:
    
    - `n² + n = O(n²)`        
    - `2ⁿ + n⁹ = O(2ⁿ)`
        
- Why? When combining terms, the **biggest one dominates** as `n` grows.  
    (Imagine you’re comparing $1000 vs $2 — the $2 doesn’t matter in the long run.)
    
---

### 🌱 Summary (intuition)

- Ignore constants (`7n³ → O(n³)`)
    
- Keep the **fastest growing term** (`n² + n → O(n²)`)
    
- Growth hierarchy (slow → fast):
    
    `1 < log n < n < n² < n³ < ... < 2ⁿ < 3ⁿ < ...`
    

---

⚡ Think of it like racing cars:

- **log n** = bicycle    
- **n** = car    
- **n²** = race car    
- **2ⁿ** = rocket 🚀
    
No matter how big the car is, the rocket will eventually leave it behind.

---

``` python
import matplotlib.pyplot as plt
import numpy as np

# Range of n values
n = np.linspace(1, 20, 400)  # from 1 to 20

# Functions to compare
log_n = np.log(n)
linear = n
quadratic = n**2
exponential = 2**n

# Plot
plt.figure(figsize=(10, 6))
plt.plot(n, log_n, label="log n (slow growth)", linewidth=2)
plt.plot(n, linear, label="n (linear)", linewidth=2)
plt.plot(n, quadratic, label="n² (quadratic)", linewidth=2)
plt.plot(n, exponential, label="2ⁿ (exponential)", linewidth=2)

plt.ylim(0, 50)  # limit y for better visualization
plt.xlabel("n (input size)")
plt.ylabel("Growth")
plt.title("Growth comparison of log n, n, n², and 2ⁿ")
plt.legend()
plt.grid(True)
plt.show()
```

![[big_o_growth_diff.png]]



##### Big-O Notation: Plots

We start by reminding the definitions. Consider two functions f(n) and g(n) that are defined for all positive integers and take on non-negative real values. (Some frequently used functions used in algorithm design: logn, n⎯⎯√, nlogn, n3, 2n). We say that **f grows slower than g** and write f≺g, if f(n)g(n) goes to 0 as n grows. We say that **f grows no faster than g** and write f⪯g, if there exists a constant c such that f(n)≤c⋅g(n) for all n.

Three important remarks.

1. $f \prec g$ is the same as $f = o(g)$ (small-o) and $f \preceq g$ is the same as $f = O(g)$ (big-O).  
   In this notebook, we've decided to stick to the $\preceq$ notation, since many learners find this notation more intuitive.  

   One source of confusion is the following: many learners are confused by the statement like "$5n^2 = O(n^3)$".  
   When seeing such a statement, they claim: "But this is wrong! In fact, $5n^2 = O(n^2)$!"  

   At the same time, both these statements are true: $5n^2 = O(n^3)$ and also $5n^2 = O(n^2)$.  
   They both just say that $5n^2$ grows no faster than both $n^2$ and $n^3$.  
   In fact, $5n^2$ grows no faster than $n^2$ and grows slower than $n^3$.  

   In $\preceq$ notation, this is expressed as follows: $5n^2 \preceq n^2$ and $5n^2 \preceq n^3$.  
   This resembles comparing integers: if $x = 2$, then both statements $x \leq 2$ and $x \leq 3$ are correct.

2. Note that if $f \prec g$, then also $f \preceq g$.  
   In plain English: if $f$ grows slower than $g$, then $f$ certainly grows no faster than $g$.

3. Note that we need to use a fancy $\preceq$ symbol instead of the standard less-or-equal sign $\leq$,  
   since the latter one is typically used as follows: $f \leq g$ if $f(n) \leq g(n)$ for all $n$.  
   Hence, for example, $5n^2 \nleq n^2$, but $5n^2 \preceq n^2$.


![[logarithms_rules.png]]