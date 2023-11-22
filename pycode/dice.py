'''
Code to compute the probability of rolling a dice (value 1-6) x times and getting a sum of y
'''
import numpy as np

# Compute exact probability through dynamic programming
def compute_exact_prob(x, y):
    # Initialize a 2D array to store the probabilities
    prob = [[0 for _ in range(y+1)] for _ in range(x+1)]

    # initialize the first row
    for i in range(1, y+1):
        if 1 <= i <= 6:
            prob[1][i] = 1/6
    
    # compute probabilities
    for i in range(2, x+1):
        for j in range(1, y+1):
            for k in range(1, 7):
                if j-k >= 1:
                    prob[i][j] += prob[i-1][j-k]/6
    return prob[x][y]

# Utilities
def get_mean_variance(x):
    EX2 = (1/6) * (1+4+9+16+25+36)
    EX = (1/6) * (1+2+3+4+5+6)
    single_var = EX2 - EX**2
    return single_var/x

def normal_pdf(x, mean, std_dev):
    """
    Calculate the probability density function of a normal distribution.

    :param x: Value to calculate the PDF for.
    :param mean: Mean (mu) of the normal distribution.
    :param std_dev: Standard deviation (sigma) of the normal distribution.
    :return: PDF value at x.
    """
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

def get_approx_prob(x, y):
    sample_mean = 7/2
    sample_mean_var = get_mean_variance(x)
    sample_std_dev = np.sqrt(sample_mean_var)
    pdf = normal_pdf(y/x, sample_mean, sample_std_dev)
    # need to multiply the pdf by the length on x-axis
    length = 1/x
    return pdf * length

# compute approximate probability when x is large through central limit theorem

if __name__ == '__main__':
    x = 20
    y = 75
    print('The approximate probability of rolling a dice {} times and getting a sum of {} is {}'.format(x, y, get_approx_prob(x, y)))
    print('The exact probability of rolling a dice {} times and getting a sum of {} is {}'.format(x, y, compute_exact_prob(x, y)))

    # benchmark
    import time
    start_time = time.time()
    for _ in range(100):
        compute_exact_prob(x, y)
    print('Time taken to compute exact probability: {}'.format(time.time() - start_time))

    start_time = time.time()
    for _ in range(100):
        get_approx_prob(x, y)
    print('Time taken to compute approximate probability: {}'.format(time.time() - start_time))