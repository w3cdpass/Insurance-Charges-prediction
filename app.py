import tkinter as tk
from dashboard.dashboard import Dashboard


def run_dashboard():
    root = tk.Tk()
    app = Dashboard(root)
    
    app.create_prediction_tab()
    root.mainloop()


if __name__ == "__main__":
    run_dashboard()
