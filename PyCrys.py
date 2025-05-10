import tkinter as tk
import pymsgbox


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
       
        Lbl = tk.Label(self,text = ' ',bg="Blue", width="700",height="5")
        Lbl.pack(side="bottom")
        Lbl = tk.Label(self,text = ' ',bg="Blue", width="700",height="5")
        Lbl.pack(side="top")
        
        
    def show(self):
        self.lift()
        

class Home(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Lbl = tk.Label(self, text = ' ', bg="Blue", width="700",height="2")
        Lbl.pack(side="top")
        Lbl = tk.Label(self, text ='Introduction To Python', width="40", height="2",font=('Times New Roman', 12, 'bold'))
        Lbl.pack(side='top', anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text ='Python  was  Created in the early 1990s by Guido van Rossum.      \n  Python is a very Powerful Programming Language.                             ', width="70", height="3", font=('Leelawadee UI', 12, 'bold'))
        Lbl.pack(side='top', anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text ="Python's elegant Syntax, and dynamic typing, together with its     \n Interpreted nature, makes it an ideal language for Scripting and     \n      rapid application development in many areas on most platforms.        ", width="70", height="3", font=('Leelawadee UI', 12, 'bold'))
        Lbl.pack(side='top', anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text = '     Python is a General Purpose Language  with  wide range of Application.        ', width="75",height="3", font=('Leelawadee UI', 12, 'bold'))
        #Lbl.pack(side="top", anchor='w', fill='none', expand=False)
        #Lbl = tk.Label(self, text = ' ', width="70",height="1")
        Lbl.pack(side="top", anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text = 'Some Areas in which Python is Applicable...     ', width="55",height="3", font=('Times New Roman', 12, 'bold'))
        Lbl.pack(side="top", anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text = '        Web Development                \ndjango \nBottle  ', width="40",height="3", font=('Leelawadee UI', 12, 'bold'))
        Lbl.pack(side="top", anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text = '        Mathematical Computations \nNumPy \nSymPy   ', width="40",height="3", font=('Leelawadee UI', 12, 'bold'))
        Lbl.pack(side="top", anchor='w', fill='none', expand=False)
        Lbl = tk.Label(self, text ='         Graphical User Interface \npygame  \nPANDA3D     ', width="40", height="3", font=('Leelawadee UI', 12, 'bold'))
        Lbl.pack(side="top", anchor='w', fill='none', expand=False)
        #A combo of widgets
        
        #photo = tk.PhotoImage(file="python.png")
        #Lbl = tk.Label(self, width=500, height=500, image=photo)
        #Lbl.pack(side="left", anchor='center', fill='none', expand=True)
        #Lbl.image = photo
        
        
             
    
        


class File(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        scrl = tk.Scrollbar(self)
        scrl.pack(side=tk.RIGHT, fill=tk.Y)
        txt = tk.Text(self, height="50", width="300", yscrollcommand=scrl.set)
        
        txt.pack(side=tk.LEFT, fill=tk.Y)
        scrl.config(command=txt.yview)
        txt.config(wrap='word', yscrollcommand=scrl.set)
        txt.tag_config('bold_italics', font=('Times New Roman', 12, 'bold'))
        arguments = """
    Let us understand what Software Engineering stands for. The term is made of two words, software and engineering.\n
    Software is more than just a program code. A program is an executable code, which serves some computational purpose.\n
    Software is considered to be collection of executable programming code, associated libraries and documentations.\n
    Software, when made for a specific requirement is called software product.\n
    Engineering on the other hand, is all about developing products, using well-defined, scientific principles and methods.\n
    Software engineering is an engineering branch associated with development of software product using well-defined scientific principles,\n
    methods and procedures. The outcome of software engineering is an efficient and reliable software product.\n
        (1) The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software;\n
            that is, the application of engineering to software.\n
        (2) The study of approaches as in the above statement.\n
            Fritz Bauer, a German computer scientist, defines software engineering as:\n

            “Software engineering is the establishment and use of sound engineering principles in order to obtain economically software\n
            that is reliable and work efficiently on real machines.”\n
    Software Evolution\n
        The process of developing a software product using software engineering principles and methods is referred to as Software Evolution.\n
        This includes the initial development of software and its maintenance and updates, till desired software product is developed,\n
        which satisfies the expected requirements.


                       """
        txt.insert(tk.END, arguments)
        
        
        
class Tools(Page):
    def __init__(self, *args, **kwargs):
         Page.__init__(self, *args, **kwargs)
         lbl = tk.Label(self, text="These are Some Programming Tools")
         lbl.pack(side="left", fill="none", expand=False, anchor="n")
         txt = tk.Text(self, height=50, width=90, bg='sky blue')
         txt.tag_config('bold_italics', font=('Times New Roman', 12, 'bold', 'italic'))
         txt.tag_config('color', foreground='#476042', font=('Arial', 12, 'bold'))
         txt.insert(tk.END, '\n\tSome Python`s Libraries\n')
         verification = """ \n\t\t\t•Tkinter.\n
                         Tkinter is Python’s default GUI library.\n
                         It is based on the Tk toolkit,\n
                         originally designed for the Tool Command Language(Tcl)\n
                        •Kivy\n
                        •PyQT(Python wrapper for the Qt toolkit)\n
                        •wxPython(Python wrapper for wx widgets collection)\n
                        •PySide(Alternative Python wrapper for the Qt toolkit)\n
                        •PyGObject\n
                        •PyGTK\n
                        """
         txt.insert(tk.END, verification)
         txt.pack(side="left")
         

class Help(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        photo = tk.PhotoImage(file="python.png")
        Lbl = tk.Label(self, compound=tk.TOP, width=500, height=500, image=photo)
        Lbl.pack(side="left")
        Lbl.image = photo

        txt1 = tk.Text(self, height=50, width=80)
        scroll = tk.Scrollbar(self, command=txt1.yview)
        txt1.config(yscrollcommand=scroll.set)
        txt1.tag_config('bold_italics', font=('Times New Roman', 12, 'bold', 'italic'))
        txt1.tag_config('color', foreground='#476042', font=('Arial', 12, 'bold'))
        txt1.insert(tk.END, '\n\t\t\t\tGetting Started\n')
        verification = """ \n\t\t You can navigate through different Pages.\n
                           for information and Updates you can visit.\n
                           https://www.python.org\n
                           CREDITS\n
                           Thank's to the Python Team/Tutorials that made\n
                           my Project a Success.\n
                           Guido van Rossum, as well as being the creator\n
                           of the Python language, is the original creator of IDLE.\n
                           Other contributors prior to Version 0.8 include\n
                           Mark Hammond, Jeremy Hylton, Tim Peters, and Moshe Zadka.\n
                           IDLE\n
                           Python's Integrated Development Environment and\n
                           Learning Environment\n
                           email:idel-dev@python.org\n

                       """
        txt1.insert(tk.END, verification, 'color')
        txt1.pack(side="left")
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        
        
             



class About(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        txt1 = tk.Text(self, height=20, width=50)
        photo = tk.PhotoImage(file="my_icon.png")
        #photo1 = tk.PhotoImage(file="iconn.png")
        button1 = tk.Button(self, compound=tk.TOP, width=320, height=320, image=photo,  bg='white')
        button1.pack(side=tk.LEFT, padx=2, pady=2)
        button1.image = photo

        #declared another widget text
        txt2 = tk.Text(self, height=20, width=80)
        #declares some widgets
        scroll = tk.Scrollbar(self, command=txt2.yview)
        txt2.config(yscrollcommand=scroll.set)
        txt2.tag_config('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        txt2.tag_config('color', foreground='#476042', font=('Tempus Sans ITC', 12, 'bold'))
        #Gives Information about the developer......
        txt2.insert(tk.END, '\n\t\t\t\tAbout Developer\n', 'big')
        verification = """ \n\t\t My name is IBRAHIM Saudatu aka(also known as) Saudii.\n
                           I Developed this Software as my First Software Application.\n
                           for more visit me @twitter,facebook,instagram...\n
                          \tYou Can download this app from my blog\n
                            @Saudiiirm.blogspot.com"""
        txt2.insert(tk.END, verification, 'color')
        txt2.insert(tk.END, '\n\n\n\n\t\t\t\tPlease Do Like and Follow\n', 'follow')
        txt2.pack(side=tk.LEFT)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        pg1 = Home(self)
        pg2 = File(self)
        pg3 = Tools(self)
        pg4 = Help(self)
        pg5 = About(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        pg1.place(in_=container, x=0, y=0, relwidth=2, relheight=1)
        pg2.place(in_=container, x=0, y=0, relwidth=2, relheight=1)
        pg3.place(in_=container, x=0, y=0, relwidth=2, relheight=1)
        pg4.place(in_=container, x=0, y=0, relwidth=2, relheight=1)
        pg5.place(in_=container, x=0, y=0, relwidth=2, relheight=1)

        bt1 = tk.Button(buttonframe, text="HOME", command=pg1.lift)
        bt2 = tk.Button(buttonframe, text="FILE", command=pg2.lift)
        bt3 = tk.Button(buttonframe, text="TOOLS", command=pg3.lift)
        bt4 = tk.Button(buttonframe, text="HELP", command=pg4.lift)
        bt5 = tk.Button(buttonframe, text="ABOUT", command=pg5.lift)

        bt1.pack(side="left")
        bt2.pack(side="left")
        bt3.pack(side="left")
        bt4.pack(side="left")
        bt5.pack(side="left")

        pg1.show()




if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("11000x1000")
    root.title("PyCrys")
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='my_icon.png'))
    root.mainloop()
        
