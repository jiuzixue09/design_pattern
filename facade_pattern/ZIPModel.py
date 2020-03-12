import logging
from os import path


class ZIPModel:

    def compress(self, src_file_path, dst_file_path):
        print('ZIP模块正在进行"%s"文件的压缩......' % src_file_path)
        print('文件压缩成功，已保存至"%s"' % dst_file_path)

    def decompress(self, src_file_path, dst_file_path):
        print('ZIP模块正在进行"%s"文件的解压缩......' % src_file_path)
        print('文件解压缩成功，已保存至"%s"' % dst_file_path)


class RARModel:

    def compress(self, src_file_path, dst_file_path):
        print('RAR模块正在进行"%s"文件的压缩......' % src_file_path)
        print('文件压缩成功，已保存至"%s"' % dst_file_path)

    def decompress(self, src_file_path, dst_file_path):
        print('RAR模块正在进行"%s"文件的解压缩......' % src_file_path)
        print('文件解压缩成功，已保存至"%s"' % dst_file_path)


class ZModel:

    def compress(self, src_file_path, dst_file_path):
        print('7Z模块正在进行"%s"文件的压缩......' % src_file_path)
        print('文件压缩成功，已保存至"%s"' % dst_file_path)

    def decompress(self, src_file_path, dst_file_path):
        print('7Z模块正在进行"%s"文件的解压缩......' % src_file_path)
        print('文件解压缩成功，已保存至"%s"' % dst_file_path)


class CompressionFacade:

    def __init__(self):
        self.__zip_model = ZIPModel()
        self.__rar_model = RARModel()
        self.__z_model = ZModel()

    def compress(self, src_file_path, dst_file_path, file_type: str):
        ext_name = '.' + file_type
        full_name = dst_file_path + ext_name
        file_type = file_type.lower()
        if file_type == 'zip':
            self.__zip_model.compress(src_file_path, full_name)
        elif file_type == 'rar':
            self.__rar_model.compress(src_file_path, full_name)
        elif file_type == '7z':
            self.__z_model.compress(src_file_path, full_name)
        else:
            logging.error('Not support this format: %s' % file_type)
            return False
        return True

    def decompress(self, src_file_path, dst_file_path):

        base_name = path.basename(src_file_path)
        ext_name = base_name.split('.')[-1].lower()
        if ext_name == 'zip':
            self.__zip_model.decompress(src_file_path, dst_file_path)
        elif ext_name == 'rar':
            self.__rar_model.decompress(src_file_path, dst_file_path)
        elif ext_name == '7z':
            self.__z_model.decompress(src_file_path, dst_file_path)
        else:
            logging.error('Not support this format: %s' % ext_name)
            return False
        return True


def test_compression():
    facade = CompressionFacade()
    facade.compress('/home/test/test.md', '/home/test/test', 'zip')
    facade.decompress('/home/test/test.zip', '/home/test/test.md')
    print()

    facade.compress('/home/test/test.md', '/home/test/test', 'rar')
    facade.decompress('/home/test/test.rar', '/home/test/test.md')
    print()

    facade.compress('/home/test/test.md', '/home/test/test', '7z')
    facade.decompress('/home/test/test.7z', '/home/test/test.md')
    print()


if __name__ == '__main__':
    test_compression()

