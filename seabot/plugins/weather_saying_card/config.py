from pydantic import BaseSettings


class Config(BaseSettings):
    # 定时提醒开关
    card_reminder_start: bool = True

    # 定时提醒推送的群号
    card_reminder_groups: list = [""]

    # 定时提醒时间
    card_reminder_time: list = ["8:00"]

    # 要查询天气的城市名称
    card_weather_city: str = "<城市名称>"

    class Config:
        extra = "ignore"
