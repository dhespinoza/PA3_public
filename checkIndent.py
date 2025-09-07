#!/usr/bin/env python3
import re
import sys

def check(file):
    """
    Checks c++ file for correct indentation. Displays one error at the time

    Args:
        file: Input .cpp, .h, or .hpp file

    Returns:
        Function returns after the first error

    """
    indent = 0
    lineNum = 0
    comment = False
    correct = True
    inStatment = False
    cin_cout_finished = True

    for line in file:
        lineNum+=1
        
        #second part needed to exclude the situation below
        # cout << kjfbkj
        #       << jkfhjkd; (indentation choice left to students)
        if (comment==False or inStatment==False) and cin_cout_finished==True:
            if line.strip().find("/*")!=-1:
                comment = True
            if (line.strip().find("*/") > line.strip().find("/*")):
                comment = False

            #check if line is not empty after removing wight spaces
            #and check if line is not starting with in line comment
            if  line.strip() and (line.strip().startswith("//")==False):
                # print(line, end="")

                #check if line starts with }, it should have 1 less indent
                if line.strip().startswith('}'):
                    indent-=1
                    # print("28 Indent: "+ str(indent))
                #find the first non space character
                x = re.search(r"[^\s]", line)
                if x.start()!=indent*4:
                    print ("\033[31mWrong indentation on line "+str(lineNum)+"\033[0m")
                    print ("You have:")
                    print (line, end="")
                    # print("You have: " + line, end="")
                    print("Expected: ")
                    print(" "*indent*4 + line.strip())
                    # print("Expected: " + " "*indent*4 + line.strip())
                    correct = False
                    break
                
                #adjust indent if needed
                #if closing brases are not at the begining of the line, like initialization list
                if not(line.strip().startswith('}')) and line.find("}")!=-1:
                    indent-=1
                    # print("46 Indent: "+ str(indent))

                if not(line.find("{")==-1):
                    indent+=1
                    # print("50 Indent: "+ str(indent))
        else: #comment==True and inStatment== True
            #look for the comment end
            if line.strip().find("*/")!=-1:
                comment = False

        #check if we are done with statment
        if line.strip().endswith(';') or line.strip().endswith('}') or line.strip().startswith('#'):
            inStatment = False
        else:
            inStatment = True

        if (line.strip().startswith('cout') or line.strip().startswith('cin')) and not(line.strip().endswith(';')):
            cin_cout_finished=False
        elif cin_cout_finished==False and line.strip().endswith(';'):
            cin_cout_finished=True

    if (correct):
        print("\033[32m    " + str(file.name) + " has passed indentation test\033[0m")

# Gather our code in a main() function
def main():
    if len(sys.argv) == 1:
        print("USAGE: ", format(sys.argv[0]), " <file name>")
    for i in range(1, len(sys.argv)):
        print("\n#####Testing "+ sys.argv[i]+"#####")
        file = open(sys.argv[i], 'r')
        check(file)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
