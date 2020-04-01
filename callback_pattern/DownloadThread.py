import requests

from threading import Thread


class DownloadThread(Thread):

    CHUNK_SIZE = 1024 * 512


    def __init__(self, file_name, url, save_path, call_back_progress, call_back_finished):
        super().__init__()
        self.__file_name = file_name
        self.__url = url
        self.__save_path = save_path
        self.__call_back_progress = call_back_progress
        self.__call_back_finished = call_back_finished

    def run(self) -> None:
        read_size = 0
        r = requests.get(self.__url, stream=True)
        total_size = int(r.headers.get('Content-Length'))
        with open(self.__save_path, 'wb') as file:
            for chuck in r.iter_content(chunk_size=self.CHUNK_SIZE):
                if chuck:
                    file.write(chuck)
                    read_size += self.CHUNK_SIZE
                    self.__call_back_progress(self.__file_name, read_size, total_size)
        self.__call_back_finished(self.__file_name)


def testDownload():

    def download_progress(file_name, read_size, total_size):
        percent = (read_size / total_size) * 100
        print('[下载%s] 下载进度：%.2f%%' % (file_name, percent))

    def download_finished(file_name):
        print('[下载%s] 文件下载完成！' % file_name)

    print('开始下载 TestForDownload1.pdf......')
    download_url1 = 'http://cachefly.cachefly.net/100mb.test'
    download1 = DownloadThread('TestForDownload1', download_url1, './download/TestForDownload1.test', download_progress,
                               download_finished)
    download1.start()

    download_url2 = 'http://hbimg.huabanimg.com/1ff95bdf3070e1fbff052a03ed353b409749f5ea16a809-WXy25b_fw658'
    download2 = DownloadThread('TestForDownload2', download_url2, './download/TestForDownload2.jpg', download_progress,
                               download_finished)
    download2.start()
    print('执行其他任务......')


testDownload()
