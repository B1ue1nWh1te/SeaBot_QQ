from pydantic import BaseSettings


class Config(BaseSettings):
    # 微博热搜 定时提醒开关
    weibo_reminder_start: bool = False

    # 微博热搜 定时提醒推送的群号
    weibo_reminder_groups: list = [""]

    # 微博热搜 推送数量与推送时间
    weibo_amount: int = 10
    weibo_reminder_time: list = ["8:00"]

    # 知乎热榜 定时提醒开关
    zhihu_reminder_start: bool = False

    # 知乎热榜 定时提醒推送的群号
    zhihu_reminder_groups: list = [""]

    # 知乎热榜 推送数量与推送时间
    zhihu_amount: int = 10
    zhihu_reminder_time: list = ["8:00"]

    # 央视要闻 定时提醒开关
    cctv_reminder_start: bool = False

    # 央视要闻 定时提醒推送的群号
    cctv_reminder_groups: list = [""]

    # 央视要闻 推送数量与推送时间
    cctv_amount: int = 5
    cctv_reminder_time: list = ["8:00"]

    # 同花顺快讯 定时提醒开关
    tonghuashun_reminder_start: bool = False

    # 同花顺快讯 定时提醒推送的群号
    tonghuashun_reminder_groups: list = [""]

    # 同花顺快讯 推送数量与推送时间
    tonghuashun_amount: int = 5
    tonghuashun_reminder_time: list = ["8:00"]

    class Config:
        extra = "ignore"
