# Let's create a dashboard 
# that define our dataset information 
# like what insight are coming from data
# and more 

# https://github.com/w3cdpass/Data-driven-Prediction/blob/main/Worldpopulation/answer.ipynb


from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import font
import webbrowser

from machinePrediction.prediction import PredictionInterface

class Dashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Insurance Charges")
        self.master.geometry("1680x850")
        self.master.iconbitmap("./dashboard/asset/ins.ico")
        # self.style = ttk.Style()
        # self.style.theme_create("custom", parent="alt", settings={
        #     "TNotebook": {
        #         "configure": {
        #             "tabmargins": [0, 0, 0, 0], 
        #             "background": "lightgrey",  # Set background color of notebook page
        #             "borderwidth": 0, 
        #             "highlightthickness": 0, 
        #             "font": ("Arial", 16)
        #         },
        #     },
        #     "TNotebook.Tab": {
        #         "configure": {
        #             "padding": [5, 1], 
        #             "background": "lightgray",  # Set background color of tab area
        #             "font": ("Courier", 16)
        #         },
        #     },
        # })
        # self.style.theme_use("custom")

        
        self.notebook = ttk.Notebook(self.master)
        
        self.notebook.pack(fill=tk.BOTH, expand=True)
        self.dashboard_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.dashboard_frame, text="Dashboard")

        self.create_dashboard_tab()
        # self.create_prediction_tab()
        
    def create_dashboard_tab(self):
        # Add title label
        title_label = tk.Label(self.dashboard_frame, text="Data Insights Dashboard", font=("Monospace", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Load images
        image1 = Image.open("./dashboard/asset/dist.png")
        image2 = Image.open("./dashboard/asset/ageCharges.png")
        image3 = Image.open("./dashboard/asset/yesno.png")
        image4 = Image.open("./dashboard/asset/agevssmoker.png")

        # Resize images if needed
        image1 = image1.resize((550, 300), Image.LANCZOS)
        image2 = image2.resize((550, 300), Image.LANCZOS)
        image3 = image3.resize((550, 300), Image.LANCZOS)
        image4 = image4.resize((550, 300), Image.LANCZOS)

        # Convert images to tkinter-compatible format
        photo1 = ImageTk.PhotoImage(image1)
        photo2 = ImageTk.PhotoImage(image2)
        photo3 = ImageTk.PhotoImage(image3)
        photo4 = ImageTk.PhotoImage(image4)

        # Create labels for images and their information
        label1 = tk.Label(self.dashboard_frame, image=photo1)
        label1.image = photo1
        label1.grid(row=1, column=0, padx=10, pady=10)

        info1 = tk.Label(self.dashboard_frame, text="The histogram plot shows the\n distribution of insurance charges in\n your dataset. Each bar\n represents a range of charges,\n with the height indicating the\n frequency of charges falling within\n that range. The plot provides\n a quick overview of the\n typical costs and variability of\n insurance charges in your data.")
        info1.grid(row=1, column=1, padx=10, pady=10)

        label2 = tk.Label(self.dashboard_frame, image=photo2)
        label2.image = photo2
        label2.grid(row=1, column=2, padx=10, pady=10)

        info2 = tk.Label(self.dashboard_frame, text="Scatter plot of age versus charges.\nShows relationship between \nage and insurance charges, with smoker \nstatus indicated by color.\nUseful for understanding \nhow age influences\n insurance costs, and \nif smoking status plays a role.")
        info2.grid(row=1, column=3, padx=10, pady=10)

        label3 = tk.Label(self.dashboard_frame, image=photo3)
        label3.image = photo3
        label3.grid(row=2, column=0, padx=10, pady=10)

        info3 = tk.Label(self.dashboard_frame, text="Count plot showing the \nnumber of records by smoker status.\n Each bar represents \nthe count of individuals.")
        info3.grid(row=2, column=1, padx=10, pady=10)

        label4 = tk.Label(self.dashboard_frame, image=photo4)
        label4.image = photo4
        label4.grid(row=2, column=2, padx=10, pady=10)

        info4 = tk.Label(self.dashboard_frame, text="Count plot showing records \nby gender, with bars colored by \nsmoker status. Title indicates focus on record\n distribution by gender.\n Helpful for understanding \ngender-wise distribution\n and its relation to smoking habits.")
        info4.grid(row=2, column=3, padx=10, pady=10)

        # Add link button
        def open_link(event):
            webbrowser.open_new_tab("https://github.com/w3cdpass/Insurance-Charges-prediction/tree/master")

        link_label = tk.Label(self.dashboard_frame, text="For source code \nhttps://github.com/w3cdpass/Insurance-Charges-prediction", fg="black", cursor="hand2")
        link_label.grid(row=3, column=0, columnspan=3, padx=0, pady=10)
        link_label.bind("<Button-1>", open_link)
        
        # Define a function to open the link
        def open_link2(event):
            webbrowser.open_new_tab("https://github.com/w3cdpass/Insurance-Charges-prediction/blob/master/mynotebook.ipynb")

        # Create a label for the second link
        link_label2 = tk.Label(self.dashboard_frame, text="My notebook\nhttps://github.com/w3cdpass/Insurance-Charges-prediction/mynotebook.ipynb", fg="black", cursor="hand2")
        link_label2.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        link_label2.bind("<Button-1>", open_link2)


    def create_prediction_tab(self):
        # Create a new frame for the prediction interface tab
        self.prediction_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.prediction_frame, text="Prediction Interface")

        # Instantiate the PredictionInterface class in the prediction tab
        prediction_interface = PredictionInterface(self.prediction_frame)
        return prediction_interface

