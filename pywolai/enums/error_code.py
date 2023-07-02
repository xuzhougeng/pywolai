from enum import Enum


# |值|原因|
# |-|-|
# |17001|缺少参数|
# |17002|参数错误|
# |17003|无效的 token|
# |17004|获取资源失败|
# |17005|资源未找到|
# |17006|服务器内部错误|
# |17007|请求过于频繁|
# |17008|请求体过大|
# |17009|不支持的媒体类型|
# |17010|暂不支持的块类型|
# |17011|权限不足|

class ErrorCode(Enum):
    
    REQUEST_ERROR = 16999 # 请求错误
    NO_RESULT = 17000 # 请求无结果

    PARAM_MISSING = 17001
    PARAM_ERROR = 17002
    INVALID_TOKEN = 17003
    GET_RESOURCE_FAILED = 17004
    RESOURCE_NOT_FOUND = 17005
    INTERNAL_SERVER_ERROR = 17006
    REQUEST_TOO_FREQUENT = 17007
    REQUEST_BODY_TOO_LARGE = 17008
    UNSUPPORTED_MEDIA_TYPE = 17009
    UNSUPPORTED_BLOCK_TYPE = 17010
    INSUFFICIENT_PERMISSIONS = 17011
