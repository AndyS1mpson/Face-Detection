from tkinter import Button, Label, Radiobutton, StringVar, Tk, ttk, filedialog
from turtle import width
from PIL import Image, ImageTk

from detecotrs import template_matching


def save_image():
    global image
    im = Image.open(filedialog.askopenfilename(title='open'))
    im.save("images/img.jpg")
    im = im.resize((400, 300))
    image = ImageTk.PhotoImage(im)
    image_label = Label(templ_match_tab, image=image)
    image_label.grid(row=7, column=0, padx=15, pady=10)

def save_template():
    global templ
    im = Image.open(filedialog.askopenfilename(title='open'))
    im.save("images/template.jpg")
    im = im.resize((200, 200))
    templ = ImageTk.PhotoImage(im)
    template_label = Label(templ_match_tab, image=templ)
    template_label.grid(row=7, column=1, padx=15, pady=10)

def tm_result():
    global result_image
    template_matching(method.get())
    result = Image.open("images/result.jpg")
    result.save("images/result.jpg")
    result = result.resize((400, 300))
    result_image = ImageTk.PhotoImage(result)
    result_label = Label(templ_match_tab, image=result_image)
    result_label.grid(row=7, column=2, padx=15, pady=10)   


window = Tk()

window.title = ("Face Detection")
window.geometry("1000x900")

tab_parent = ttk.Notebook(window)

templ_match_tab = ttk.Frame(tab_parent)
viola_jones_tab = ttk.Frame(tab_parent)

# Methods variable can contain only one of this methods: [TM_SQDIFF, TM_CCORR, TM_CCOEFF]
method = StringVar()
# Default method
method.set('cv2.TM_SQDIFF')


tm_sqdiff = Radiobutton(templ_match_tab, text="TM_SQDIFF", variable=method, value='cv2.TM_SQDIFF')
tm_ccorr = Radiobutton(templ_match_tab, text="TM_CCORR",  variable=method, value='cv2.TM_CCORR')
tm_ccoeff = Radiobutton(templ_match_tab, text="TM_CCOEFF",  variable=method, value='cv2.TM_CCOEFF')

# Add buttons
img_but = Button(templ_match_tab, text="Загрузить изображение", command = lambda : save_image())
template_but = Button(templ_match_tab, text="Загрузить шаблон", command = lambda : save_template())
res_but = Button(templ_match_tab, text="Получить результат", command = lambda : tm_result())

# Add radio buttons to window
tm_sqdiff.grid(row=0, column=0, padx=15, pady=7)
tm_ccorr.grid(row=1, column=0, padx=15, pady=7)
tm_ccoeff.grid(row=2, column=0, padx=15, pady=7)

# Add buttons to window
img_but.grid(row=4, column=0, padx=15, pady=10)
template_but.grid(row=4, column=1, padx=15, pady=10)
res_but.grid(row=4, column=2, padx=15, pady=10)

# Add tabs to window
tab_parent.add(templ_match_tab, text="Template Matching")
tab_parent.add(viola_jones_tab, text="Viola Jones")

tab_parent.pack(expand=1, fill='both')


window.mainloop()
