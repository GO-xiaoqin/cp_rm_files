import os
import logging
import shutil
import sys
import threading
import time

from configparser import ConfigParser


logging.basicConfig(level=logging.INFO)

class UbuntuFiles(object):
    '''
    需求：
    在Ubuntu下通过这个文件可以批量复制和删除
    '''
    thread_list = []

    def __new__(cls):
        cls.files()
        return super().__new__(cls)

    def __init__(self):
        self.rm_files = dict(self.section)['rm_files'].split(',')
        self.cp_files = dict(self.section)['cp_files'].split(',')
        self.cp_or_rm_files_path = dict(self.section)['cp_or_rm_files_path']

    def copy_files(self, file):
        # 复制文件
        if self.cp_or_rm_files_path and file:
            f = './' + file
            cp_file = self.cp_or_rm_files_path + file
            if not os.path.exists(cp_file):
                try:
                    shutil.copy(f, cp_file)
                    logging.info('复制成功！！！')    
                except shutil.SameFileError as identifier:
                    logging.error(identifier)
                    return
                except FileNotFoundError as identifier:
                    logging.error(identifier)
                    return
            else:
                logging.warning('文件已存在！！！')
                return
        else:
            logging.error("请先配置文件！！！")
            return

    def remove_files(self, file):
        # 删除文件
        if self.cp_or_rm_files_path and file:
            f = self.cp_or_rm_files_path + file
            if os.path.exists(f):
                os.unlink(f)
                logging.info('删除成功！！')
            else:
                logging.warning('文件不存在！！！')
                return
        else:
            logging.error("请先配置文件！！！")
            return

    @classmethod
    def files(cls):
        if os.path.exists('./files.conf'):
            cf = ConfigParser()
            cf.read('files.conf')
            section = cf.sections()[0]
            cls.section = cf.items(section)
            return cls
        else:
            logging.error('配置文件不存在！！！')
            return cls
    
    def run(self):
        # 函数执行
        if len(sys.argv) == 2:
            if sys.argv[1] == 'cp':
                for file in self.cp_files:
                    if file == '*':
                        # TODO:复制该文件夹下所有的文件
                        pass
                    else:
                        t = threading.Thread(target=self.copy_files, args=(file,))
                        self.thread_list.append(t)
            elif sys.argv[1] == 'rm':
                for file in self.rm_files:
                    t = threading.Thread(target=self.remove_files, args=(file,))
                    self.thread_list.append(t)
            else:
                logging.error("请输入合适的参数！！！")
            # 执行线程
            for t in self.thread_list:
                t.setDaemon(True)
                t.start()
            for t in self.thread_list:
                t.join()
            logging.info("线程结束，操作完成！！！")
        elif len(sys.argv) == 1:
            logging.warning("请选择需要的操作！！！")
        else:
            logging.error("请输入合适的参数！！！")


if __name__ == "__main__":
    files = UbuntuFiles()
    files.run()
    
