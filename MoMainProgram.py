def MoMainProgram():
    import time
    print("MainProgram Active")
    time.sleep(0.5)
    a = 5
    for i in range(5,0,-1):
        print(str(a)+"秒后关闭")
        a -=1
        time.sleep(1)
    input("按任意键退出")
