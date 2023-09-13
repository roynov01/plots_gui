import matplotlib
import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk


PLOT_SIZE = (900, 600)
SIZE = (1280, 820)

class App:
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        root.title = "My awesome app"
        root.protocol("WM_DELETE_WINDOW", self.quit_attempt)
        screen_width = root.winfo_screenwidth()  # Width of the screen
        screen_height = root.winfo_screenheight()  # Height of the screen
        x = (screen_width / 2) - (SIZE[0] / 2)
        y = (screen_height / 2) - (SIZE[1] / 2)
        root.geometry('%dx%d+%d+%d' % (SIZE[0], SIZE[1], x, y))
        self.root = root

        self.plots = None


        self.frame_controls = ctk.CTkFrame(master=self.root)
        self.frame_plot = ctk.CTkFrame(master=self.root)
        self.frame_updates = ctk.CTkFrame(master=self.root)

        self.optionmenu_organism = ctk.CTkOptionMenu(master=self.frame_controls, command=self.callback_organism, values=["Mouse", "Human"])
        self.optionmenu_rna = ctk.CTkOptionMenu(master=self.frame_controls, command=self.callback_type, values=["RNA", "Protein"])
        self.optionmenu_organ = ctk.CTkOptionMenu(self.frame_controls,
                                                   values=["All tissues", "Pancreas", "Intestine", "Liver"],
                                                   command=self.callback_organ)
        self.entry = ctk.CTkEntry(master=self.frame_controls, placeholder_text="Gene")
        self.button_generate = ctk.CTkButton(master=self.frame_controls, command=self.callback_generate, text="Generate")
        self.button_next = ctk.CTkButton(master=self.frame_plot, command=self.callback_next, text="Next")
        self.button_previous = ctk.CTkButton(master=self.frame_plot, command=self.callback_previous, text="Previous")


        path = "img.png" #todo
        self.image1 = ImageTk.PhotoImage(Image.open(path))
        self.image = ctk.CTkImage(dark_image=Image.open(path), size=PLOT_SIZE)
        self.plot_label = ctk.CTkLabel(self.frame_plot, image=self.image)
        self.button_save = ctk.CTkButton(master=self.frame_plot, command=self.callback_save, text="Save")
        self.switch_save = ctk.CTkSwitch(master=self.frame_plot, command=self.callback_switch_save, text="Remember output folder")

        self.frame_controls.grid(column=1, row=1, rowspan=5, padx=20, pady=20)
        self.frame_updates.grid(column=1, row=6, rowspan=2, padx=20, pady=20)
        self.frame_plot.grid(column=2, row=1, rowspan=7, columnspan=4, padx=20, pady=20)
        self.optionmenu_organism.grid(column=1, row=1, padx=20, pady=20)
        self.optionmenu_rna.grid(column=1, row=2, padx=20, pady=20)
        self.optionmenu_organ.grid(column=1, row=3, padx=20, pady=20)
        self.entry.grid(column=1, row=4, padx=20, pady=20)
        self.button_generate.grid(column=1, row=5, padx=20, pady=20)

        self.button_previous.grid(column=2, row=1, padx=20, pady=20)
        self.button_next.grid(column=3, row=1, padx=20, pady=20)
        self.plot_label.grid(column=2, row=2, columnspan=4, rowspan=5, padx=20, pady=20)
        self.button_save.grid(column=3, row=7, columnspan=2, padx=5, pady=20)
        self.switch_save.grid(column=4, row=7, padx=20, pady=20)

    def callback_organism(self, val):
        print("organism: ", val)
    def callback_type(self,val):
        print("type: ", val)
    def callback_organ(self,val):
        print("organ: ", val)
    def callback_generate(self):
        print("generate button, gene: ", self.entry.get())
    def callback_next(self):
        print("next button")
    def callback_previous(self):
        print("previous button")
    def callback_save(self):
        print("save button")

    def load_all_datasets(self):
        pass
    def which_plot(self):
        # get organism, type, organ, return which datasets to run
        pass

    def callback_switch_save(self):
        print("save output:", self.switch_save.get())

    def quit_attempt(self):
        if messagebox.askokcancel("Quit", "Quit?"):
            self.root.destroy()

    def create_plots(self):
        self.plots = self.which_plot()
        pass
    def update_plots(self):
        pass
    def update_label(self):
        pass



if __name__ == "__main__":
    root = ctk.CTk()
    App(root)
    root.mainloop()


