from aip import AipOcr
import config

class BaiduOcr(object):
    def __init__(self):
        APP_ID = config.config['APP_ID']
        API_KEY = config.config['API_KEY']
        SECRET_KEY = config.config['SECRET_KEY']
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def getData(self, path):
        # 获取图片信息
        # image = requests.get(url)
        # with open('123.png', "wb") as code:
        #     code.write(image.content)
        image = self.get_file_content(path)
        opt = {
            'language_type':'ENG',
        }
        result = self.client.basicGeneral(image, opt)
        # result = self.client.vinCode(image)
        # print(result)
        # return result['words_result'][0]['words']
        return result


