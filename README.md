<div align="center">

# SeaBot_QQ

SeaBot 计划的 QQ 分支
能够获取新闻资讯并推送至 QQ 群 的机器人
目前支持的信息来源有：知乎、微博、央视新闻、同花顺快讯、历史上的今天

基于 [Nonebot2](https://github.com/nonebot/nonebot2) 开发
基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 实现

![Lisence](https://img.shields.io/github/license/B1ue1nWh1te/SeaBot_QQ)
![Release](https://img.shields.io/github/v/release/B1ue1nWh1te/SeaBot_QQ?include_prereleases)
![Python Version](https://img.shields.io/badge/Python-3.7+-blue)
![NoneBot Version](https://img.shields.io/badge/Nonebot2-latest-red)
![go-cqhttp Version](https://img.shields.io/badge/gocqhttp-latest-green)

</div>

# 声明

项目由 [B1ue1nWh1te](https://github.com/B1ue1nWh1te) 独立完成，若有不足的地方还请指教，项目会持续基本的维护(功能嘛想到再更，由于只用在自己的班群里，所以功能也没有花里胡哨- -)。

此项目仅可在合理情况下作为学习交流和个人日常使用。

# 已实现功能

- [x] [Call 回复(就是机器人昵称被 Call 时进行回复)]
- [x] [定时打卡提醒(emm 我们学校每天都要体温打卡 超级管理员可主动调用)]
- [x] [知乎热榜推送(仅标题)]
- [x] [微博热搜推送(仅标题)]
- [x] [央视新闻推送(含详情)]
- [x] [同花顺快讯推送(含详情)]
- [x] [历史上的今天推送]
- [x] [所有推送实现定时(可自行配置)]

# 功能调用示例

假设机器人昵称为`小海`。

- Call 回复-`小海`
- 打卡提醒-`小海-打卡提醒`
- 知乎热榜-`小海-知乎`(若在一定时间内回复`详情-1` 机器人会分享对应的链接) 或 `小海-知乎 1,2`(这样就会直接分享对应的链接)
- 微博热搜-`小海-微博`(同理)
- 央视新闻-`小海-新闻`
- 同花顺快讯-`小海-同花顺`
- 历史上的今天-`小海-历史`(无额外操作)

# 部署

## 容器化部署

假设你已经在 Linux 上安装并配置好了 Docker 和 docker-compose。

```shell
git clone https://github.com/B1ue1nWh1te/SeaBot_QQ
cd SeaBot_QQ
```

修改`src/plugins`中各功能插件的`config.py`配置。

之后修改`./go-cqhttp`中的`config.yml`配置文件，一般情况下，在`acount-uin`字段中填写机器人的 QQ 号，其他保持默认即可。

然后修改`./`中的`.env.prod`配置文件，一般情况下，修改`NICKNAME`、`SUPERUSERS`、`GROUP_ID`,其他保持默认即可。

两项配置修改完成后，在`SeaBot_QQ`目录下打开终端，执行如下命令。

```shell
docker-compose up -d
```

等待应用自动部署即可，如有异常，与项目无关，请自行搜索解决方案。

初次使用时，需要在`go-cqhttp`端扫码登录机器人账号，可使用如下命令查看扫码。

```shell
docker logs -f go-cqhttp
```

# 许可证

本项目使用 [MIT](https://choosealicense.com/licenses/mit/) 作为开源许可证。
