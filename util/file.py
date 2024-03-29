import os
import shutil

source_folder = "path_to_source_folder"  # 替换为源文件夹路径
destination_folder = "path_to_destination_folder"  # 替换为目标文件夹路径



def delete_dir_file(dir_path):
    """
    删除文件夹中所有文件
    :param dir_path: 文件夹目录路径
    :return:
    """
    # 遍历文件夹中的文件并删除
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def move_file(source_path,destination_path):
    """
     将源文件夹中的所有文件和文件夹移动到另一个文件夹
    :param dir_path:
    :return:
    """

    for item in os.listdir(source_path):
        source = os.path.join(source_path, item)
        destination = os.path.join(destination_path, item)
        # 移动文件或文件夹到目标文件夹
        shutil.move(source, destination)

def get_latest_report(dir_path):
    """
    文件夹中有多个文件夹，按时间命名的如202307311039，请获取最新的文件夹路径
    :param dir_path:
    :return:最新的文件夹路径
    """
    # 获取目标文件夹中的所有文件夹
    folders = [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

    # 按时间排序文件夹，并获取最新的文件夹
    latest_folder = max(folders, key=lambda x: os.path.getctime(os.path.join(dir_path, x)))

    # 构建最新文件夹的完整路径
    latest_folder_path = os.path.join(dir_path, latest_folder)

    print(latest_folder_path)  # 输出最新文件夹的路径
    return latest_folder_path