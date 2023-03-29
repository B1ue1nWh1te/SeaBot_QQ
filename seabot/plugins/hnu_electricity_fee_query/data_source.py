import aiohttp
import asyncio

Headers = {
    'Host': 'wxpay.hnu.edu.cn',
    'Referer': 'http://wxpay.hnu.edu.cn/electricCharge/home/',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    'X-Requested-With': 'XMLHttpRequest'
}


async def get_electricity_fee(park: str, building: str, room: str) -> str:
    try:
        ParkNo = None
        BuildingNo = None
        async with aiohttp.ClientSession() as session:
            async with session.get("http://wxpay.hnu.edu.cn/api/appElectricCharge/parkList", headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Data = RawData["data"]
                for i in Data:
                    if i["Name"] == park:
                        ParkNo = i["Code"]
                        break
                assert(ParkNo != None)
            async with session.get("http://wxpay.hnu.edu.cn/api/appElectricCharge/buildinglist", params={"parkno": ParkNo}, headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Data = RawData["data"]
                for i in Data:
                    if i["Name"] == building:
                        BuildingNo = i["Code"]
                        break
                assert(BuildingNo != None)
            async with session.get("http://wxpay.hnu.edu.cn/api/appElectricCharge/checkRoomNo", params={'parkNo': ParkNo, 'buildingNo': BuildingNo, 'roomNo': room}, headers=Headers, timeout=5) as response:
                RawData = await response.json()
                Data = RawData["data"]["Balance"]
                return Data
    except:
        return "获取信息失败"
