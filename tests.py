from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def main():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    '''working_dir = 'calculator'
    #print(get_file_content(working_dir, "lorem.txt"))
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))'''
    '''root_contents = get_files_info(working_dir, '.')
    print(root_contents)
    pkg_contents = get_files_info(working_dir, 'pkg')
    print(pkg_contents)
    bin_contents = get_files_info(working_dir, 'bin')
    print(bin_contents)
    up_contents = get_files_info(working_dir, '..\\')
    print(up_contents)'''
main()
