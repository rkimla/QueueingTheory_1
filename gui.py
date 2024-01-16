import tkinter as tk
from tkinter import ttk
import numpy as np
from model import calculate_parameters
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def update_plot():
    try:
        mu = float(mu_entry.get())
        N = int(N_entry.get())
        lambd_start = float(lambd_start_entry.get())
        lambd_end = float(lambd_end_entry.get())
        lambd_step = int(lambd_step_entry.get())
        lambd_range = np.linspace(lambd_start, lambd_end, lambd_step)

        L_values, W_values = [], []
        for lambd in lambd_range:
            results = calculate_parameters(lambd, mu, N)
            L_values.append(results['Average number in system (L)'])
            W_values.append(results['Average time in system (W)'])

        # Clear current figures
        ax1.clear()
        ax2.clear()

        # Replot with new values
        ax1.plot(lambd_range, L_values, label='L (avg. number in system)')
        ax1.set_xlabel('Arrival rate (lambda)')
        ax1.set_ylabel('Average number in system (L)')
        ax1.set_title('Impact of Arrival Rate on L')
        ax1.legend()

        ax2.plot(lambd_range, W_values, label='W (avg. time in system)')
        ax2.set_xlabel('Arrival rate (lambda)')
        ax2.set_ylabel('Average time in system (W)')
        ax2.set_title('Impact of Arrival Rate on W')
        ax2.legend()

        canvas.draw()
    except ValueError:
        result_label.config(text="Please enter valid numbers.")


# Set up the main application window
root = tk.Tk()
root.title("M/M/1/N Queue Model Analysis")

# Create and place labels and entry widgets
mu_label = ttk.Label(root, text="Service Rate (mu):")
mu_label.pack()
mu_entry = ttk.Entry(root)
mu_entry.pack()

N_label = ttk.Label(root, text="Buffer Size (N):")
N_label.pack()
N_entry = ttk.Entry(root)
N_entry.pack()

lambd_start_label = ttk.Label(root, text="Lambda Start:")
lambd_start_label.pack()
lambd_start_entry = ttk.Entry(root)
lambd_start_entry.pack()

lambd_end_label = ttk.Label(root, text="Lambda End:")
lambd_end_label.pack()
lambd_end_entry = ttk.Entry(root)
lambd_end_entry.pack()

lambd_step_label = ttk.Label(root, text="Number of Steps for Lambda Range:")
lambd_step_label.pack()
lambd_step_entry = ttk.Entry(root)
lambd_step_entry.pack()

# Submit button
submit_button = ttk.Button(root, text="Run Simulation", command=update_plot)
submit_button.pack()

# Result label
result_label = ttk.Label(root, text="")
result_label.pack()

# Setup Matplotlib Figure and Axes
fig = Figure(figsize=(10, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

# Embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Run the application
root.mainloop()
