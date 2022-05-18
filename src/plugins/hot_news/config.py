from pydantic import BaseSettings


class Config(BaseSettings):

    weibo_amount: int = 10
    weibo_reminder_time_hours: list = ["7"]
    weibo_reminder_time_minutes: list = ["59"]

    zhihu_amount: int = 10
    zhihu_reminder_time_hours: list = ["7"]
    zhihu_reminder_time_minutes: list = ["59"]

    cctv_amount: int = 5
    cctv_reminder_time_hours: list = ["7"]
    cctv_reminder_time_minutes: list = ["59"]

    tonghuashun_amount: int = 5
    tonghuashun_reminder_time_hours: list = ["7"]
    tonghuashun_reminder_time_minutes: list = ["59"]

    class Config:
        extra = "ignore"
