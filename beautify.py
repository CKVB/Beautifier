from tkinter import *
import os,shutil

myapp=Tk()
try:
	myapp.iconbitmap("pyt.ico")
except:
	pass
myapp.resizable(0,0)
myapp.title("Beautify")
myapp.geometry("600x270+405+199")
myapp.configure(background="#287ed3")
font10 = "-family {Segoe UI} -size 18 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
font12 = "-family {Bookman Old Style} -size 18 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"
font15 = "-family Arial -size 14 -weight normal -slant italic "  \
            "-underline 0 -overstrike 0"
font9 = "-family {Segoe UI Symbol} -size 18 -weight normal "  \
            "-slant italic -underline 0 -overstrike 0"

def Beautify_Folder():
	
	folder_path=path_text.get()
	
	try:
		os.chdir(folder_path)
		for _ in os.listdir():
			if '.' in _:
				ext=(_.split('.')[-1]).upper()
				try:
					os.makedirs(ext)
				except:
					pass
				dst_path=os.path.realpath(ext)
				src_path=os.path.realpath(_)
				try:
					shutil.move(src_path,dst_path)
				except:
					os.remove(_)
	except:
		emyapp=Tk()
		try:
			emyapp.iconbitmap("pyt.ico")
		except:
			pass
		emyapp.geometry("398x177+490+225")
		emyapp.title("Invalid Path")
		emyapp.resizable(0,0)
		Label(emyapp,text="Error",font=30,relief=GROOVE).place(relx=0.13, rely=0.17, height=41, width=304)
		Label(emyapp,text="Please provide a valid path",font=30,relief=GROOVE).place(relx=0.13, rely=0.56, height=41, width=304)
		emyapp.mainloop()
	else:
		current_folder=os.getcwd()
		emyapp=Tk()
		try:
			emyapp.iconbitmap("pyt.ico")
		except:
			pass
		emyapp.geometry("398x177+490+225")
		emyapp.title("Beautified")
		emyapp.resizable(0,0)
		Label(emyapp,text="Success",font=30,relief=GROOVE).place(relx=0.13, rely=0.17, height=41, width=304)
		Label(emyapp,text="Folder "+current_folder.split("\\")[-1]+" is Beautified",font=30,relief=GROOVE).place(relx=0.13, rely=0.56, height=41, width=304)
		emyapp.mainloop()

Label(text="Enter The Path",font=font12,background="#287ed3",foreground="#ffffff").place(relx=0.07, rely=0.19, height=31, width=174)
Entry(font=font15,background="#ffff30",foreground="#000000",relief=GROOVE).place(relx=0.37, rely=0.19,height=30, relwidth=0.61)
Button(text='Beautify',font=font9,command=Beautify_Folder,background="#77b8d8",foreground="#ffffff",relief=GROOVE,cursor="hand2").place(relx=0.35, rely=0.59, height=44, width=177)
Label(text="Note : Action can't be undone",font=font10,background="#287ed3",foreground="#54ff54").place(relx=0.18, rely=0.37, height=31, width=394)
path_text=StringVar()
path_entry=Entry(font=font15,textvariable=path_text,background="#ffff30",foreground="#000000",relief=GROOVE).place(relx=0.37, rely=0.19,height=30, relwidth=0.61)
myapp.mainloop()