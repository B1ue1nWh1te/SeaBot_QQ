from pydantic import BaseSettings


class Config(BaseSettings):
    # 定时提醒开关
    clockin_reminder_start: bool = True

    # 定时提醒推送的群号
    clockin_reminder_groups: list = [""]

    # 定时提醒时间
    clockin_reminder_time: list = ["0:00", "8:00"]

    # 提醒内容
    clockin_reminder_contents: list = ["<第一次的提醒内容>", "<第二次的提醒内容>"]

    class Config:
        extra = "ignore"
