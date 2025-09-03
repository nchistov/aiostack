# AIOStack
## Modern async StackExchange API wrapper (Inspired by PyStackAPI)

### Library is in development! Version 0.1.0a

### Installation

```shell
$ pip install git+https://github.com/nchistov/aiostack.git
```

### Usage

Simple usage:

```python
from aiostack import Site
from aiostack.sites import StackOverflow

import asyncio

site = Site(StackOverflow)

async def main():
    answers = await site.get_answers_by_id([12])

    print(answers)

asyncio.run(main())
```
