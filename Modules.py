#module =   a file containing python code. Maycontain functions, classes, etc.
#used with modular programming, which is to separate a program into parts

import Modules_Sub as msg

#Modules_Sub.hello()
#Modules_Sub.bye()


msg.hello()
msg.bye()

from Modules_Sub import hello,bye #or "import *" for all modules

hello()
bye()
help("modules")