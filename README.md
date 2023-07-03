# Python Library Based on Wolai API

> Current functionality includes only two features: creating blocks and getting blocks.

Installation:

```bash
pip install pywolai
```

development version

```bash
pip install git+https://github.com/xuzhougeng/pywolai
```

## Usage

Create an API and initialize token:

```python

from pywolai import WolaiApi
appId="APP's ID"
appSecret="APP's secret key"

api = WolaiApi()
api.set_token(appId, appSecret)
```

Get a block:

```python
api.get_block("block_id")
```

Get all child blocks of a block:

```python
api.get_block_children("block_id")
```

Create a child block:

```python
from pywolai.block import TextBlock

text = TextBlock("Hello")
text2= TextBlock("World")
parent_id = "The ID of the block where the new block is to be created"

# Create a single block
api.create_block(parent_id , text)
# Create multiple blocks
api.create_blocks(parent_id , [text, text2])
```

## Image Download

The API can only get block information; images need to be downloaded separately:

```python
api.download_media(media_id="ID of the media")
```

By default, it is downloaded in the current directory with the media ID as the filename.