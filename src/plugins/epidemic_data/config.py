from pydantic import BaseSettings


class Config(BaseSettings):

    epidemic_data_reminder_time_hour: str = "9"
    epidemic_data_reminder_time_minute: str = "0"
    epidemic_data_province: str = "<省份名称>"
    epidemic_data_city: str = "<城市名称>"

    class Config:
        extra = "ignore"
