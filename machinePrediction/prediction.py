import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from machinePrediction.model import traiPredictionmodel

class PredictionInterface:
    def __init__(self, master, dataset_path='dataset/insurance.csv'):
        self.dataset_path = dataset_path
        self.master = master
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Labels
        tk.Label(self.frame, text="Age:").grid(row=0, column=18, padx=10, pady=10)
        tk.Label(self.frame, text="BMI:").grid(row=1, column=18, padx=10, pady=10)
        tk.Label(self.frame, text="Smoker:\n (yes or no)").grid(row=2, column=18, padx=10, pady=10)

        # Entry fields
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=0, column=20, columnspan=10, padx=10, pady=0)
        self.bmi_entry = tk.Entry(self.frame)
        self.bmi_entry.grid(row=1, column=20, columnspan=10, padx=10, pady=0)
        self.smoker_entry = tk.Entry(self.frame)
        self.smoker_entry.grid(row=2, column=20, columnspan=10, padx=10, pady=0)

        # Button to predict
        tk.Button(self.frame, text="Predict", command=self.predict).grid(row=3, column=18, columnspan=2, padx=10, pady=10)

        # Button to clear input fields
        tk.Button(self.frame, text="Clear", command=self.clear_input).grid(row=3, column=19, columnspan=2, padx=10, pady=10)

        # Create a canvas for plotting
        self.canvas = tk.Canvas(self.frame, width=800, height=500)
        self.canvas.grid(row=4, column=12, padx=10, pady=10)

    def predict(self):
        age = float(self.age_entry.get())
        bmi = float(self.bmi_entry.get())
        smoker = self.smoker_entry.get()

        # Convert smoker input to encoded format
        smoker_encoded = 1 if smoker.lower() == 'yes' else 0

        # Check if age is below 18
        if age < 18:
            messagebox.showerror("Error", "Sorry, predictions cannot be made for individuals under 18 years of age.")
            return

        # Check if BMI is valid
        if bmi <= 16:
            messagebox.showerror("Error", "Please enter a valid BMI above 17.")
            return

        # Load and train model
        model = traiPredictionmodel.load_and_train_model(self.dataset_path)

        # Make prediction
        prediction = model.predict([[age, bmi, smoker_encoded]])

        # Display prediction
        prediction_label = tk.Label(self.frame, text=f"Predicted charges: ${prediction[0]:.2f}")
        prediction_label.grid(row=4, column=15, columnspan=2, padx=10, pady=10)
        # Visualize data
        self.visualize_data(age, prediction[0])

    def clear_input(self):        
        self.age_entry.delete(0, tk.END)
        self.bmi_entry.delete(0, tk.END)
        self.smoker_entry.delete(0, tk.END)

    def visualize_data(self, age, predicted_charge):
        # Clear previous plot
        if hasattr(self, 'plot'):
            self.plot.get_tk_widget().destroy()
        
        self.message_button = tk.Button(self.frame, text="Things to know", command=self.show_message_box)
        self.message_button.grid(row=3, column=12, padx=10, pady=10)

        # Create a new canvas for plotting
        self.plot_canvas = tk.Canvas(self.canvas, width=400, height=500)
        self.plot_canvas.grid(row=4, column=6, columnspan=8, padx=10, pady=10)

        # Load data
        data = pd.read_csv(self.dataset_path)
        
        # Create the plot
        plt.figure(figsize=(7, 5))
        plt.title("X-Y lines represents Prediction of machine")
        scatter = sns.scatterplot(data=data, x="age", y="charges", hue="smoker", palette="pastel", ax=plt.gca())
        plt.axvline(x=age, color='red', linestyle='dashed', linewidth=0.7)
        plt.axhline(y=predicted_charge, color='red', linestyle='dashed', linewidth=0.7)

        # Convert the plot to a Tkinter-compatible format
        self.plot = FigureCanvasTkAgg(plt.gcf(), master=self.plot_canvas)
        self.plot.draw()

        # Display the plot on the canvas
        self.plot.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def show_message_box(self):
        message = (" * x-Dashed represents Age & y-Dashed represents Prediction Charges.\n"
                   " * Predicted Charges may reflect slightly above or low\n * Because User define and give us input-data of |Age|BMI|Yes-No|\n"
                   " * So, along that when Gender is argue by user input-data Prediction Charges will be predicted well by train model.\n"
                   " * Blue-dots shows Smoker[Yes]\n Orange-dots shows Smoker[No]")
        messagebox.showinfo("Some bugs", message)

def main():
    root = tk.Tk()
    app = PredictionInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
