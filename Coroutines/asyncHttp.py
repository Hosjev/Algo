"""
REST API (asynchronous) example

-input file URLs
    *read it one line AAT, concurrently run that URL
-request them
-scrap out href tags
-output these links/URLs to file
"""
import pathlib
import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse

import aiofiles
import aiohttp
from aiohttp import ClientSession


# Write the output in a certain format?
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML.

    kwargs are passed to `session.request()`.

    Return string
    """
    resp = await session.request(method="GET", url=url, ** kwargs)
    resp.raise_for_status()
    logger.info(f"Response received for {url}: {resp.status}")
    html = await resp.text()
    return html


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    """
    Find HREFs in the HTML of `url`.

    Return set
    """
    found = set()
    try:
        # Here's where we could add aioRedis to check and see if the URL in question
        # has already been crawled. (applicable to a recursive crawl, or--diving deep)
        html = await fetch_html(url=url, session=session, **kwargs)
    except(aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as e:
        logger.error(f"aiohttp exception for {url}: {e}")
        return found
    except Exception as e:
        logger.exception(f"Non-aiohttp exception occurred: {e}")
        return found
    else:
        # We enter a blocking a phase that stops all other non-blocking actions
        # If this were more significant, other than a single regex, we'd use loop.run_in_executor()
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError) as e:
                logger.exception("Error parsing URL {link}: {e}")
                pass  # we don't want to stop, just ACK
            else:
                found.add(abslink)
        logger.info(f"Found {len(found)} links for {url}")
        return found


async def write_one(outfile: IO, url: str, **kwargs) -> None:
    """
    Write the found HREFs from `url` to `file`.
    We're into the asynchronous tasks.

    Return nothing
    """
    result = await parse(url=url, **kwargs)
    if not result:  # a 404 or other
        return None
    async with aiofiles.open(outfile, "a") as f:
        for url_path in result:
            await f.write(f"{url}\t{url_path}\n")
        logger.info(f"Wrote results for source url: {url}")


async def bulk_crawl_and_write(outfile: IO, urls: set, **kwargs) -> None:
    """
    Crawl & write concurrently to `file` for multiple `urls`.
    (we have our urls, now we give each one its own singleton async in tasks)

    Return nothing
    """
    timeout = aiohttp.ClientTimeout(total=30)
    async with ClientSession(timeout=timeout) as session:
        tasks = []
        for url in urls:  # set
            tasks.append(write_one(outfile=outfile, url=url,
                                   session=session, **kwargs))
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    # Basically, run the loop, no args (we could arg the file input/output)
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("URLS/whit.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("OUTPUT/foundwhit.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.run(bulk_crawl_and_write(outfile=outpath, urls=urls))
