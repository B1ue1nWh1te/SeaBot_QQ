from pydantic import BaseSettings


class Config(BaseSettings):

    clockin_reminder_time_hours: list = ["0", "8"]
    clockin_reminder_time_minutes: list = ["0", "0"]
    clockin_reminder_contents: list = ["<第一次的提醒内容>", "<第二次的提醒内容>"]

    class Config:
        extra = "ignore"
