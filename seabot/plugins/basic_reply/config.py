from pydantic import BaseSettings


class Config(BaseSettings):
    # 随机回复内容
    reply_contents: list = ["?", "怎么说", "[CQ:face,id=277]"]

    class Config:
        extra = "ignore"
