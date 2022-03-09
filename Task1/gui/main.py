from tkinter import Button, Label, Radiobutton, StringVar, Tk, ttk, filedialog
from PIL import Image, ImageTk

from detecotrs import template_matching, viola_jones


def save_image():
    global image
    im = Image.open(filedialog.askopenfilename(title='open'))
    im.save("images/img.jpg")
    im = im.resize((500, 400))
    image = ImageTk.PhotoImage(im)
    image_label = Label(templ_match_tab, image=image)
    image_label.grid(row=7, column=0, padx=15, pady=10)

def save_template():
    global templ
    im = Image.open(filedialog.askopenfilename(title='open'))
    im.save("images/template.jpg")
    im = im.resize((300, 200))
    templ = ImageTk.PhotoImage(im)
    template_label = Label(templ_match_tab, image=templ)
    template_label.grid(row=7, column=1, padx=15, pady=10)

def tm_result():
    global result_image
    template_matching(method.get())
    result = Image.open("images/result.jpg")
    #result.save("images/result.jpg")
    result = result.resize((500, 400))
    result_image = ImageTk.PhotoImage(result)
    result_label = Label(templ_match_tab, image=result_image)
    result_label.grid(row=7, column=2, padx=15, pady=10)   

def vj_save_image():
    global v_image
    im = Image.open(filedialog.askopenfilename(title='open'))
    im.save("images/img.jpg")
    im = im.resize((500, 500))
    v_image = ImageTk.PhotoImage(im)
    image_label = Label(viola_jones_tab, image=v_image)
    image_label.grid(row=1, column=0, padx=15, pady=10)

def vj_result():
    global v_result_image
    viola_jones()
    result = Image.open("images/result.jpg")
    result = result.resize((500, 500))
    v_result_image = ImageTk.PhotoImage(result)
    v_result_label = Label(viola_jones_tab, image=v_result_image)
    v_result_label.grid(row=1, column=1, padx=15, pady=10) 


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

# Add buttons for TM
img_but = Button(templ_match_tab, text="Загрузить изображение", command = lambda : save_image())
template_but = Button(templ_match_tab, text="Загрузить шаблон", command = lambda : save_template())
res_but = Button(templ_match_tab, text="Получить результат", command = lambda : tm_result())

# Add buttons for Viola Jones
v_img_button = Button(viola_jones_tab, text="Загрузить фотографию", command = lambda : vj_save_image())
v_res_but = Button(viola_jones_tab, text="Получить результат", command = lambda : vj_result())

# Add radio buttons to window
tm_sqdiff.grid(row=0, column=0, padx=15, pady=7)
tm_ccorr.grid(row=1, column=0, padx=15, pady=7)
tm_ccoeff.grid(row=2, column=0, padx=15, pady=7)

# Add buttons to TM window
img_but.grid(row=4, column=0, padx=15, pady=10)
template_but.grid(row=4, column=1, padx=15, pady=10)
res_but.grid(row=4, column=2, padx=15, pady=10)

# ADD buttons to VJ window
v_img_button.grid(row=0, column=0, padx=15, pady=7)
v_res_but.grid(row=0, column=1, padx=15, pady=7)

# Add tabs to window
tab_parent.add(templ_match_tab, text="Template Matching")
tab_parent.add(viola_jones_tab, text="Viola Jones")

tab_parent.pack(expand=1, fill='both')


window.mainloop()
