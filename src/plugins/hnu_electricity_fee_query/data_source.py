import aiohttp
import asyncio

Headers = {
    'Host': 'wxpay.hnu.edu.cn',
    'Referer': 'http://wxpay.hnu.edu.cn/electricCharge/home/',
    'X-Requested-With': 'XMLHttpRequest',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
}


async def get_electricity_fee(park: str, building: str, room: str) -> str:
    try:
        ParkNo = None
        BuildingNo = None
        async with aiohttp.get("http://wxpay.hnu.edu.cn/api/appElectricCharge/parkList", headers=Headers, timeout=5) as response:
            RawData = await response.json()
            Data = RawData["data"]
            for i in Data:
                if i["Name"] == park:
                    ParkNo = i["Code"]
                    break
            assert(ParkNo != None)
        async with aiohttp.get("http://wxpay.hnu.edu.cn/api/appElectricCharge/buildinglist", params={"parkno": ParkNo}, headers=Headers, timeout=5) as response:
            RawData = await response.json()
            Data = RawData["data"]
            for i in Data:
                if i["Name"] == building:
                    BuildingNo = i["Code"]
                    break
            assert(BuildingNo != None)
        async with aiohttp.get("http://wxpay.hnu.edu.cn/api/appElectricCharge/checkRoomNo", params={'parkNo': ParkNo, 'buildingNo': BuildingNo, 'roomNo': room}, headers=Headers, timeout=5) as response:
            RawData = await response.json()
            Data = RawData["data"]["Balance"]
            return Data
    except:
        return "获取信息失败"
