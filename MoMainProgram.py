def MoMainProgram():
    import time
    import os
    from playsound import playsound
    from dearpygui.core import *
    from dearpygui.simple import *
    from multiprocessing import Process
    print("MainProgram Active")
    #---------------------------------------------------其他定义函数---------------------------------------------------
    def MusicPlayer(MusicName,MusicFile):
        os.system(MusicFile)
        add_text("BGM："+MusicName)

    def MusicPlayInMenu():
        MusicPlayer("そしていつかまた出逢って ... 桜花之恋冢 ~ JapaneseFlower - 凋叶棕",r'C:\Users\ss2007ghc\Desktop\そしていつかまた出逢って...桜花之恋冢~JapaneseFlower-凋叶棕.flac')
        time.sleep(235)
        MusicPlayer("First Memory ／ Next Memory - Stack,lily-an",r'C:\Users\ss2007ghc\Desktop\FirstMemoryNextMemoryStacklilyan.mp3')
    #---------------------------------------------------Gui定义函数---------------------------------------------------
    def apply_text_multiplier(sender, data):
        font_multiplier = get_value("Font Size Multiplier")
        set_global_font_scale(font_multiplier)


    def apply_theme(sender, data):
        theme = get_value("Themes")
        set_theme(theme)
    #---------------------------------------------------Gui主体部分---------------------------------------------------
    def MainProgramMainUnit():
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

        #MusicName = "そしていつかまた出逢って ... 桜花之恋冢 ~ JapaneseFlower - 凋叶棕"
        #MusicFile = r'C:\Users\ss2007ghc\Desktop\そしていつかまた出逢って...桜花之恋冢~JapaneseFlower-凋叶棕.flac'
        #os.system(MusicFile)
        #add_text("BGM："+MusicName)
        add_additional_font(r'C:\Windows\Fonts\msyh.ttc', 18, glyph_ranges = 'chinese_full')
        start_dearpygui()
        input("按任意键退出")

    def start_process():
        try:
            process_list = [Process(target=i) for i in [MusicPlayInMenu,MainProgramMainUnit]]
            for item in process_list:
                item.start()
            for item in process_list:
                item.join()
        except:
            print("多线程错误")

    start_process()
