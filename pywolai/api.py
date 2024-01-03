from typing import List
import requests
import json
from pywolai.enums import ErrorCode, BlockTypes, RequestMethod, RequestAddr
from pywolai.block import Block
from pywolai.block_format import BlockFormat
from pywolai.database_format import DatabaseFormat

def safe_request(url, method, params=None, data=None, headers=None):
    """安全请求
    :param url: 请求地址
    :param method: 请求方法
    :param data: 请求数据
    :param headers: 请求头
    :return: 请求结果
    """
    try:
        if method == "GET":
            response = requests.get(url,params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=json.dumps(data), headers=headers)
        elif method == "PUT":
            response = requests.put(url, data=json.dumps(data), headers=headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise Exception("不支持的请求方法")
        
        # 状态码不为20x时，抛出异常
        if response.status_code // 100 != 2:
            raise Exception(ErrorCode.REQUEST_ERROR.value, "请求错误")

        data = response.json()["data"]
        if data is None:
            raise Exception(ErrorCode.NO_RESULT.value, "请求无结果")
        return data
    
    except requests.exceptions.RequestException as e:
        #TODO: 返回结果有问题，后续还需要修改
        print(e)
        return None

class WolaiApi:

    def __init__(self, base_url = "https://openapi.wolai.com/v1",  app_id = None, app_secret = None  ):
        """初始化
        :param base_url: API基础URL
        """
        self._base_url = base_url
        if app_id is not None and app_secret is not None:
            self.set_token(app_id, app_secret)
        else:
            self._api_token = None

    # Token
    def set_token(self, app_id, app_secret):
        """创建token
        :param app_id: 应用ID
        :param app_secret: 应用密钥
        """

        url = self._base_url + "/token"
        data = {
            "appId": app_id,
            "appSecret": app_secret
        }
        self._api_token = safe_request(url, "POST", data=data)["app_token"]
  
    def get_token(self):
        """获取token
        """
        return self._api_token

    def reset_token(self, app_id, old_token):
        """重置token
        :param app_id: 应用ID
        :param old_token: 旧token
        """
        url = self._base_url + "/token"
        data = {
            "appId": app_id,
            "appToken": old_token
        }

        self._api_token = safe_request(url, "PUT", data=data)["app_token"]

    # Block
    def get_block(self, block_id):
        """
        :param block_id: 块ID
        :return: BlockFormat Class
        """

        url = self._base_url + "/blocks/" + block_id
        data = safe_request(url, "GET", headers={"Authorization": self.get_token()})

        return BlockFormat(**data)

    def get_block_children(self, block_id, start_cursor:str="undefined", page_size:int=200):
        """
        :param block_id: 块ID
        :param start_cursor: 起始游标
        :param page_size: 每页大小
        """
        url = self._base_url + "/blocks/" + block_id + "/children"
        params = {
            "startCursor": start_cursor,
            "pageSize": page_size
        }
        data = safe_request(url, "GET", params=params, headers={"Authorization": self.get_token()})

        block_list = [ BlockFormat(**block) for block in data ]

        return block_list

    # download media
    def download_media(self, media_id:str, output_dir:str=".", file_name:str=None):
        """
        :param media_id: 媒体ID
        :param output_dir: 输出目录, 默认当前目录
        :param file_name: 文件名, 默认使用媒体ID
        """

        media_block_info = self.get_block(media_id)
        if media_block_info.type not in [ 
            BlockTypes.IMAGE.value,
            BlockTypes.AUDIO.value,
            BlockTypes.VIDEO.value,
        ]:
            raise Exception(ErrorCode.REQUEST_ERROR , "请求的并非媒体" )
        
        media_url = media_block_info.other_fields['media']['download_url']
        # 获取文件类型
        file_type = media_url.split(".")[-1]
        # 获取文件名
        if file_name is None:
            file_name = media_id + "." + file_type

        # 下载文件
        response = requests.get(media_url, stream=True)
        with open(output_dir + "/" + file_name, "wb") as f:
            for chunk in response.iter_content(chunk_size=512):
                f.write(chunk)

    def create_block(self, parent_id:str, block:Block ):
        """
        :param parent_id: 父块ID
        :param block: 单个block 
        """

        url = self._base_url + "/blocks"

        data = {
            "parent_id": parent_id,
            "blocks": block.to_dict() 
        }

        data = safe_request(url, "POST", data = data, headers={"Authorization": self.get_token()})

        return data


    def create_blocks(self, parent_id:str, blocks:List[Block] ):
        """
        :param parent_id: 父块ID
        :param block: 一组block
        """

        url = self._base_url + "/blocks"

        data = {
            "parent_id": parent_id,
            "blocks": [ block.to_dict() for block in blocks ]
        }

        data = safe_request(url, "POST", data= data, headers={"Authorization": self.get_token()})

        return data

    def get_database(self, database_id:str) -> DatabaseFormat:
        """
        :param database_id: 数据库ID
        :return 序列化后的数据库实例
        """
        url = RequestAddr.DATABASE_GET % (self._base_url, database_id)

        data = safe_request(url, RequestMethod.GET, headers={"Authorization": self.get_token()})
        return DatabaseFormat(**data)

    def insert_database(self, database_id:str, value:[{str:any}]):
        """
        :param database_id: 数据库ID
        :return:
        """
        url = RequestAddr.DATABASE_INSERT % (self._base_url, database_id)
        data = {
            "rows": value
        }

        data = safe_request(url, "POST", data = data, headers={"Authorization": self.get_token()})
        return data
