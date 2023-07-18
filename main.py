import customtkinter
from button import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("simple file manager")
        self.geometry("960x860")

        # frame for view files
        self.open_folder_frame = customtkinter.CTkFrame(self)
        self.open_folder_frame.grid(row=0, column=0)
        self.open_label = customtkinter.CTkLabel(self.open_folder_frame, text="folder you want to open:")
        self.open_label.grid(row=0, column=0)
        self.open_entry = customtkinter.CTkEntry(self.open_folder_frame, width=400)
        self.open_entry.grid(row=0, column=1)
        self.lst_file_open = {}
        self.open_button = customtkinter.CTkButton(self.open_folder_frame, text="go",
                                                   command=lambda: openPath(self.open_entry.get(),
                                                                            self.lst_display,
                                                                            self))
        self.open_button.grid(row=0, column=2)
        self.deep_search_button = customtkinter.CTkButton(self.open_folder_frame, text="deep search",
                                                          command=lambda: deep_search(self.open_entry.get(),
                                                                                      self.lst_display, self))
        self.deep_search_button.grid(row=0, column=3)

        # frame for display and select file
        self.lst_file = {}
        self.lst_display = {}
        self.display_control_frame = customtkinter.CTkFrame(self)
        self.display_control_frame.grid(row=1, column=0)
        self.selectAll_button = customtkinter.CTkCheckBox(self.display_control_frame, text="Select all",
                                                          command=lambda: AllSeclect(self.selectAll_button,
                                                                                     self.lst_display))
        self.selectAll_button.grid(row=0, column=0)
        self.show_path_checkbox = customtkinter.CTkCheckBox(self.display_control_frame, text="show file path",
                                                            command=lambda: show_path(self.show_path_checkbox,
                                                                                      self.lst_display))
        self.show_path_checkbox.grid(row=0, column=1)
        self.show_path_checkbox.select()
        self.display_frame = customtkinter.CTkScrollableFrame(self, width=900, height=250)
        self.display_frame.grid(row=2, column=0)

        # get selected file
        self.selcet_button = customtkinter.CTkButton(self, text="select",
                                                     command=lambda: getSelected(self.selected_frame,
                                                                                 self.lst_display,
                                                                                 self.lst_selected,
                                                                                 self.selectAll_button1))
        self.selcet_button.grid(row=3, column=0)

        # display selected file
        self.display_label = customtkinter.CTkLabel(self, text="Files selected:")
        self.display_label.grid(row=4, column=0)
        self.lst_selected = {}
        self.selected_control_frame = customtkinter.CTkFrame(self)
        self.selected_control_frame.grid(row=5, column=0)
        self.selectAll_button1 = customtkinter.CTkCheckBox(self.selected_control_frame, text="Select all",
                                                           command=lambda: AllSeclect(self.selectAll_button1,
                                                                                      self.lst_selected))
        self.selectAll_button1.grid(row=0, column=0)
        self.selectAll_button1.select()
        self.show_path_checkbox1 = customtkinter.CTkCheckBox(self.selected_control_frame, text="show file path",
                                                             command=lambda: show_path(self.show_path_checkbox1,
                                                                                       self.lst_selected))
        self.show_path_checkbox1.grid(row=0, column=1)
        self.show_path_checkbox1.select()
        self.selected_frame = customtkinter.CTkScrollableFrame(self, width=900, height=250)
        self.selected_frame.grid(row=6, column=0)

        # control selection
        self.control_frame = customtkinter.CTkFrame(self, width=400, height=200)
        self.control_frame.grid(row=7, column=0)
        self.deselect_button = customtkinter.CTkButton(self.control_frame, text="deselect",
                                                       command=lambda: deselect_item(self.lst_selected))
        self.deselect_button.grid(row=0, column=1)
        self.move_label = customtkinter.CTkLabel(self.control_frame, text="destination: ")
        self.move_label.grid(row=1, column=0)
        self.move_path_entry = customtkinter.CTkEntry(self.control_frame, width=400)
        self.move_path_entry.grid(row=1, column=1)
        self.move_button = customtkinter.CTkButton(self.control_frame, text="move",
                                                   command=lambda: move_file(self.lst_selected,
                                                                             self.move_path_entry.get()))
        self.move_button.grid(row=1, column=2)
        self.copy_button = customtkinter.CTkButton(self.control_frame, text="copy",
                                                   command=lambda: copy_file(self.lst_selected,
                                                                             self.move_path_entry.get()))
        self.copy_button.grid(row=2, column=2)
        self.new_folder_path_label = customtkinter.CTkLabel(self.control_frame, text="new folder path: ")
        self.new_folder_path_label.grid(row=3, column=0)
        self.new_folder_path_entry = customtkinter.CTkEntry(self.control_frame, width=400)
        self.new_folder_path_entry.grid(row=3, column=1)
        self.new_folder_name_label = customtkinter.CTkLabel(self.control_frame, text="new folder name: ")
        self.new_folder_name_label.grid(row=4, column=0)
        self.new_folder_name_entry = customtkinter.CTkEntry(self.control_frame, width=100)
        self.new_folder_name_entry.grid(row=4, column=1)
        self.create_new_file_button = customtkinter.CTkButton(self.control_frame, text="create new folder",
                                                              command=lambda: create_file(self.new_folder_path_entry.get(),
                                                                                          self.new_folder_name_entry.get()))
        self.create_new_file_button.grid(row=4, column=2)

app1 = app()
app1.mainloop()
