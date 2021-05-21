from tkinter import *
import pickle
import json
import numpy as np
with open("training/columns.json", "r") as f:
    data = json.load(f)
columns  = np.array(data['data_columns'])
options = columns[3:]
with open("training/banglore_home_prices_model.pickle", 'rb') as mod:
    model = pickle.load(mod)


root = Tk()
root.geometry('500x500')
root.configure(background="pink")
root.title("Banglore Housing Price estimator")

Label(root, text='Number of bathroom.').grid(row=0, column=0)
Bathrooms = Entry(root, width=35, borderwidth=5)
Bathrooms.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

Label(root, text='BHK.').grid(row=1, column=0)
Bhk = Entry(root, width=35, borderwidth=5)
Bhk.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

Label(root, text='Squareft.').grid(row=2, column=0)
Sqft = Entry(root, width=35, borderwidth=5)
Sqft.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

Label(root, text='Location.').grid(row=3, column=0)
clicked = StringVar()
clicked.set("please select a location")
OptionMenu(root, clicked, *options).grid(row=3, column=1)

Label(root, text='Result.').grid(row=4, column=0)
result = Entry(root, width=35, borderwidth=5)
result.grid(row=4, column=1, columnspan=3, padx=10, pady=10)




def predict_price(location,sqft,bath,bhk):    
    loc_index = np.where(columns==location.lower())[0][0]

    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    val = str(round(model.predict([x])[0], 2)) + " Lakh"
    result.delete(0, END)
    result.insert(0, val)

button_1=Button(root,text="Show",padx=40,pady=20,command=lambda:predict_price(clicked.get(),int(Sqft.get()), int(Bathrooms.get()), int(Bhk.get())))
button_1.grid(row=5, column=1)
root.mainloop()
