<div align="center">

# SeaBot_QQ

SeaBot 计划的 QQ 分支

一个能够获取新闻资讯并推送至 QQ 的群聊机器人

目前支持的信息来源有：

[知乎](https://www.zhihu.com/)、[微博](https://weibo.com/)、[央视新闻](https://news.cctv.com/)、[同花顺快讯](https://news.10jqka.com.cn/realtimenews.html)、[历史上的今天](https://baike.baidu.com/calendar/)

主体基于 [nonebot2](https://github.com/nonebot/nonebot2) 开发

消息推送基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 实现

[![Lisence](https://img.shields.io/github/license/B1ue1nWh1te/SeaBot_QQ)](https://github.com/B1ue1nWh1te/SeaBot_QQ/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/B1ue1nWh1te/SeaBot_QQ?include_prereleases)](https://github.com/B1ue1nWh1te/SeaBot_QQ/releases/)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/)
[![NoneBot Version](https://img.shields.io/badge/nonebot2-red)](https://github.com/nonebot/nonebot2)
[![go-cqhttp Version](https://img.shields.io/badge/gocqhttp-purple)](https://github.com/Mrs4s/go-cqhttp)

</div>

# 声明

项目由 [B1ue1nWh1te](https://github.com/B1ue1nWh1te) 独立完成，若有不足的地方还请指教。

项目会保留最基本的维护(功能也许会更新吧，由于只在自己的班群里使用，所以目前实现的也没有太花里胡哨- -)。

此项目仅可在合理情况下作为学习交流和个人日常使用。

# 已实现功能

- [x] [Call 回复](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/chat)(就是机器人昵称被 Call 时进行简单的回复)

- [x] [定时打卡提醒](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/clockin)(emm 学校每天都要体温打卡 超级管理员可主动调用(防风控无法@全体))

- [x] [知乎热榜推送](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/news)(默认仅展示前十条的标题)

- [x] [微博热搜推送](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/news)(默认仅展示前十条的标题)

- [x] [央视新闻推送](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/news)(默认展示前五条的标题及详情内容)

- [x] [同花顺快讯推送](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/news)(默认展示前五条的标题及详情内容)

- [x] [历史上的今天推送](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins/todaybefore)(数据来源本质上是百度的历史上的今天)

- [x] [所有功能均可定时](https://github.com/B1ue1nWh1te/SeaBot_QQ/tree/main/src/plugins)(推送时间和次数可自行配置)

# 功能调用示例

假设机器人昵称为 `小海` 。

- Call 回复 | `小海`

- 打卡提醒 | `小海-打卡提醒`

* 知乎热榜 | `小海-知乎`
  - 若在一定时间内回复 `详情-1` 机器人会分享对应的链接
  - 或 `小海-知乎 1,2` 这样就会直接分享对应的链接

- 微博热搜 | `小海-微博`

- 央视新闻 | `小海-新闻`

- 同花顺快讯 | `小海-同花顺`

- 历史上的今天 | `小海-历史` (无详情)

# 文档

以下文档可以参考。

- [nonebot2 官方文档](https://v2.nonebot.dev/guide/)

- [go-cqhttp 官方文档](https://docs.go-cqhttp.org/guide/)

- SeaBot_QQ 使用教程(还没写- -)

# 部署

目前只做了容器化部署的教程，常规部署请自行研究，比较简单。

## 容器化部署

使用容器化部署可以让你非常快速地把机器人服务跑起来(一顿操作 调调配置就可以直接用了)。

假设你已经在 Linux 上安装并配置好了 docker 和 docker-compose。

```shell
git clone https://github.com/B1ue1nWh1te/SeaBot_QQ
cd SeaBot_QQ
```

修改`src/plugins`中各功能插件的`config.py`配置。

之后修改 `./go-cqhttp` 中的 `config.yml` 配置文件，一般情况下，在 `account-uin` 字段中填写机器人的 QQ 号，其他保持默认即可。

然后修改 `./` 中的 `.env.prod` 配置文件，一般情况下，修改 `NICKNAME`、`SUPERUSERS`、`GROUP_ID`, 其他保持默认即可。

两项配置修改完成后，在 `SeaBot_QQ` 目录下打开终端，执行如下命令。

```shell
docker-compose up -d
```

等待应用自动部署即可，如有异常，与项目无关，请自行搜索解决方案。

初次使用时，需要在 `go-cqhttp` 端扫码登录机器人账号，可使用如下命令查看并扫码。

```shell
docker logs -f go-cqhttp
```

一切顺利的话，很快就可以用上机器人了。

# 开源许可

本项目使用 [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) 作为开源许可证。
