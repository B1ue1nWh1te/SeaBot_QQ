from pydantic import BaseSettings


class Config(BaseSettings):

    reminder_time_hours: List[str] = ["0", "8"]
    reminder_time_minutes: List[str] = ["0", "0"]
    first_content: str = "<第一次的提醒内容>"
    second_content: str = "<第二次的提醒内容>"
    weather_city: str = "<要获取天气的城市名称简写>"

    class Config:
        extra = "ignore"
