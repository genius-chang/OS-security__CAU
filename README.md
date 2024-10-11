<h1>Timer Interrupt Simulation</h1>
<h3>Description</h3>
This project simulates a timer interrupt mechanism using Python, which switches between two processes at a regular interval. 
The script demonstrates how an operating system manages process switching using timer interrupts.

<h3>Features</h3>
Simulates process switching: Alternates between two processes, "Process A" and "Process B," with a 5-second timer interrupt.
Uses multi-threading: A separate thread handles the timer interrupt to allow simultaneous execution of the processes.

<h3>How It Works</h3>
The process function simulates a process that runs for a specified duration, printing its status every second.
The timer_interrupt function runs on a separate thread, triggering a timer interrupt every 5 seconds to switch between processes.

<h3>Usage</h3>
1. Clone the repository.
2. Run the script: "python3 timer_interrupt.py"
3. Observe how "Process A" and "Process B" alternate based on the timer interrupt.

<h3>Requirements</h3>
Python 3.11

<h3>License</h3>
This project is open-source and available under the MIT License.
