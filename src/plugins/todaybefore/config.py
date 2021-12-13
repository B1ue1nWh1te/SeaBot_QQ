from pydantic import BaseSettings


class Config(BaseSettings):

    reminder_time_hour: str = "7"
    reminder_time_minute: str = "59"

    class Config:
        extra = "ignore"
