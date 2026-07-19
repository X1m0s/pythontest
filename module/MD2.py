#包是一种管理Python模块命名空间的形式，采用"点模块名称"，如A.B表示包A中的子模块B
#在导入一个包的时候，python会根据sys.path中的目录来寻找这个包中包含的子目录
#目录只有包含一个叫做__init__.py的文件才会被认作是一个包，主要是为了避免一些过于大众的命名影响搜索路径中的有效模块
# sound/                          顶层包
#       __init__.py               初始化 sound 包
#       formats/                  文件格式转换子包
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  声音效果子包
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  filters 子包
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...
#上面是本文件的演示用案例

#使用时也可以每次只导入一个包里面的特定模块，比如：import sound.effects.echo
#上文的用法会导入子模块：sound.effects.echo。必须使用全名访问:sound.effects.echo.echofilter(input,output,delay=0.7,atten=4)
#还有一种导入子模块的方法是：from sound.effects import echo。这种方式同样可导入子模块echo，但他不需要前缀，可直接使用
#还有一种方式是直接导入一个函数或变量：from sound.effects.echo import echofilter。这种方式会导入子模块echo，并且可直接使用这个函数echofilter()
#当使用from package import item的形式导入时，对应的item既可以是子模块(子包)，也可以是包里面定义的其他名称(类，函数，变量)
#import语法会首先把item当作一个包定义的名称，如果未找到，再试图按照模块导入，如果还没找到则抛出一个:exc:ImportError异常
#相反的是，如果使用import item.subitem.subsubitem这种形式，除了最后一项都必须是包，最后一项可以是模块或包，但不能是类，函数或变量名

#windows平台上，通常不使用from package import *，因为windows是不区分大小写的系统，因此python提供了一个精确包的索引
#导入时python会遵循如下规则：当包定义文件__init__.py存在一个叫做__all__的列表变量时，在导入*时会把这个列表中所有名字导入
#如果不在__all__中定义，就只会导入__init__.py中定义的内容和import过的子模块，工作区内的.py文件不会自动导入

#包内部也提供了一个相对导入工具 比如from . import echo 在同级目录 当前包里的echo模块
#                                 from .. import formats 在上一级目录 父包里的formats模块
#                                 from ..filter import equalizer 父包里的filter子包 equalizer模块
#使用相对导入的好处是包名修改后不用全局替换，但只能在作为包的一部分被import引入或在__init__.py文件中使用
#在运行入口脚本中必须使用绝对路径导入
#无论是隐式的还是显式的相对导入都是从当前模块开始的。主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
#包还提供一个额外的属性__path__。这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义。可以修改这个变量，用来影响包含在包里面的模块和子包。
#这个功能并不常用，一般用来扩展包里面的模块。

