import uuid
import json
import tkinter as tk
from tkinter import ttk



def create_db_example(dicus, usernames):
    dbexample = {}

    for i, user_data in enumerate(dicus.values()):
        entry_id = str(uuid.uuid4())
        dbexample[entry_id] = {}

        for j, attribute_name in enumerate(usernames):
            attribute_value = user_data[j]
            dbexample[entry_id][attribute_name] = attribute_value

            if attribute_name == 'country':
                dbexample[entry_id]['country attributes'] = {}
                if attribute_value == 'France':
                    dbexample[entry_id]['country attributes']['France1'] = 'at1'
                    dbexample[entry_id]['country attributes']['France2'] = 'at2'
                elif attribute_value == 'South Africa':
                    dbexample[entry_id]['country attributes']['South Africa1'] = 'at1'
                    dbexample[entry_id]['country attributes']['South Africa2'] = 'at2'
                elif attribute_value == 'Ireland':
                    dbexample[entry_id]['country attributes']['Ireland1'] = 'at1'
                    dbexample[entry_id]['country attributes']['Ireland2'] = 'at2'

    return dbexample



def create_citizen_science_app(data):
    def submit():
        username = username_entry.get()
        country = country_entry.get().strip().capitalize()
        region = region_entry.get().strip().capitalize()

        # Generate a unique ID for each entry (you may want to use a more robust method)
        entry_id = str(uuid.uuid4())

        # Create a dictionary for the current entry
        entry_data = {
            'Username': username,
            'country': country,
            'regions': region
        }

        # Add the entry to the data dictionary
        data[entry_id] = entry_data
        data[entry_id]['country attributes'] = {}
        if country == 'France':
            data[entry_id]['country attributes']['France1'] = 'at1'
            data[entry_id]['country attributes']['France2'] = 'at2'
        elif country == 'South Africa':
            data[entry_id]['country attributes']['South Africa1'] = 'at1'
            data[entry_id]['country attributes']['South Africa2'] = 'at2'
        elif country == 'Ireland':
            data[entry_id]['country attributes']['Ireland1'] = 'at1'
            data[entry_id]['country attributes']['Ireland2'] = 'at2'

        # Clear the input fields
        username_entry.delete(0, tk.END)
        country_entry.delete(0, tk.END)
        region_entry.delete(0, tk.END)

    # Create the main application window
    root = tk.Tk()
    root.title('Citizen Science Application')
    root.geometry('400x250')  # Set window size

    # Configure background colors
    root.configure(bg='green')

    # Create and configure labels and entry fields
    welcome_label = ttk.Label(root, text='Welcome, plsease provide some informations ', background='green', foreground='yellow')
    username_label = ttk.Label(root, text='Username:', background='green', foreground='yellow')
    username_entry = ttk.Entry(root)

    country_label = ttk.Label(root, text='Country:', background='green', foreground='yellow')
    country_entry = ttk.Entry(root)

    region_label = ttk.Label(root, text='Region:', background='green', foreground='yellow')
    region_entry = ttk.Entry(root)

    submit_button = ttk.Button(root, text='Submit', command=submit)

    welcome_label.place(x=120, y=10)
    username_label.place(x=20, y=60)
    username_entry.place(x=150, y=60)
    country_label.place(x=20, y=100)
    country_entry.place(x=150, y=100)
    region_label.place(x=20, y=140)
    region_entry.place(x=150, y=140)
    submit_button.place(x=170, y=180)

    bottom_text = ttk.Label(root, text='Citizen Science by Expleo', background='green', foreground='blue')
    bottom_text.place(x=100, y=230)

    # Start the GUI application
    root.mainloop()

    return data



Username= "John Snow"
country = "France"
regions = "Gironde"
user=[Username,country, regions]
Username2= "John Mow"
country2 = "South Africa"
regions2 = "Mpumalanga"
user2=[Username2,country2, regions2]
Username3= "John Floow"
country3 = "Ireland"
regions3 = "Ulster"
user3=[Username3,country3, regions3]

dicus={}
dicus[0] = user
dicus[1] = user2
dicus[2] = user3
usernames=['Username','country', 'regions']


dbexample = create_db_example(dicus, usernames)
print(dbexample)

data = dbexample
data = create_citizen_science_app(data)

print(data)