#!/bin/python
import os 
import shutil
#Clean
if os.path.exists("project"):
    shutil.rmtree("project")
    print("Folder Deleted")

os.system("mkdir -p project/src")
os.system("mkdir -p project/tests")
os.system("mkdir -p project/build")
os.system("touch project/src/main.cpp")
os.system("chmod u+x project/src/main.cpp")
os.system("touch project/CMakeLists.txt")

#Write in Cpp file
os.system("cd project/src")
with open ("project/src/main.cpp","w") as first_file:
    first_file.write("""#include <iostream>
    int main(){
    std::cout<<"helloworld\"<<std::endl;
    return 0;             
    }""")
first_file.close()

#Create CmakeLists.txt
with open ("project/CMakeLists.txt","w") as second_file:  
    second_file.write("""cmake_minimum_required(VERSION 3.10)
    project(helloworld)
    add_exectuable(helloworld src/main.cpp)""")
second_file.close

#build

os.chdir("project/build")
os.system("cmake .. && make -j && ./helloworld")

print("Done")
