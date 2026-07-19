def greet():
    print("来自example模块的问候!")

if __name__=="__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")