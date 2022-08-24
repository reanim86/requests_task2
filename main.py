import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def my_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.my_headers()
        file_to_disk = file_path.split('/')
        params = {'path': f'{file_to_disk[-1]}', 'overwrite': 'true'}
        get_link = requests.get(url, headers=headers, params=params)
        link = get_link.json()
        response = requests.put(url=link['href'], data=open(file_path))
        response.raise_for_status()

if __name__ == '__main__':
    path_to_file = './upload/text.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
