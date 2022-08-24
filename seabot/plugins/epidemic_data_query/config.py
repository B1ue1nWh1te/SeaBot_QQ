from pydantic import BaseSettings


class Config(BaseSettings):
    # 定时提醒开关
    epidemic_data_reminder_start: bool = True

    # 定时提醒推送的群号
    epidemic_data_reminder_groups: list = [""]

    # 定时提醒时间
    epidemic_data_reminder_time: list = ["8:00"]

    # 要查询的城市所在的省份名称
    epidemic_data_province: str = "<省份名称>"

    # 要查询的城市名称
    epidemic_data_city: str = "<城市名称>"

    class Config:
        extra = "ignore"
