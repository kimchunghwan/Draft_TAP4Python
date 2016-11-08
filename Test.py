#use jpype
import os
import jpype as jp
classPath = os.pathsep.join("TestCode/testjpype.jar")
print(jp.getDefaultJVMPath())
jp.startJVM(jp.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % classPath)


j_class = jp.JClass("Testjpype")
jc = j_class()
j_class.main()
