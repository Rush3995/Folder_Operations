import os

all_files = ['Text1.txt', 'Text2.txt', 'Text3.txt']
WORKING_DIR = os.path.dirname(__file__)
FOLDER = os.path.join(WORKING_DIR, 'files')


def get_file_path_list(file_names, folder):
    """
    This function provides all files path in list
    :return:
    """
    files_path = ''
    for root, _, files in os.walk(folder):
        for each_file in file_names:
            all_files_path = os.path.join(root, each_file)
            for single_file in file_names:
                if single_file in all_files_path:
                    if not os.path.isfile(os.path.join(
                            FOLDER, single_file)):
                        print(f'{single_file} does not exists in {FOLDER}')
                    else:
                        files_path += f'{os.path.join(FOLDER, single_file)}\n'
    files_path_list = files_path[:-1].split('\n')
    print(files_path_list)
    return files_path_list


if __name__ == '__main__':
    get_file_path_list(all_files, FOLDER)
