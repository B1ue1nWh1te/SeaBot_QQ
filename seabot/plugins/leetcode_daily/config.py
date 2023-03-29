from pydantic import BaseSettings


class Config(BaseSettings):
    # 定时提醒开关
    leetcode_reminder_start: bool = False

    # 定时提醒推送的群号
    leetcode_reminder_groups: list = [""]

    # 定时提醒时间
    leetcode_reminder_time: list = ["8:00"]

    class Config:
        extra = "ignore"
