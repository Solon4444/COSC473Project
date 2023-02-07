import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql

LARGEFONT =("Verdana", 20)
FONT = ("Verdana", 12)

class tkinterApp(tk.Tk):
        
        # __init__ function for class tkinterApp
        def __init__(self, *args, **kwargs):
                
                # __init__ function for class Tk
                tk.Tk.__init__(self, *args, **kwargs)
                
                # creating a container
                container = tk.Frame(self)
                container.pack(side = "top", fill = "both", expand = True)

                container.grid_rowconfigure(0, weight = 1)
                container.grid_columnconfigure(0, weight = 1)

                # initializing frames to an empty array
                self.frames = {}

                # iterating through a tuple consisting
                # of the different page layouts
                for F in (Home, Dining, Attractions, Lodging, Itinerary):

                        frame = F(container, self)

                        # initializing frame of that object from
                        # startpage, page1, page2 respectively with
                        # for loop
                        self.frames[F] = frame

                        frame.grid(row = 20, column = 20, sticky ="nsew")

                self.show_frame(Home)

        # to display the current frame passed as
        # parameter
        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()

# first window frame startpage

class Home(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                # label of frame Layout 2
                label = ttk.Label(self, text ="Pittsburgh, PA Tourism App", font = LARGEFONT)
                
                # putting the grid in its place by using
                # grid
                label.grid(row = 0, column = 3, padx = 10, pady = 10)
                label = ttk.Label(self, text ="Welcome to Pittsburgh!", font = LARGEFONT)
                
                # putting the grid in its place by using
                # grid
                label.grid(row = 2, column = 3, padx = 10, pady = 10)

                button1 = ttk.Button(self, text ="Dining",
                command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 3, column = 1, padx = 10, pady = 10)

                ## button to show frame 2 with text layout2
                button2 = ttk.Button(self, text ="Attractions",
                command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 4, column = 1, padx = 10, pady = 10)

                ## button to show frame 3 with text layout2
                button3 = ttk.Button(self, text ="Lodging",
                command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 5, column = 1, padx = 10, pady = 10)
                
                ## button to show frame 4 with text layout2
                button4 = ttk.Button(self, text ="Itinerary",
                command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 6, column = 1, padx = 10, pady = 10)

                ## button to show frame 4 with text layout2
                button5 = ttk.Button(self, text ="Quit", command = quit)
                button5.grid(row = 7, column = 1, padx = 10, pady = 10)

                label = ttk.Label(self, text ="Recommendations", font = FONT)
                label.grid(row = 8, column = 3, padx = 10, pady = 10)

                load = Image.open("MainPage.png")
                render = ImageTk.PhotoImage(load)
                img = ttk.Label(self, image=render)
                img.image = render
                img.place(x=100, y=100)


# second window frame page1
class Dining(tk.Frame):
        
        def __init__(self, parent, controller):
                
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Dining", font = LARGEFONT)
                label.grid(row = 0, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place
                # by using grid
                button1.grid(row = 3, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button2 = ttk.Button(self, text ="Attractions",
                                                        command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 4, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Lodging",
                                                        command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 5, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Itinerary",
                                                        command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 6, column = 1, padx = 10, pady = 10)

                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 7, column = 1, padx = 10, pady = 10)
                
                #Drop Down Menu1
                my_str_var = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var,
                    values= ["Yes", "No"])

                my_combobox.grid(row=2, column=2,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Currently Open")
                label.grid(row = 1, column = 2, padx = 10, pady = 10)

                #Drop Down Menu 2

                my_str_var2 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var2,
                    values= ["9 am - 9 pm", "12 pm - 12 am", "5 pm - 3 am"])

                my_combobox.grid(row=2, column=3,padx = 10, pady = 10 )

                label = ttk.Label(self, text ="Filter by Hours")
                label.grid(row = 1, column = 3, padx = 10, pady = 10)

                                #Drop Down Menu 3

                my_str_var3 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var3,
                    values= ["1 Star", "2 Stars", "3 Stars", "4 Stars","5 Stars"])

                my_combobox.grid(row=2, column=4,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Rating")
                label.grid(row = 1, column = 4, padx = 10, pady = 10)

                                                #Drop Down Menu 4

                my_str_var4 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var3,
                    values= ["Fine Dining", "Fast Food", "Casual", "Family","Bar"])

                my_combobox.grid(row=2, column=5,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Type")
                label.grid(row = 1, column = 5, padx = 10, pady = 10)

                

                                                #Drop Down Menu 5

                my_str_var5 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var5,
                    values= ["$", "$$", "$$$", "$$$$","$$$$$"])

                my_combobox.grid(row=2, column=6,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Price")
                label.grid(row = 1, column = 6, padx = 10, pady = 10)

                label = ttk.Label(self, text ="Recommendations", font = FONT)
                label.grid(row = 8, column = 4, padx = 10, pady = 10)



                

# third window frame page2
class Attractions(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Attractions", font = LARGEFONT)
                label.grid(row = 0, column = 4, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 3, column = 1, padx = 10, pady = 10)

                button2 = ttk.Button(self, text ="Dining",
                                                        command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 4, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Lodging",
                                                        command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 5, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Itinerary",
                                                        command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 6, column = 1, padx = 10, pady = 10)

                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 7, column = 1, padx = 10, pady = 10)

                                #Drop Down Menu1
                my_str_var = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var,
                    values= ["Yes", "No"])

                my_combobox.grid(row=2, column=2,padx = 10, pady = 10 )

                label = ttk.Label(self, text ="Currently Open")
                label.grid(row = 1, column = 2, padx = 10, pady = 10)

                #Drop Down Menu 2

                my_str_var2 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var2,
                    values= ["9 am - 9 pm", "12 pm - 12 am", "5 pm - 3 am"])

                my_combobox.grid(row=2, column=3,padx = 10, pady = 10 )

                label = ttk.Label(self, text ="Filter by Hours")
                label.grid(row = 1, column = 3, padx = 10, pady = 10)

                                #Drop Down Menu 3

                my_str_var3 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var3,
                    values= ["1 Star", "2 Stars", "3 Stars", "4 Stars","5 Stars"])

                my_combobox.grid(row=2, column=4,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Rating")
                label.grid(row = 1, column = 4, padx = 10, pady = 10)

                                                #Drop Down Menu 4

                my_str_var4 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var4,
                    values= ["Museum", "Amusement Park", "Outdoor Fun", "Tours"])

                my_combobox.grid(row=2, column=5,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Type")
                label.grid(row = 1, column = 5, padx = 10, pady = 10)

                                                #Drop Down Menu 5

                my_str_var5 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var5,
                    values= ["$", "$$", "$$$", "$$$$","$$$$$"])

                my_combobox.grid(row=2, column=6,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Price")
                label.grid(row = 1, column = 6, padx = 10, pady = 10)

                label = ttk.Label(self, text ="Recommendations", font = FONT)
                label.grid(row = 8, column = 4, padx = 10, pady = 10)
                
# third window frame page3
class Lodging(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Lodging", font = LARGEFONT)
                label.grid(row = 0, column = 3, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 3, column = 1, padx = 10, pady = 10)

                button2 = ttk.Button(self, text ="Dining",
                                                        command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 4, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Attractions",
                                                        command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 5, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Itinerary",
                                                        command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 6, column = 1, padx = 10, pady = 10)

                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 7, column = 1, padx = 10, pady = 10)

                                #Drop Down Menu 1
                my_str_var = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var,
                    values= ["Hotel", "Motel", "Camping"])

                my_combobox.grid(row=2, column=2,padx = 10, pady = 10 )

                label = ttk.Label(self, text ="Filter by Type")
                label.grid(row = 1, column = 2, padx = 10, pady = 10)


                                #Drop Down Menu 2

                my_str_var2 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var2,
                    values= ["1 Star", "2 Stars", "3 Stars", "4 Stars","5 Stars"])

                my_combobox.grid(row=2, column=3,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Rating")
                label.grid(row = 1, column = 3, padx = 10, pady = 10)


                                                #Drop Down Menu 3

                my_str_var3 = tk.StringVar()

                my_combobox = ttk.Combobox(
                    self, textvariable = my_str_var3,
                    values= ["$", "$$", "$$$", "$$$$","$$$$$"])

                my_combobox.grid(row=2, column=4,padx = 10, pady = 10)

                label = ttk.Label(self, text ="Filter by Price")
                label.grid(row = 1, column = 4, padx = 10, pady = 10)

                label = ttk.Label(self, text ="Recommendations", font =FONT)
                label.grid(row = 8, column = 3, padx = 10, pady = 10)

# fourth window frame page4
class Itinerary(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Itinerary", font = LARGEFONT)
                label.grid(row = 0, column = 3, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 3, column = 1, padx = 10, pady = 10)

                button2 = ttk.Button(self, text ="Dining",
                                                        command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 4, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Attractions",
                                                        command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 5, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Lodging",
                                                        command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 6, column = 1, padx = 10, pady = 10)
                
                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 7, column = 1, padx = 10, pady = 10)

                label = ttk.Label(self, text ="Recommendations", font = FONT)
                label.grid(row = 8, column = 3, padx = 10, pady = 10)

# Driver Code
app = tkinterApp()
app.mainloop()
