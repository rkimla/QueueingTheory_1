def calculate_parameters(lambd, mu, N):
    """
    Calculate the main characteristics of an M/M/1/N queue.

    :param lambd: Arrival rate (lambda)
    :param mu: Service rate (mu)
    :param N: Maximum number of customers in the system (queue + service)
    :return: Dictionary of system parameters
    """
    rho = lambd / mu
    p0 = (1 - rho) / (1 - rho ** (N + 1))
    pn = p0 * rho ** N

    L = sum(i * p0 * rho ** i for i in range(1, N + 1))
    Lq = sum(i * p0 * rho ** i for i in range(1, N))
    W = L / lambd
    Wq = Lq / lambd

    return {
        'Probability of 0 customers': p0,
        'Probability of N customers': pn,
        'Average number in system (L)': L,
        'Average number in queue (Lq)': Lq,
        'Average time in system (W)': W,
        'Average time in queue (Wq)': Wq,
        'System Utilization (rho)': rho
    }