from pydantic import BaseSettings


class Config(BaseSettings):
    # 定时提醒开关
    todaybefore_reminder_start: bool = True

    # 定时提醒推送的群号
    todaybefore_reminder_groups: list = [""]

    # 定时提醒时间
    todaybefore_reminder_time: list = ["8:00"]

    class Config:
        extra = "ignore"
