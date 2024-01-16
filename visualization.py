import matplotlib.pyplot as plt


def plot_characteristics(lambd_range, mu, N):
    """
    Plot system characteristics over a range of arrival rates.

    :param lambd_range: Range of arrival rates to plot
    :param mu: Service rate
    :param N: Buffer size
    """
    from model import calculate_parameters

    L_values = []
    W_values = []

    for lambd in lambd_range:
        results = calculate_parameters(lambd, mu, N)
        L_values.append(results['Average number in system (L)'])
        W_values.append(results['Average time in system (W)'])

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(lambd_range, L_values, label='L (avg. number in system)')
    plt.xlabel('Arrival rate (lambda)')
    plt.ylabel('Average number in system (L)')
    plt.title('Impact of Arrival Rate on L')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(lambd_range, W_values, label='W (avg. time in system)')
    plt.xlabel('Arrival rate (lambda)')
    plt.ylabel('Average time in system (W)')
    plt.title('Impact of Arrival Rate on W')
    plt.legend()

    plt.tight_layout()
    plt.show()