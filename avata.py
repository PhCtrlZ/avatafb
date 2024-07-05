import webbrowser

from tkinter import *

from tkinter import messagebox




def btnlogin_click():
	pwd=tbPass.get()

	url = "https://mbasic.facebook.com/profile/picture/view/?profile_id="+pwd
	robot_brain = webbrowser.open_new_tab(url)
	messagebox.showinfo("Thông báo","Process successfully!!!")
def wed_click():
		url="https://commentpicker.com/find-facebook-id.php"
		robot_brain = webbrowser.open_new_tab(url)
frmlogin=Tk()

frmlogin.title("Tool")

frmlogin.geometry("600x280")

lb1= Label(frmlogin, text="Nguyễn Hoàng Phúc", font=("Time New Romen",18),fg="red")#fg=chọn màu,bg=màu background

lb1.pack()
lb2=Button(frmlogin,text="Ấn vào đây để vào wed check id người mà bạn cần lấy avata",font=("Time New Roman",12,"bold"),fg="White",bg="red",command=wed_click)

lb2.pack()

lb3= Label(frmlogin, text="Nhập ID người mà bạn cần lấy avata:" , font=("Arial",12),fg="red")

lb3.pack()

tbPass=Entry(frmlogin,width=30,font=("consolas",12))

tbPass.pack()

btnlogin=Button(frmlogin,text="Run",font=("san-serif",16,"bold"), fg="white",bg="red",command=btnlogin_click)

btnlogin.pack()

frmlogin.mainloop()
