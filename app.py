import tkinter as tk
import time


class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Writing App")

        # Timer settings
        self.timeout = 5  # seconds
        self.last_written_time = time.time()

        # Create text area
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(padx=10, pady=10)

        # Timer label
        self.timer_label = tk.Label(self.root, text=f"Time left: {self.timeout} seconds")
        self.timer_label.pack(pady=5)

        # Update timer every second
        self.update_timer()

        # Bind key event to reset the timer
        self.text_area.bind("<KeyRelease>", self.reset_timer)

    def reset_timer(self, event=None):
        """Reset the timer whenever the user types something"""
        self.last_written_time = time.time()

    def update_timer(self):
        """Update the countdown timer and check if time is up"""
        elapsed_time = time.time() - self.last_written_time
        remaining_time = self.timeout - int(elapsed_time)

        if remaining_time > 0:
            self.timer_label.config(text=f"Time left: {remaining_time} seconds")
        else:
            # Clear text area when time runs out
            self.text_area.delete(1.0, tk.END)
            self.timer_label.config(text="Time's up! Text has been erased.")

        # Schedule the next update (every 1000 ms)
        self.root.after(1000, self.update_timer)


# Create the main window
root = tk.Tk()

# Create the app instance
app = DisappearingTextApp(root)

# Run the application
root.mainloop()
