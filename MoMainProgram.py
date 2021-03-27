def MoMainProgram():
    import time
    import os
    from dearpygui.core import *
    from dearpygui.simple import *
    print("MainProgram Active")
    def apply_text_multiplier(sender, data):
        font_multiplier = get_value("Font Size Multiplier")
        set_global_font_scale(font_multiplier)


    def apply_theme(sender, data):
        theme = get_value("Themes")
        set_theme(theme)

    add_window("主题")
    themes = ["Dark", "Light", "Classic", "Dark 2", "Grey", "Dark Grey", "Cherry", "Purple", "Gold", "Red"]
    add_combo("Themes", items=themes, default_value="Dark", callback=apply_theme)

    add_slider_float("Font Size Multiplier", default_value=1.0, min_value=0.0, max_value=2.0,
                     callback=apply_text_multiplier)
    end()

    add_window("貘")
    file = open(r'C:\ProgramData\Version-Mo\Mocheckver.txt')
    checkver=file.read()
    add_text(checkver)
    os.system(r'C:\Users\Public\Music\RickRoll.mp3')
    start_dearpygui()
    input("按任意键退出")
