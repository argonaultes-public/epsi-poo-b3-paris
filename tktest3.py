from tkinter import N, W, E, S, Tk, StringVar, IntVar
from tkinter import ttk

def calculate():
    feet_value = float(feet.get())
    print(f'raw value: {feet_value}')
    meters.set(feet_value * 0.3048)

# créer la fenêtre principale
root = Tk()
root.title("Pieds en mètres")

# créer le cadre principal
mainframe = ttk.Frame(root, padding="10 10 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# créer le widget de saisie

feet = IntVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# créer le widget d'affichage

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ajotuer les widgets statiques

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# assurer la boucle d'évènements

root.mainloop()