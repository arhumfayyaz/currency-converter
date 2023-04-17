#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import tkinter as tk

# API endpoint and app ID
ENDPOINT = 'https://openexchangerates.org/api/latest.json'
APP_ID = '5de58349386f46c29e39406297f58a0f'

# Create a GUI window
root = tk.Tk()
root.title('Arham`s Currency Converter')

# Create a label and entry for the amount to convert
amount_label = tk.Label(root, text='Amount:')
amount_label.pack(side=tk.LEFT, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(side=tk.LEFT, padx=5, pady=5)

# Create a label and dropdown for the source currency
source_label = tk.Label(root, text='From:')
source_label.pack(side=tk.LEFT, padx=5, pady=5)
source_var = tk.StringVar()
source_dropdown = tk.OptionMenu(root, source_var, 'USD', 'EUR', 'GBP', 'JPY')
source_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# Create a label and dropdown for the target currency
target_label = tk.Label(root, text='To:')
target_label.pack(side=tk.LEFT, padx=5, pady=5)
target_var = tk.StringVar()
target_dropdown = tk.OptionMenu(root, target_var, 'USD', 'EUR', 'GBP', 'JPY')
target_dropdown.pack(side=tk.LEFT, padx=5, pady=5)

# Create a button to perform the conversion
def convert():
    amount = float(amount_entry.get())
    source = source_var.get()
    target = target_var.get()
    response = requests.get(f'{ENDPOINT}?app_id={APP_ID}&base={source}&symbols={target}')
    data = response.json()
    rate = data['rates'][target]
    result = amount * rate
    result_label.config(text=f'{result:.2f}')

convert_button = tk.Button(root, text='Convert', command=convert)
convert_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create a label to display the result
result_label = tk.Label(root, text='')
result_label.pack(side=tk.LEFT, padx=5, pady=5)

# Run the GUI main loop
root.mainloop()


# In[ ]:




