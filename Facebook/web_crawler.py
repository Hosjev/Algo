#!/usr/bin/python

import sys
sys.path.append("/home/hosjev/.local/lib/python3.6/site-packages")
import re
import asyncio
import aiofiles
import aiohttp
import urllib.error, urllib.parse

from pathlib import Path
from argparse import ArgumentParser
from aiohttp import ClientSession
from typing import IO
sys.path.append(str(Path().joinpath("..", "Utilities")))
from decorators import timer

HREF_RE = re.compile(r'href="(.*?)"')


class WebCrawler:

    async def fetch(self, url: str, session: ClientSession, **kwargs):
        response = await session.request(method="GET", url = url, **kwargs)
        response.raise_for_status()
        html = await response.text()
        return html

    async def parse(self, url: str, **kwargs):
        data = set()
        try:
            html = await self.fetch(url, **kwargs)
        except (aiohttp.ClientError,
                aiohttp.http_exceptions.HttpProcessingError) as e:
            print(e)
            return data
        except Exception as e:
            print(e)
            return data
        else:
            # Blocking
            for link in HREF_RE.findall(html):
                try:
                    l = urllib.parse.urljoin(url, link)
                except (urllib.error.URLError, ValueError):
                    pass
                else:
                    data.add(l)
        return data

    async def single(self, url: str, outfile: IO, **kwargs):
        result = await self.parse(url, **kwargs) # session buried
        if not result: return None
        async with aiofiles.open(outfile, "a") as fh:
            for line in result:
                await fh.write(f"{url}\t{line}\n")

    async def bulk_crawl(self, urls: set, outfile: IO):
        timeout = aiohttp.ClientTimeout(total=30)
        async with ClientSession(timeout=timeout) as session:
            tasks = []
            for url in urls:
                tasks.append(self.single(url, outfile, session=session))
            await asyncio.gather(*tasks)
            

def sync_read(infile):
    with open(infile) as fh:
        urls = set(map(str.strip, fh))
    return urls

@timer
def main(*args):
    here = Path(__file__).parent
    urls = sync_read(here.joinpath("URLS", args[0].infile))
    wc = WebCrawler()
    asyncio.run(wc.bulk_crawl(urls, here.joinpath("OUT", args[0].outfile)))


if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Async WC requires >= Py 3.7+"
    parser = ArgumentParser(description="WebCrawler (async)")
    parser.add_argument("--infile")
    parser.add_argument("--outfile")
    args = parser.parse_args()
    main(args)
