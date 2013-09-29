from os import mkdir
from os import listdir
from os import path
from shutil import move

from_path = "/Users/breannalynn/projects/week1project/original_files/"
to_path = "/Users/breannalynn/projects/week1project/%s/"

#create list of files to be moved
file_list = listdir(from_path)

#make 26 directories
def make_directories(to_path):
    for i in range(97, 123):
        letter = chr(i)
        if not path.exists(to_path % letter):
            mkdir(to_path % letter)


#iterate through list and move each file to correct directory
def alphabetize_files(from_path, to_path):
    for given_file in file_list:
        if given_file != ".DS_Store":
            letter = given_file[0]
            move(from_path + given_file, to_path % letter)

make_directories(to_path)
alphabetize_files(from_path, to_path)




