import requests
from pprint import pprint

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
        params = {'path': f'{file_path}', 'overwrite': 'true'}
        get_link = requests.get(url, headers=headers, params=params)
        link = get_link.json()
        response = requests.put(url=link['href'], data=open('./upload/text.txt'))
        pprint(response)



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)






# url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
# token = ''
# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'OAuth '
# }
# params = {'path': 'test.txt', 'overwrite': 'true'}
# get_link = requests.get(url, headers=headers, params=params)
# link = get_link.json()
# response = requests.put(url=link['href'], data=open('./upload/text.txt'))
#
# pprint(response)