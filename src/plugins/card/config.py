from pydantic import BaseSettings


class Config(BaseSettings):

    card_reminder_time_hours: str = "7"
    card_reminder_time_minutes: list = "59"
    card_weather_city: str = "<城市名称>"

    class Config:
        extra = "ignore"
