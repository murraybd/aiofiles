#!/usr/bin/python3

import asyncio
import aiofiles

async def test_aiofiles():
    async with aiofiles.open('README.rst', 'r') as fp:
        contents = await fp.read()

    assert('aiofiles' in contents)


event_loop = asyncio.get_event_loop_policy().get_event_loop()
try:
    event_loop.run_until_complete(test_aiofiles())
finally:
    event_loop.close()
