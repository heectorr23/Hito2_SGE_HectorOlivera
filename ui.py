from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pandas as pd
import matplotlib.pyplot as plt
from database import Database
import os
import tkinter.font as font  # Import the font module

class AlcoholHealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encuesta sobre Alcohol y Salud")
        self.root.geometry("1920x1080")
        self.db = Database()
        self.current_records = []
        self.create_widgets()

    def create_widgets(self):
        # Menú
        menubar = ttk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = ttk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        file_menu.add_command(label="Exportar a Excel", command=self.export_to_excel)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)

        # PanedWindow
        paned_window = ttk.PanedWindow(self.root, orient=VERTICAL)
        paned_window.grid(row=0, column=0, sticky=(W, E, N, S))

        # Frame del formulario
        form_frame = ttk.Frame(paned_window, padding="10")
        paned_window.add(form_frame, weight=1)

        # Frame de registros
        records_frame = ttk.Frame(paned_window, padding="10")
        paned_window.add(records_frame, weight=3)

        # Campos de entrada en el formulario
        ttk.Label(form_frame, text="Edad:").grid(row=0, column=0, sticky=W)
        self.age_entry = ttk.Entry(form_frame)
        self.age_entry.grid(row=0, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Sexo:").grid(row=1, column=0, sticky=W)
        self.sex_combobox = ttk.Combobox(form_frame, values=["Hombre", "Mujer"])
        self.sex_combobox.grid(row=1, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Consumo Semanal de Alcohol:").grid(row=2, column=0, sticky=W)
        self.consumption_entry = ttk.Entry(form_frame)
        self.consumption_entry.grid(row=2, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Cervezas por Semana:").grid(row=3, column=0, sticky=W)
        self.beer_entry = ttk.Entry(form_frame)
        self.beer_entry.grid(row=3, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Bebidas Fin de Semana:").grid(row=4, column=0, sticky=W)
        self.weekend_drinks_entry = ttk.Entry(form_frame)
        self.weekend_drinks_entry.grid(row=4, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Bebidas Destiladas por Semana:").grid(row=5, column=0, sticky=W)
        self.distilled_drinks_entry = ttk.Entry(form_frame)
        self.distilled_drinks_entry.grid(row=5, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Vinos por Semana:").grid(row=6, column=0, sticky=W)
        self.wine_entry = ttk.Entry(form_frame)
        self.wine_entry.grid(row=6, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Pérdidas de Control:").grid(row=7, column=0, sticky=W)
        self.control_loss_entry = ttk.Entry(form_frame)
        self.control_loss_entry.grid(row=7, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Diversión Dependencia Alcohol:").grid(row=8, column=0, sticky=W)
        self.alcohol_dependence_combobox = ttk.Combobox(form_frame, values=["Si", "No"])
        self.alcohol_dependence_combobox.grid(row=8, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Problemas Digestivos:").grid(row=9, column=0, sticky=W)
        self.digestive_issues_combobox = ttk.Combobox(form_frame, values=["Si", "No"])
        self.digestive_issues_combobox.grid(row=9, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Tensión Alta:").grid(row=10, column=0, sticky=W)
        self.high_tension_entry = ttk.Entry(form_frame)
        self.high_tension_entry.grid(row=10, column=1, sticky=(W, E))

        ttk.Label(form_frame, text="Dolor de Cabeza:").grid(row=11, column=0, sticky=W)
        self.headache_entry = ttk.Entry(form_frame)
        self.headache_entry.grid(row=11, column=1, sticky=(W, E))

        # Botones en el formulario
        ttk.Button(form_frame, text="Agregar Registro", command=self.add_record).grid(row=12, column=0, sticky=W)
        ttk.Button(form_frame, text="Actualizar Registro", command=self.update_record).grid(row=12, column=1, sticky=W)
        ttk.Button(form_frame, text="Eliminar Registro", command=self.delete_record).grid(row=12, column=2, sticky=W)
        ttk.Button(form_frame, text="Ver Registros", command=self.view_records).grid(row=12, column=3, sticky=W)

        # Tabla de registros
        self.tree = ttk.Treeview(records_frame, columns=("id", "age", "sex", "consumption", "beer", "weekend_drinks", "distilled_drinks", "wine", "control_loss", "alcohol_dependence", "digestive_issues", "high_tension", "headache"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("age", text="Edad")
        self.tree.heading("sex", text="Sexo")
        self.tree.heading("consumption", text="Consumo Semanal de Alcohol")
        self.tree.heading("beer", text="Cervezas por Semana")
        self.tree.heading("weekend_drinks", text="Bebidas Fin de Semana")
        self.tree.heading("distilled_drinks", text="Bebidas Destiladas por Semana")
        self.tree.heading("wine", text="Vinos por Semana")
        self.tree.heading("control_loss", text="Pérdidas de Control")
        self.tree.heading("alcohol_dependence", text="Diversión Dependencia Alcohol")
        self.tree.heading("digestive_issues", text="Problemas Digestivos")
        self.tree.heading("high_tension", text="Tensión Alta")
        self.tree.heading("headache", text="Dolor de Cabeza")
        self.tree.grid(row=0, column=0, columnspan=4, sticky=(W, E, N, S))

        # Ajustar el ancho de las columnas según el encabezado
        for col in self.tree["columns"]:
            self.tree.column(col, width=font.Font().measure(self.tree.heading(col, 'text')), anchor=CENTER)

        ttk.Label(records_frame, text="Ordenar por:").grid(row=1, column=0, sticky=W)
        self.order_by_var = ttk.StringVar()
        self.order_by_combobox = ttk.Combobox(records_frame, textvariable=self.order_by_var)
        self.order_by_combobox['values'] = ("idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza")
        self.order_by_combobox.grid(row=1, column=1, sticky=(W, E))
        self.order_by_combobox.bind("<<ComboboxSelected>>", self.on_order_by_selected)

        ttk.Button(records_frame, text="Mostrar Gráfico", command=self.show_graph).grid(row=2, column=0, sticky=W)

    def add_record(self):
        age = self.age_entry.get()
        sex = self.sex_combobox.get()
        consumption = self.consumption_entry.get()
        beer = self.beer_entry.get()
        weekend_drinks = self.weekend_drinks_entry.get()
        distilled_drinks = self.distilled_drinks_entry.get()
        wine = self.wine_entry.get()
        control_loss = self.control_loss_entry.get()
        alcohol_dependence = self.alcohol_dependence_combobox.get()
        digestive_issues = self.digestive_issues_combobox.get()
        high_tension = self.high_tension_entry.get()
        headache = self.headache_entry.get()
        self.db.add_record(age, sex, consumption, beer, weekend_drinks, distilled_drinks, wine, control_loss, alcohol_dependence, digestive_issues, high_tension, headache)
        messagebox.showinfo("Éxito", "Registro agregado exitosamente")
        self.view_records()

    def update_record(self):
        selected_item = self.tree.selection()[0]
        id = self.tree.item(selected_item)['values'][0]
        age = self.age_entry.get()
        sex = self.sex_combobox.get()
        consumption = self.consumption_entry.get()
        beer = self.beer_entry.get()
        weekend_drinks = self.weekend_drinks_entry.get()
        distilled_drinks = self.distilled_drinks_entry.get()
        wine = self.wine_entry.get()
        control_loss = self.control_loss_entry.get()
        alcohol_dependence = self.alcohol_dependence_combobox.get()
        digestive_issues = self.digestive_issues_combobox.get()
        high_tension = self.high_tension_entry.get()
        headache = self.headache_entry.get()
        self.db.update_record(id, age, sex, consumption, beer, weekend_drinks, distilled_drinks, wine, control_loss, alcohol_dependence, digestive_issues, high_tension, headache)
        messagebox.showinfo("Éxito", "Registro actualizado exitosamente")
        self.view_records()

    def delete_record(self):
        selected_item = self.tree.selection()[0]
        id = self.tree.item(selected_item)['values'][0]
        self.db.delete_record(id)
        messagebox.showinfo("Éxito", "Registro eliminado exitosamente")
        self.view_records()

    def view_records(self, order_by="idEncuesta"):
        for row in self.tree.get_children():
            self.tree.delete(row)
        records = self.db.fetch_records(order_by)
        self.current_records = records
        for row in records:
            self.tree.insert("", "end", values=row)

    def on_order_by_selected(self, event):
        self.view_records(order_by=self.order_by_var.get())

    def export_to_excel(self):
        df = pd.DataFrame(self.current_records, columns=["idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])
        file_path = os.path.join(os.getcwd(), "resultados_encuesta.xlsx")
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Éxito", f"Datos exportados a Excel exitosamente en {file_path}")

    def show_graph(self):
        rows = self.db.fetch_records()
        df = pd.DataFrame(rows, columns=["idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos", "TensionAlta", "DolorCabeza"])

        # Example: Plot average weekly alcohol consumption by age group
        df['edad'] = pd.to_numeric(df['edad'], errors='coerce')
        df['BebidasSemana'] = pd.to_numeric(df['BebidasSemana'], errors='coerce')
        age_groups = pd.cut(df['edad'], bins=[0, 18, 25, 35, 45, 55, 65, 100], labels=["0-18", "19-25", "26-35", "36-45", "46-55", "56-65", "66+"])
        avg_consumption_by_age = df.groupby(age_groups)['BebidasSemana'].mean()

        avg_consumption_by_age.plot(kind='bar', title='Consumo Semanal Promedio de Alcohol por Grupo de Edad')
        plt.xlabel('Grupo de Edad')
        plt.ylabel('Consumo Semanal Promedio de Alcohol')
        plt.show()