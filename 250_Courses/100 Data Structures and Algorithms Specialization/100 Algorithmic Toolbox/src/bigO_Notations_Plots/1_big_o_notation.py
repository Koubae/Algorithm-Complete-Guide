import matplotlib.pyplot as plt
import numpy as np



def main():
    one_simple_plot()
    two_add_20n_plot()
    rule_5_smaller_term_can_be_omitted()
    rule_1_multiplicative_constants_can_be_omitted()
    rule_2_out_of_2_polynomials_the_one_larger_degree_grows_faster()
    rule_3_polynomials_grows_slower_than_exponentials()
    rule_4_polylogarithm_grows_slower_than_polynomials()

def one_simple_plot():
    """
    Now, plotting a function is as easy as the following three lines of code. It shows the plot of a function  7n2+6n+5
      in the range  1≤n≤100
     . Note that the scale of the  y
     -axis adjusts nicely.
    """
    n = np.linspace(1, 100)
    plt.plot(n, 7 * n * n + 6 * n + 5)
    plt.show()

def two_add_20n_plot():
    n = np.linspace(1, 100)
    plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    plt.plot(n, 20 * n, label="20n")
    plt.legend(loc='upper left')
    plt.show()

def rule_5_smaller_term_can_be_omitted():
    # n = np.linspace(1, 5)
    # plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    # plt.plot(n, 7 * n * n, label="7n^2")
    # plt.legend(loc='upper left')
    # plt.show()

    n = np.linspace(1, 100)
    plt.plot(n, 7 * n * n + 6 * n + 5, label="7n^2+6n+5")
    plt.plot(n, 7 * n * n, label="7n^2")
    plt.legend(loc='upper left')
    plt.show()

    # can also be justified as:
    x = np.linspace(1, 100)
    plt.plot(n, (7 * n * n + 6 * n + 5) / (7 * n * n))
    plt.show()

def rule_1_multiplicative_constants_can_be_omitted():
    n = np.linspace(1, 100)
    plt.plot(n, (7 * n * n + 6 * n + 5) / (n * n))
    plt.show()

def rule_2_out_of_2_polynomials_the_one_larger_degree_grows_faster():
    # n = np.linspace(1, 10)
    # plt.plot(n, n, label="n")
    # plt.plot(n, n * n, label="n^2")
    # plt.plot(n, n * n * n, label="n^3")
    # plt.legend(loc='upper left')
    # plt.show()

    n = np.linspace(1, 100)
    plt.plot(n, n, label="n")
    plt.plot(n, n * n, label="n^2")
    plt.plot(n, n * n * n, label="n^3")
    plt.legend(loc='upper left')
    plt.show()

def rule_3_polynomials_grows_slower_than_exponentials():
    # n = np.linspace(1, 10)
    # plt.plot(n, n ** 4, label="n^4")
    # plt.plot(n, 2 ** n, label="2^n")
    # plt.legend(loc='upper left')
    # plt.show()

    n = np.linspace(1, 20)
    plt.plot(n, n ** 4, label="n^4")
    plt.plot(n, 2 ** n, label="2^n")
    plt.legend(loc='upper left')
    plt.show()

def rule_4_polylogarithm_grows_slower_than_polynomials():
    # n = np.linspace(1, 20)
    # plt.plot(n, n, label="n")
    # plt.plot(n, np.log(n), label="log n")
    # plt.legend(loc='upper left')
    # plt.show()

    # n = np.linspace(1, 100)
    # plt.plot(n, n ** .5, label="n^.5")
    # plt.plot(n, np.log(n) ** 3, label="(log n)^3")
    # plt.legend(loc='upper left')
    # plt.show()
    #
    # n = np.linspace(1, 10 ** 6)
    # plt.plot(n, n ** .5, label="n^.5")
    # plt.plot(n, np.log(n) ** 3, label="(log n)^3")
    # plt.legend(loc='upper left')
    # plt.show()
    #
    # n = np.linspace(1, 10 ** 8)
    # plt.plot(n, n ** .5, label="n^.5")
    # plt.plot(n, np.log(n) ** 3, label="(log n)^3")
    # plt.legend(loc='upper left')
    # plt.show()

    n = np.linspace(1, 10 ** 15)
    plt.plot(n, n ** .5, label="n^.5")
    plt.plot(n, np.log(n) ** 3, label="(log n)^3")
    plt.legend(loc='upper left')
    plt.show()

    # exercise
    # n = np.linspace(1, 10 ** 1)
    # plt.plot(n, n ** .1, label="n^.1")
    # plt.plot(n, np.log(n) ** 5, label="(log n)^5")
    # plt.legend(loc='upper left')
    # plt.show()

if __name__ == '__main__':
    main()
