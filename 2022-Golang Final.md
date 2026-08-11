<img src='https://pic.imgdb.cn/item/630612c816f2c2beb1ad57c6.jpg' align='right' style=' width:150px;height:60 px'/>

# 个人信息
 - 刘鹏亮/ 男/ 1988.12
 - 手机: 151 5710 5503
 - 本科/ 2012.9-2015.6 / 吉林工程技术师范学院/ 计算机科学与技术 (学信网可查)
 - 专科/ 2010.9-2012.6 / 长春工业大学/ 计算机应用
 - 工作年限: 9年
 - Email: liupengliang1012@126.com
 - Github: https://github.com/Allen-LPL
 - dockerhub: https://hub.docker.com/u/liupengliang
 - 个人博客: http://www.liupengliang.com
 - 在线简历: http://www.hangzhouai.com
 
# 工作经历
## 杭州淘游科技 | 高级开发工程师 | 2020.6 - 2022.6
**主要项目:**
1. 基于Golang从0-1开发电商平台
    - 使用Gin框架, Grpc通信, 组建微服务架构, 模块拆分为用户模块, 交易模块, 支付管理模块(包括三方支付), 日志模块等
    - 使用Openresty, Redis, Golang组建高并发场景, 多次完美完成秒杀活动
2. PHP项目的Golang重构
    - 50W日活, 3000QPS平台的重构优化, 将用户, 金融, 后台脚本服务等用Golang重构, 实现了降低成本和性能的提升
    - 使用docker-compose编排服务, 统一开发环境, 横向扩展机器的速度提高一倍
3. 重新部署调整架构, 打造高可用多活架构
    - 防御DDOS攻击
    - 防御CC攻击
    - 分离业务层与数据层
    - 网关层增加降级和限流
    - 增加监控与报警
    - 搭建IDC+ECS混合模式, 增加多活高可用

**其他工作:** <br/>
1. 项目运维自动化部署
2. 处理各项疑难问题及技术方向决策
3. 550G的Mysql数据不关机迁移
4. 分片副本10T的Mongo数据的迁移
5. sql审计, 堡垒机和蜜罐的部署, 增加架构层级
6. 使用Golang实现分布式cron, 增强cron服务服务稳定性及强度, 以此替代Linux Cron

<div STYLE="page-break-after: always;"></div>

## 杭州天钻网络技术 | 高级开发工程师 | 2018.11 - 2020.6
**主要项目:**
1. 跳跳猪pc和H5项目
    - 从0到1开发, 项目成型后组建5人团队, 主要负责核心代码开发, server服务稳定
    - docker-compose编排服务, 实现低成本快速扩容
    - 组建高性能架构, 中间转发层使用php + Openresty, 核心业务逻辑使用Golang开发, 即保障了开发速度又提高了性能

**其他工作:** <br/>
1. 处理各项疑难问题及技术方向决策
2. 对接阿里, 腾讯等三方公司的SDK
3. 运维自动化部署
    
## 霍尔果斯拓美互娱 | PHP研发工程师 | 2015.8 - 2018.11
**主要项目:**
1. 网赚类项目
    - 页游试玩模块的维护
    - 棋牌模块主程, 0到1完成棋牌模块及所有涉及棋牌模块的活动
    - 平台娱乐游戏的脚本维护
2. 宝石星球项目(APP)
    - 挖矿服务, 每日按照算法产生收益
    - 霹霹乐, 农场等cocos游戏后端

**其他工作:** <br/>
1. 对接阿里, 腾讯等三方公司的SDK
2. 优化调整mysql
 
## 长春网翼科技(实习) | PHP研发工程师 | 2014.8 - 2015.7
**主要项目:**
1. 官网项目
    - 使用各类CMS制作官网
2. 二次开发商城项目
    - PHP二次开发商城


<div STYLE="page-break-after: always;"></div>

# 项目经历
## 2021.3 - 2021.6 | 杭州淘游科技有限公司 | 高级开发工程师
**项目描述**: 全兜买电商 <br/>
**角色**: 高级开发工程师 <br/>
**技术**: 使用Gin, Grpc, Protobuf, Nacos, Consul, ElaticSearch组建微服务 <br/>
**工作内容**: 从0-1开发商城, 完成部署架构到最后交付的所有工作  
- Gin框架中间件、工具集、项目框架的设计及代码规范
- 模块拆分为用户模块, 交易模块, 支付管理模块(包括三方支付), 日志模块等
- 使用Nacos, Consul, Kafka, Grpc等完成微服务的治理, 发现和通信
- 使用docker-compose编排各项服务, 实现服务一致性和横向的快速扩展
- 基于gitlab-runner运维自动化编译部署
- Golang内存溢出, 全链路排查等疑难问题的排查与解决
- 多次秒杀活动, 使用Openresty, Redis, Golang组建高并发场景


## 2020.6 - 2021.12 | 杭州淘游科技有限公司 | 高级开发工程师
**项目描述**: Gin重构PHP项目核心模块 <br/>
**角色**: 高级开发工程师 <br/>
**技术**: 使用PHP, Gin, Gorm, Redis, Docker-compose等 <br/>
**工作内容**: PHP项目核心模块Golang重构 
- PHP项目核心模块, 用户, 用户金融, 后台服务脚本的Gin重构
- 实现PHP项目与Golang项目的Grpc和http交互
- KVM虚拟机改造为docker-compose编排
- 使用gitlab-runner运维自动化编译部署
- 处理PHP进程假死等疑难问题

## 2020.6 - 2022.6 | 杭州淘游科技有限公司 | 高级开发工程师
**项目描述**: 架构优化调整 <br/>
**角色**: 高级开发工程师 <br/>
**技术**: 使用Openresty, Lua, Golang, Redis, Docker等 <br/>
**工作内容**: 打造高可用多活架构, 提高项目健壮性 
- 隐藏IP, 组建DDOS防御层
- Openresty + Golang做网关, 防御CC攻击
- 实现降级, 限流, 实现对业务层的防护
- 抵御最高400G的DDOS和5G带宽的CC混合类型的攻击
- 升级验证码为拼图验证
- 部署sql审计, 堡垒机, Zabbix日志监控, 钉钉机器人和短信报警

<div STYLE="page-break-after: always;"></div>  

## 2018.11 - 2020.6 | 杭州天钻网络技术 | 高级开发工程师
**项目描述**: 跳跳猪项目 <br/>
**角色**: 高级开发工程师 <br/>
**技术**: 使用Openresty, Thinkphp, Docker-compose, Golang, Redis等 <br/>
**工作内容**: 跳跳猪pc和H5项目 
- 使用Thinkphp从0到1开发跳跳猪PC项目
- 组建5人团队, 开发跳跳猪H5项目及Golang重构
- docker-compose编排服务, 保障服务一致性, 降低维护难度
- 使用Openresty做网关, PHP做业务开发, 脚本服务使用Golang开发
- 使用Redis完成多次红包雨活动
- 使用Gitlab-runner完成自动化运维

## 2015.8 - 2017.1 | 霍尔果斯拓美互娱 | PHP开发工程师
**项目描述**: 网赚类项目<br/>
**角色**: PHP开发工程师 <br/>
**技术**: 使用ThinkPHP, Mysql, Redis等 <br/>
**工作内容**: 网赚类项目 
- 页游试玩模块的维护
- 从0到1完成棋牌模块及所有涉及棋牌模块的活动
- 后台组件化棋牌管理, 使棋牌广告上新简便易懂
- 平台娱乐游戏的脚本维护

## 2017.1 - 2018.11 | 霍尔果斯拓美互娱 | PHP开发工程师
**项目描述**: 宝石星球项目(APP)<br/>
**角色**: PHP开发工程师 <br/>
**技术**: 使用Yii2, Mysql, Redis, Rabbitmq等 <br/>
**工作内容**: 宝石星球项目(APP) 
- 使用Redis完成百万级别冷用户的挖矿服务, 每日按照算法产生收益
- 使用Rabbitmq异步计算70W日活热用户的挖矿服务, 计算收益
- 霹霹乐, 农场等cocos游戏后端

<div STYLE="page-break-after: always;"></div>  

# 解决的疑难问题
- 抵御400G的DDOS和5G带宽CC混合攻击
  - 调整架构, 根据用户模型做分化
  - 监控服务器性能指标, 设置告警, 提前预警
  - 加强日志审查, 定制Waf
- Mongo副本集切片主从仲裁docker容器化及全量数据同步
  - docker-compose编排切片副本集, 形成一主多从一仲裁
  - 10T数据全量迁移
- 分布式高可用负载, Nginx进程无法重启, 无法杀死
- 仿极验拼图验证
    - [PHP版](https://github.com/Allen-LPL/tncode), 生产使用[Golang版](https://github.com/Allen-LPL/Captcha-Pic)拼图验证.
- PHP进程大量假死问题排查
    - PHP-Fpm调参, 进程数调整
    - Mysql慢查询排查
    - Xhprof分析
- 大量MySQL数据的无感迁移
  - 全量迁移, 将数据批量dump
    - 默认使用MySQL工具
    - dump异常时使用go-dumper
  - 增量迁移
    - 读取binlog, 数据导入消息队列(Kafka), 异步导入数据 
- 加速海外服务器在国内的访问
- 业务服务迁移与扩容
  - docker镜像编排及容器管理实现快速部署
  - gitlab-runner实现运维自动化
- HTTPS出入站的SSL版本问题

# 开源项目
- [Captcha-Pic](https://github.com/Allen-LPL/Captcha-Pic)
    - Golang做的拼图验证, HTML版和Api接口版
- [laradock二次开发](https://github.com/Allen-LPL/Laradock)
    - [laradock](https://github.com/laradock/laradock)是为PHPer制作的开源项目, 在此基础上, 通过修改和完善Docker镜像管理, 使其更适合在生产环境中使用, 其中新增了Openresty, Openresty-Waf, Openresty-Lor, Verynginx, Golang, Python, Walle, Xhgui, Xhprof, Gitlab-Runner, Filebate.
- [webcron](https://github.com/Allen-LPL/webCron) (https://github.com/Allen-LPL/webCron)
    - Golang语言, Beego框架开发, 具有权限管理, 邮件通知, 任务模糊查询及任务终点控制.

# 技术文章
- [golang-map扩容的源码理解](http://www.liupengliang.com/golang-map的扩容/)
- [golang-slice扩容的源码理解](http://www.liupengliang.com/golang-切片的扩容/)

# 技术栈
- 主要语言: Golang, PHP, Lua
- Golang框架: Beego, Gin, gin-vue-admin, zinx
- PHP框架: Thinkphp, Laravel, Yaf, Smart, Yii2
- Golang的Orm: Gorm
- RPC: GRPC, Protobuf
- 非关系数据库: Redis, Memcache, go-cache, BigCache, Mongodb
- 关系数据库: MySQL
- 大数据: ElaticSearch( ElaticSearch + Filebate + Grafana )
- 队列: Kafka
- 网关: Nginx, Openresty
- Waf: Openresty( Waf模块自研 )
- 容器: Docker, Docker-compose
- 持续集成: Gitlab-runner, Webhook
- Code Review及接口性能管理: Xhprof, Xhgui, Tideways, PProf
- 监控: Zabbix 
- 高可用: Consul, Nacos, HA
- 项目管理：制定项目计划、文档建设、代码控制建设、Bug跟踪反馈建设、运维自动化建设、生产环境剥离, MySQL审计建设, 监控平台建设等