import asyncio


async def fetch_article():
    print("Fetching article")
    await asyncio.sleep(5)
    print("Fetched article")


async def fetch_author():
    print("Fetching author")
    await asyncio.sleep(5)
    print("Fetched author")


async def fetch_comments():
    print("Fetching comments")
    await asyncio.sleep(5)
    print("Fetched comments")


async def main():
    await asyncio.gather(fetch_article(), fetch_author(), fetch_comments())


asyncio.run(main())
