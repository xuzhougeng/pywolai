
# 基于Wolai API 封装python库

> 目前功能就两个创建块和获取快

安装

```bash
pip install git+https://github.com/xuzhougeng/pywolai
```

## 使用案例

创建一个API，并初始化token

```python

from pywolai import WolaiApi
appId="APP的ID"
appSecret="APP的密钥"

api = WolaiApi()
api.set_token(appId, appSecret)
```

获取一个块

```python
api.get_block("block_id")
```

获取一个块的所有子块

```python
api.get_block_children("block_id")
```

创建一个子块

```python
from pywolai.block import TextBlock

text = TextBlock("Hello")
text2= TextBlock("World")
parent_id = "创建块所在块id"

# 创建单个block
api.create_block(parent_id , text)
# 创建多个block
api.create_blocks(parent_id , [text,text2])
```
