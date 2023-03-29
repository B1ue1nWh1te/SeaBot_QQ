import aiohttp
import asyncio

Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}


async def get_github_reposity_information(url: str) -> str:
    try:
        UserName, RepoName = url.replace("https://github.com/", "").split("/")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.github.com/users/{UserName}", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                AvatarUrl = RawData["avatar_url"]
                ImageUrl = f"https://image.thum.io/get/width/1280/crop/640/viewportWidth/1280/png/noanimate/https://socialify.git.ci/{UserName}/{RepoName}/image?description=1&font=Raleway&forks=1&issues=1&language=1&logo={AvatarUrl}&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Light"
                return ImageUrl
    except:
        return "获取信息失败"
