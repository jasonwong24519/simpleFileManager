import customtkinter
import os
from shutil import copy
import tkinter


# switching the path display
def show_path(checkbox: customtkinter.CTkCheckBox, lst: dict) -> None:
    if checkbox.get():
        for i in lst:
            lst[i][0].configure(text=i + ": " + lst[i][1])
    else:
        for i in lst:
            lst[i][0].configure(text=i)
    return


def deep_search(path: str, lst: dict, app: customtkinter.CTk) -> None:
    if not os.path.exists(path):
        tkinter.messagebox.showinfo(title="invalid path", message="the path is not exist")
        return
    frame = app.display_frame
    button = app.selectAll_button
    delAllitem(lst)

    def findFile(path: str, sub: str = "") -> None:
        fileLst = os.listdir(path)
        for file in fileLst:
            if os.path.isfile(os.path.join(path, file)):
                lst[sub + file] = []
                lst[sub + file].append(
                    customtkinter.CTkCheckBox(frame, text=sub + file + ": " + path + os.sep + file,
                                              command=lambda: button.deselect()))
                lst[sub + file][0].pack()
                lst[sub + file].append(os.path.join(path, file))
            else:
                # search sub-folder in current folder
                findFile(os.path.join(path, file), file + '-')
        return

    findFile(path)
    return


# delete checked items in selected file list
def deselect_item(lst: dict) -> None:
    lst_del = []
    for i in lst:
        if lst[i][0].get():
            lst_del.append(i)
    for i in lst_del:
        lst[i][0].pack_forget()
        lst[i][0].deselect()
        del lst[i]
    return


# move checked file to new path
def move_file(lst: dict, path: str) -> None:
    for i in lst:
        if lst[i][0].get():
            os.rename(lst[i][1], os.path.join(path, i))
    tkinter.messagebox.showinfo(title="success", message="file(s) are moved successfully")
    return


# copy checked file to new path
def copy_file(lst: dict, path: str) -> None:
    if not os.path.exists(path):
        tkinter.messagebox.showinfo(title="invalid path", message="the path is not exist")
        return
    for i in lst:
        if lst[i][0].get():
            copy(lst[i][1], os.path.join(path, os.path.basename(lst[i][1])))
            os.rename(os.path.join(path, os.path.basename(lst[i][1])), os.path.join(path, i))
    tkinter.messagebox.showinfo(title="success", message="file(s) are copied successfully")
    return


# create new folder
def create_file(path: str, name: str) -> None:
    if not os.path.exists(path):
        tkinter.messagebox.showinfo(title="invalid path", message="the path is not exist")
        return

    try:
        os.mkdir(os.path.join(path, name))
        tkinter.messagebox.showinfo(title="success", message="folder is created successfully")

    except:
        tkinter.messagebox.showinfo(title="Error", message="folder already exist")

    return


# check all the checkbox
def AllSeclect(button: customtkinter.CTkCheckBox, lst: dict) -> None:
    if button.get():
        for i in lst:
            lst[i][0].select()
    else:
        for i in lst:
            lst[i][0].deselect()
    return


# get all file in the path
def openPath(path: str, lst: dict, app: customtkinter.CTk) -> None:
    if not os.path.exists(path):
        tkinter.messagebox.showinfo(title="invalid path", message="the path is not exist")
        return
    delAllitem(lst)
    fileList = os.listdir(path)
    for i in fileList:
        lst[i] = []
        lst[i].append(customtkinter.CTkCheckBox(app.display_frame, text=i + ": " + path + os.sep + i,
                                                command=lambda: app.selectAll_button.deselect()))
        lst[i][0].pack()
        lst[i].append(path + os.sep + i)
    return


# remove all item in the list
def delAllitem(lst: dict) -> None:
    for i in lst:
        lst[i][0].pack_forget()
        lst[i][0].deselect()
    lst.clear()
    return


# add all checked items to selected list
def getSelected(selectFrame: customtkinter.CTkScrollableFrame,
                displayLst: dict,
                selectLst: dict,
                selectAll_button: customtkinter.CTkCheckBox) -> None:
    for i in displayLst:
        if displayLst[i][0].get() and i not in selectLst:
            selectLst[i] = []
            selectLst[i].append(customtkinter.CTkCheckBox(selectFrame,
                                                          text=i + ": " + displayLst[i][1],
                                                          command=lambda: selectAll_button.deselect()))
            selectLst[i][0].pack()
            selectLst[i][0].select()
            selectLst[i].append(displayLst[i][1])
    return
