from dearpygui.core import *
from dearpygui.simple import *

def print_me(sender, data):
    log_debug(f"Menu Item: {sender}")
def print_me_slider_value(sender, data):
    log_debug(f"Menu Item: {sender}" + str(get_value("float")))
    #here's example how to set text value, or any value i think
    set_value("TestText",str(get_value("float")))

def file_picker(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".*,.py")

def apply_selected_file(sender, data):
    log_debug(data)  # so we can see what is inside of data
    directory = data[0]
    file = data[1]
    set_value("directory", directory)
    #setting file value we can have access to it
    set_value("file", file)
    set_value("file_path", f"{directory}\\{file}")

#define window settings
set_main_window_size(1280,728)
set_theme("Gold")
set_style_window_padding(30,30) 



#show_documentation()
#show_logger()

with window("Medical"):
    with tab_bar("TabBar1"):
        with tab("File picker"):
        #Select file
            add_button("Directory Selector", callback=file_picker)
            add_text("Directory Path: ")
            add_same_line()
            add_label_text("##filedir", source="directory", color=[255, 0, 0])
            add_text("File: ")
            add_same_line()
            add_label_text("##file", source="file", color=[255, 0, 0])
            add_text("File Path: ")
            add_same_line()
            add_label_text("##filepath", source="file_path", color=[255, 0, 0])
        with tab("float "):
            add_checkbox("Dupa")
            add_slider_float("float", default_value=0.273, min_value =0,max_value=1,callback=print_me_slider_value)

            add_label_text("TestText")
            #adding drawing
            add_drawing("slice1",width=348,height=582)
            add_same_line()
            add_drawing("slice2",width=348,height=582)
            add_drawing("slice3",width=348,height=582)
            add_same_line()
            add_drawing("slice4",width=348,height=582)
            #taka fajna krecha
            add_separator()
            #vertical gap 12 pixel 
            add_spacing(count=12)



    
    with menu_bar("Main Menu Bar"):

        with menu("File"):

            add_menu_item("Open", callback=file_picker)
            add_menu_item("Save", callback=print_me)
            add_menu_item("Save As", callback=print_me)
            

            with menu("Settings"):

                add_menu_item("Setting 1", callback=print_me)
                add_menu_item("Setting 2", callback=print_me)

        add_menu_item("Help", callback=print_me)

        with menu("Widget Items"):

            add_checkbox("Pick Me", callback=print_me)
            add_button("Press Me", callback=print_me)
            add_color_picker4("Color Me", callback=print_me)

#"pmin" and "pmax" we can define the upper left and lower right area of the rectangle that the image will be draw onto the canvas. 
# The image will scale to fit the specified area.
draw_image("slice1","Multidimentional-Visualization\placeholder.png",[0,240],pmax=[200, 600])
draw_image("slice2","Multidimentional-Visualization\placeholder.png",[0,240],pmax=[200, 600])
draw_image("slice3","Multidimentional-Visualization\placeholder.png",[0,240],pmax=[200, 600])
draw_image("slice4","Multidimentional-Visualization\placeholder.png",[0,240],pmax=[200, 600])

start_dearpygui(primary_window ="Medical")

