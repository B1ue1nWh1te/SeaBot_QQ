import aiohttp
import asyncio

Headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}


async def get_github_reposity_information(url: str) -> str:
    try:
        UserName, RepoName = url.replace("https://github.com/", "").split("/")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.github.com/users/{UserName}", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                AvatarUrl = RawData["avatar_url"]
                ImageUrl = f"https://image.thum.io/get/width/640/crop/320/viewportWidth/640/png/noanimate/https://socialify.git.ci/{UserName}/{RepoName}/image?description=1&font=Rokkitt&forks=1&issues=1&language=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark&logo={AvatarUrl}"
                return ImageUrl
    except:
        return "获取信息失败"
