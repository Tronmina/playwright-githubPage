import os
import shutil
import argparse
from datetime import datetime, timedelta

def delete_old_folders(n_days, folder_name):
    # 獲取當前日期
    now = datetime.now()

    # 遍歷指定文件夾中的所有文件和子文件夾
    for filename in os.listdir(folder_name):
        # 獲取文件或子文件夾的完整路徑
        file_path = os.path.join(folder_name, filename)

        # 獲取文件或子文件夾的最後修改時間
        mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

        # 如果文件或子文件夾的最後修改時間早於指定的天數，則刪除它
        if now - mtime > timedelta(days=n_days):
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

if __name__ == "__main__":
    # 創建命令行參數解析器
    parser = argparse.ArgumentParser(description="Delete old folders from a specified directory.")

    # 添加命令行參數
    parser.add_argument("--n-days", type=int, required=True, help="Number of days to keep. Older folders will be deleted.")
    parser.add_argument("--folder-name", type=str, required=True, help="Name of the folder where you store the reports.")

    # 解析命令行參數
    args = parser.parse_args()

    # 刪除舊的部署資料
    delete_old_folders(args.n_days, args.folder_name)
