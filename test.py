
if __name__ == '__main__':

    #Current directory
    import os

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("The full path of current directory : " + dir_path)

    f = open("demofile.txt", "rt")