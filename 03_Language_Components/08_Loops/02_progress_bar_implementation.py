"""
Purpose: Progress Status Bar Implementation

    Escape Sequences
        \t - tab space
        \n - new line
        \r - rare feed
"""
print("NITHISHRAO")
print("NITHISH\tRAO")
print("NITHISH\nRAO")
print()

print(print("NITHISH\rRAOBBB"))
print(print("NITHISH\rRA"))

data_set = range(-100, 10_00_000)
data_set_length = len(data_set)

for loop_index, _ in enumerate(data_set):
    percent_completed = (loop_index / data_set_length) * 10
    percent_completed = round(percent_completed, 2)

    print(f'\r{loop_index =} {data_set_length =} {percent_completed =}', end="")
    print(f"\r{percent_completed:5} completed", end="")


"""
Assignment: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""
import time

def progress_bar(current, total, bar_length=10):
    percentage = (current / total) * 100  # Calculate percentage
    filled_length = int(bar_length * current // total)  # Calculate filled slots
    bar = '*' * filled_length + ' ' * (bar_length - filled_length)  # Create bar
    print(f"\r[{bar}] {percentage:3.0f}%", end="")  # Print progress bar dynamically


# Simulate progress
total_steps = 100
for step in range(1, total_steps + 1):
    progress_bar(step, total_steps)  # Update progress bar
    time.sleep(0.1)  # Simulate work with a delay

print("\nProgress completed!")