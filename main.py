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
"""
    # switching the path display
    def show_path(self, checkbox: customtkinter.CTkCheckBox, lst: dict) -> None:
        if checkbox.get():
            for i in lst:
                lst[i][0].configure(text=i + ": " + lst[i][1])
        else:
            for i in lst:
                lst[i][0].configure(text=i)
        return

    # search all file in folder
    def deep_search(self, path: str, subname: str = None) -> None:
        fileLst = os.listdir(path)
        for file in fileLst:
            if os.path.isfile(os.path.join(path, file)):
                self.lst_display[subname + file] = []
                self.lst_display[subname + file].append(customtkinter.CTkCheckBox(self.display_frame,
                                                                                  text=subname + file + ": " + path + os.sep + file,
                                                                                  command=lambda: self.selectAll_button.deselect()))
                self.lst_display[subname + file][0].pack()
                self.lst_display[subname + file].append(os.path.join(path, file))
            else:
                # search sub-folder in current folder
                self.deep_search(os.path.join(path, file), file + '-')
        return

    # delete checked items in selected file list
    def deslect_item(self, lst: dict) -> None:
        lst_del = []
        for i in lst:
            if lst[i][0].get():
                lst_del.append(i)
        for i in lst_del:
            lst[i][0].pack_forget()
            lst[i][0].deselect()
            del lst[i]
        print(lst)
        return

    # move checked file to new path
    def move_file(self, lst: dict, path: str) -> None:
        for i in lst:
            if lst[i][0].get():
                os.rename(lst[i][1], os.path.join(path, os.path.basename(lst[i][1])))
        return

    # copy checked file to new path
    def copy_file(self, lst: dict, path: str) -> None:
        for i in lst:
            if lst[i][0].get():
                copy(lst[i][1], os.path.join(path, os.path.basename(lst[i][1])))
        return

    # create new folder
    def create_file(self, path: str, name: str) -> None:
        os.mkdir(os.path.join(path, name))
        return

    # check all the checkbox
    def AllSeclect(self, button: customtkinter.CTkCheckBox, lst: dict) -> None:
        if button.get():
            for i in lst:
                lst[i][0].select()
        else:
            for i in lst:
                lst[i][0].deselect()
        return

    # get all file in the path
    def openPath(self, path: str) -> None:
        self.delAllitem(self.lst_display)
        self.fileList = os.listdir(path)
        for i in self.fileList:
            self.lst_display[i] = []
            self.lst_display[i].append(customtkinter.CTkCheckBox(self.display_frame,
                                                                 text=i + ": " + path + os.sep + i,
                                                                 command=lambda: self.selectAll_button.deselect()))
            self.lst_display[i][0].pack()
            self.lst_display[i].append(path + os.sep + i)
        return

    # remove all item in the list
    def delAllitem(self, lst: dict) -> None:
        for i in lst:
            lst[i][0].pack_forget()
            lst[i][0].deselect()
        lst.clear()
        return

    # add all checked items to selected list
    def getSelected(self,
                    selectFrame: customtkinter.CTkScrollableFrame,
                    displayLst: dict,
                    selectLst: dict) -> None:
        for i in displayLst:
            if displayLst[i][0].get() and i not in selectLst:
                selectLst[i] = []
                selectLst[i].append(customtkinter.CTkCheckBox(selectFrame,
                                                              text=i + ": " + displayLst[i][1],
                                                              command=lambda: self.selectAll_button.deselect()))
                selectLst[i][0].pack()
                selectLst[i][0].select()
                selectLst[i].append(displayLst[i][1])
        return
"""

app1 = app()
app1.mainloop()
