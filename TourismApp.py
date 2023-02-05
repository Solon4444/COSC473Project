import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql

LARGEFONT =("Verdana", 20)

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

                        frame.grid(row = 0, column = 0, sticky ="nsew")

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
                label.grid(row = 0, column = 2, padx = 10, pady = 10)
                label = ttk.Label(self, text ="Welcome to Pittsburgh!", font = LARGEFONT)
                
                # putting the grid in its place by using
                # grid
                label.grid(row = 1, column = 2, padx = 10, pady = 10)

                button1 = ttk.Button(self, text ="Dining",
                command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 1, column = 1, padx = 10, pady = 10)

                ## button to show frame 2 with text layout2
                button2 = ttk.Button(self, text ="Attractions",
                command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 2, column = 1, padx = 10, pady = 10)

                ## button to show frame 3 with text layout2
                button3 = ttk.Button(self, text ="Lodging",
                command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 3, column = 1, padx = 10, pady = 10)
                
                ## button to show frame 4 with text layout2
                button4 = ttk.Button(self, text ="Itinerary",
                command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 4, column = 1, padx = 10, pady = 10)

                ## button to show frame 4 with text layout2
                button5 = ttk.Button(self, text ="Quit", command = quit)
                button5.grid(row = 5, column = 1, padx = 10, pady = 10)

                label = ttk.Label(self, text ="Recommendations", font = LARGEFONT)
                label.grid(row = 3, column = 2, padx = 10, pady = 10)

# second window frame page1
class Dining(tk.Frame):
        
        def __init__(self, parent, controller):
                
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Dining", font = LARGEFONT)
                label.grid(row = 0, column = 4, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place
                # by using grid
                button1.grid(row = 1, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button2 = ttk.Button(self, text ="Attractions",
                                                        command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 2, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Lodging",
                                                        command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 3, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Itinerary",
                                                        command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 4, column = 1, padx = 10, pady = 10)

                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 5, column = 1, padx = 10, pady = 10)

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
                button1.grid(row = 1, column = 1, padx = 10, pady = 10)

                button2 = ttk.Button(self, text ="Dining",
                                                        command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 2, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Lodging",
                                                        command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 3, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Itinerary",
                                                        command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 4, column = 1, padx = 10, pady = 10)

                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 5, column = 1, padx = 10, pady = 10)
                
# third window frame page3
class Lodging(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Lodging", font = LARGEFONT)
                label.grid(row = 0, column = 4, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 1, column = 1, padx = 10, pady = 10)

                button2 = ttk.Button(self, text ="Dining",
                                                        command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 2, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Attractions",
                                                        command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 3, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Itinerary",
                                                        command = lambda : controller.show_frame(Itinerary))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 4, column = 1, padx = 10, pady = 10)

                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 5, column = 1, padx = 10, pady = 10)

# fourth window frame page4
class Itinerary(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                label = ttk.Label(self, text ="Itinerary", font = LARGEFONT)
                label.grid(row = 0, column = 4, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button1 = ttk.Button(self, text ="Home",
                                                        command = lambda : controller.show_frame(Home))
        
                # putting the button in its place by
                # using grid
                button1.grid(row = 1, column = 1, padx = 10, pady = 10)

                button2 = ttk.Button(self, text ="Dining",
                                                        command = lambda : controller.show_frame(Dining))
        
                # putting the button in its place by
                # using grid
                button2.grid(row = 2, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button3 = ttk.Button(self, text ="Attractions",
                                                        command = lambda : controller.show_frame(Attractions))
        
                # putting the button in its place by
                # using grid
                button3.grid(row = 3, column = 1, padx = 10, pady = 10)

                # button to show frame 2 with text
                # layout2
                button4 = ttk.Button(self, text ="Lodging",
                                                        command = lambda : controller.show_frame(Lodging))
        
                # putting the button in its place by
                # using grid
                button4.grid(row = 4, column = 1, padx = 10, pady = 10)
                
                button5 = ttk.Button(self, text = "Quit", command = quit)
                button5.grid(row = 5, column = 1, padx = 10, pady = 10)



# Driver Code
app = tkinterApp()
app.mainloop()
