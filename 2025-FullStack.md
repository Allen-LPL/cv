<img src='https://pic.imgdb.cn/item/630612c816f2c2beb1ad57c6.jpg' align='right' style=' width:150px;height:60 px'/>

# Personal Information
 - Liu Pengliang / Male / 1988.11
 - Bachelor / 2012.9-2015.6 / Jilin Engineering Normal University / Computer Science and Technology (CHSI Verifiable)
 - Associate / 2010.9-2012.6 / Changchun University of Technology / Computer Applications
 - Years of Experience: 11 Years
 - Twitter: https://x.com/AllenLiou404
 - Email: liupengliang1012@gamil.com
 - Github: https://github.com/Allen-LPL
 - DockerHub: https://hub.docker.com/u/liupengliang
 - Blog: https://www.liupengliang.com
 - Online Resume: https://cv.liupengliang.com

# Highlights
 - **Career Positioning**: Technical Director / Full Stack Architect. Successfully delivered multiple products and architectures from 0 to 1 and 1 to 100.
 - **AI & Algorithms**: Proficient in enterprise-grade RAG intelligent dialogue systems, search & recommendation engines, and related algorithms. In-depth practice in large-scale vector retrieval (ES + Milvus), recall, and ranking strategies.
 - **Search / Vector Retrieval**: Design of ElasticSearch and Milvus retrieval and indexing, supporting large-scale recall and ranking.
 - **Tech Stack**: Primarily Java/Golang/Python/PHP, complemented by Vue/TypeScript. Focus on Backend, AI Algorithms, Distributed Systems, and Microservices.
 - **Architecture Experience**: Microservices / Distributed Systems / High Availability Multi-Active, K8S Cluster Management, OpenResty Gateway Rate Limiting & Disaster Recovery, Hybrid Cloud (AliCloud + IDC).
 - **Performance & Stability**: MySQL Indexing & R/W Splitting, Sharding, Redis Caching, Message Compensation, Sync to Async conversion, and Parallelization.
 - **High Concurrency**: Front-end peak clipping based on OpenResty Gateway & Redis; Backend support via Async Decoupling (RabbitMQ/Kafka), R/W Splitting, and Connection Pool extension.
 - **HA & Multi-Active**: Canary / Rolling Release strategies to ensure stability.
 - **DevOps & O&M**: Docker, CI/CD, CMDB, K8S, Zabbix/Grafana Monitoring, ES Log Platform, GoAccess Log Analysis.
 - **Security & Reliability**: Self-developed WAF/Security Strategies, DDOS/CC Protection experience, Data Consistency & Idempotency Design.
 - **Team Management**: Built and managed teams of 10-50 people from scratch. Experience in Recruitment, Performance Management, Process Standardization, and Engineering Efficiency Improvement.
 - **Business & Delivery**: Iteration of toC platforms, implementation of toB/toG projects (Research Plagiarism Check Intranet Delivery, Cross-border E-commerce).
 - **Collaboration & Drive**: Systems thinking and result-oriented. Smooth cross-departmental coordination, capable of working independently, high stress tolerance, and self-driven learning.


# Work Experience
## Hangzhou Weilan Sports Technology Co., Ltd. | Technical Director | 2023.11 - 2025.09
Peak Team Size: 20, Average: ~10
**Key Projects:**
1. **Moment Sports (WeChat Mini Program / H5 / APP, 0 to 1)**
   - Built and led a 15-person Product/R&D/Design team, streamlining Requirements, Design, R&D, Testing, and Launch processes.
   - Deconstructed business domains, designed overall technical architecture & governance (Spring Boot, Nacos, ES, Redis), and implemented DevOps, Canary Release, and Monitoring/Alerting.
   - Independently completed core backend and partial frontend development, built High Availability & Disaster Recovery systems, ensuring stable operation post-launch.
   - Formulated technical budget and personnel planning, driving company qualifications, compliance, and process implementation.
2. **Peking Union Medical College - Institute of Medical Information · Paper and Image Similarity Check**
   - Managed business docking and solution review, organizing data and permission boundaries according to research scenarios.
   - Architecture & Deployment: Intranet Delivery, Data Security Isolation, CI/CD, and O&M Monitoring.
   - Text/Image Vectorization, Similarity Comparison for Plagiarism Check, supporting Large-scale Library Retrieval.
   - Organized delivery demonstrations and training, completing intranet implementation and acceptance.
3. **Mydesign Cross-border E-commerce Independent Site**
   - Communicated requirements with stakeholders, co-produced product prototypes, and iterated incrementally by module.
   - Built cross-border data synchronization links and task orchestration, handling differences in exchange rates, time zones, taxes, and languages.
   - Automated O&M (AWS + DevOps), optimized domestic access to overseas links and acceleration.
   - Improved First Screen Loading and Key Transaction Metrics, stably handling overseas traffic.

## Shanghai Lianyin Network Technology Group Co., Ltd. | Full Stack Architect | 2022.11 - 2023.11
Peak Team Size: 24, Average: ~14
**Key Projects:**
1. **Pangxie Game Account Trading Network**
   - Independently completed the architecture and service deployment of Pangxie 1.0, transforming it from a standalone unit to a Multi-Active High Availability Distributed Architecture.
   - Perfectly supported 8x business growth.
   - Optimized frontend and backend technical architecture, reducing technical costs and improving Technical ROI.
   - Planned and designed multi-person, multi-environment collaborative development, improving development efficiency and system robustness.
2. **Java-based Pangxie 1.0 Mall Big Data Search**
   - Built and developed the search system from 0 to 1 based on ES. Achieved incremental synchronization by reading binlog asynchronously to ES on top of full MySQL data synchronization.
   - Implemented Game Account Recall, Filtering, Fine Ranking, and Business Re-ranking based on User Personas and User Behavior Data, improving search accuracy and relevance.
3. **Organized & Managed O&M and Big Data Team**
   - Managed technical resources for 104 developers across Pangxie Game Account Trading Network, Pangxie Game Mall, Pangxie Esports Platform, Innovation Division, and IM Customer Service System.
   - Completely withstood a single peak of 600GB DDOS and 15G Bandwidth CC Hybrid Attacks.
4. **Assisted Technical Director in Cost Control & Organizational Management**
   - Assisted in organizational management and project flow management of the technical team, growing from 18 to 104 people.
   - Assisted in personnel flow, code quality, and document management across project groups.

## Hangzhou Taoyou Technology Co., Ltd. | Technical Director | 2020.6 - 2022.6
Peak Team Size: 48, Average: ~30
**Key Projects:**
1. **E-commerce Platform Development from 0-1 based on Golang**
    - Used Gin framework, gRPC communication, built Microservices Architecture. Modules split into User, Trading, Payment Management (including 3rd party payment), Log modules, etc.
    - Used OpenResty, Redis, Golang to build High Concurrency scenarios, successfully completing multiple Flash Sale events.
2. **Java Refactoring of Juxiangyou PHP Project**
    - Refactoring and optimization of a platform with 500k DAU and 3000 QPS. Refactored User, Finance, and Background Script services using Java, improving project robustness and maintainability.
    - Used Docker-Compose for service orchestration, unified development environments, doubling the speed of horizontal machine scaling.
3. **Juxiangyou Redeployment & Architecture Adjustment, Building HA Multi-Active Architecture**
    - Hidden IP, built DDOS Defense Layer.
    - OpenResty + Golang as Gateway, implementing Downgrade, Rate Limiting, Business Layer Protection, and CC Attack Defense.
    - Withstood hybrid attacks of up to 400G DDOS and 5G Bandwidth CC.
    - Upgraded Captcha to Puzzle Captcha.
    - Deployed SQL Audit, Bastion Host, Zabbix Log Monitoring, DingTalk Robot, and SMS Alarms, increasing architecture hierarchy.

## Hangzhou Tianzuan Network Technology | Technical Lead | 2018.11 - 2020.6
Peak Team Size: 8, Average: ~5
**Key Projects:**
1. **Tiaotiaozhu PC and H5 Project**
    - Developed from 0 to 1. After project formation, built a 5-person team, mainly responsible for Core Code Development and Server Stability.
    - Docker-Compose service orchestration, achieving Low-cost Rapid Expansion.
    - Built High-Performance Architecture. Intermediate forwarding layer used PHP + OpenResty, Core Business Logic developed using Golang. Mixed use of HTTP and gRPC protocols ensured development speed while improving performance.

**Other Work:** <br/>
1. Handled various difficult problems and technical direction decisions.
2. Integrated SDKs from third-party companies like Alibaba and Tencent.
3. O&M Automated Deployment.
4. Managed work plans, performance, bonuses, code control, team building, and recruitment for a 5-person technical team. Improved motivation and controlled R&D costs.

## Horgos Tuomei Entertainment | PHP R&D Engineer | 2015.8 - 2018.11
**Key Projects:**
1. **Online Earning Projects**
    - Maintenance of Web Game Trial Module.
    - Lead Programmer for Chess Module, completed Chess Module and all related activities from 0 to 1.
    - Script maintenance for Platform Entertainment Games.
2. **Gem Planet Project (APP)**
    - Mining Service, generating revenue daily according to algorithms.
    - Backend for Cocos games like Pipile, Farm, etc.

**Other Work:** <br/>
1. Integrated SDKs from third-party companies like Alibaba and Tencent.
2. Optimized and adjusted MySQL.


<div STYLE="page-break-after: always;"></div>

# Project Experience
## 2023.11 - 2025.09 | Hangzhou Weilan Sports Technology Co., Ltd. | Technical Director
**Project Description**: Moment Sports <br/>
**Role**: Technical Director <br/>
**Technology**: SpringBoot 2.7, Python, Golang, MyBatis-Plus, MyBatis, MySQL, Redis, Nacos, RabbitMQ, Consul, ElasticSearch, Vue3, TS, Vite, UniApp, Docker, OpenResty, Ansible, etc. <br/>
**Content**: Completed Moment Sports WeChat Mini Program, H5, and APP from 0 to 1.
- Designed infrastructure based on business models and technical budgets, tracked project progress, and coordinated technical resources across departments.
- Advanced from 0 to 1 and 1 to 100, built a complete technical team, responsible for Technical Recruitment, Performance Management, and Technical Budget Formulation & Management.
- Dynamically determined requirements, distributed and tracked tasks, strictly controlling project rhythm and quality.
- Formulated and implemented R&D standards and processes (Frontend/Backend Code Standards, Middleware, CDN, OSS usage standards).
- Built and transformed O&M infrastructure: Evolved from Alibaba Cloud to Alibaba Cloud + IDC Hybrid Cloud.
- Implemented Canary/Rolling Release and Distributed Traffic Governance via OpenResty, reducing production risks.
- Built Automated CI/CD, CMDB, and Internal Wiki; GoAccess for Nginx Log Analysis; Zabbix/Grafana Monitoring; Elasticsearch Log Retrieval.
- Completed core backend development for Users, Accounts, Event Registration, Team Tournament Registration, Merchant Printer Services, etc.
- Completed development of H5 pages and UniApp Mini Programs.
- Optimized for High Concurrency: MySQL Indexing & R/W Splitting, Sharding, Redis Cache Design, Sync to Async & Parallel Reads, Connection Pool Optimization.
- Introduced MQ Compensation Mechanism to ensure data consistency and timely delivery of order messages to club merchants.

**Project Description**: Peking Union Medical College - Institute of Medical Information · Paper/Image Plagiarism Check <br/>
**Role**: Technical Director <br/>
**Technology**: SpringBoot 2.7, Python, MyBatis-Plus, MySQL, Redis, RabbitMQ, Vue3, TS, Vite, Docker, OpenResty, Milvus, ResNet50, CLIP, DenseNet121, Swin Transformer, DINOv2, etc. <br/>
**Content**: Paper/Image Similarity Check for Research Scenarios
- Docked with toG requirements, output technical solutions and budget quotations, produced prototypes using Axure.
- Deconstructed milestones and scheduling, handled task distribution, tracking, and progress control.
- To reduce computing costs, penetrated to local server room via frp and local three-line BGP high-bandwidth lines.
- Built Automated CI/CD via OpenResty Canary/Rolling Release.
- Deployed and managed MySQL, Redis, RabbitMQ, Milvus; designed and maintained indexes.
- Implemented Global PDF Parsing, engineered algorithm implementation, achieved index design and retrieval for 5 million small image vectors.
- Organized delivery demonstrations and training, completed intranet environment deployment and acceptance.

**Project Description**: Mydesign Cross-border E-commerce Independent Site <br/>
**Role**: Technical Director <br/>
**Technology**: SpringBoot 2.7, Python, MyBatis-Plus, MyBatis, MySQL, Redis, Nacos, RabbitMQ, ElasticSearch, Vue3, TS, Vite, UniApp, Docker, OpenResty, Ansible, etc. <br/>
**Content**: Independent Site from Prototype to Overseas Growth
- Docked with stakeholders, co-produced product prototypes and roadmaps.
- Split business modules, planned project cycles, adopted Agile Rolling Iteration.
- Built Technical Architecture and AWS Deployment, O&M Automation, and Cross-border Data Synchronization.
- Optimized Domestic Access to Overseas Network Links and Acceleration.
- Implemented Engineering of Personalized Search & Recommendation, and participated in partial algorithm implementation.

## 2022.11 - 2023.11 | Shanghai Lianyin Network Technology Group Co., Ltd. | Full Stack Architect
**Project Description**: Pangxie Game Account Trading Network <br/>
**Role**: Full Stack Architect <br/>
**Technology**: Docker, OpenResty, ThinkPHP, SpringBoot, ElasticSearch, Zabbix, etc.<br/>
**Content**: Independently completed Pangxie 1.0 architecture and service deployment. Assisted Technical Director in improving service quality, code quality management, and personnel organization management.
- Re-architected the service from a standalone unit (Business side 1 server, Admin side 1 server, QPS 30, DAU 5000) to a Multi-module, Multi-tier, Multi-environment High Availability Architecture.
- Sorted out and extended PHP business logic, re-architected large resource transmission and Websocket services, reducing technical costs and improving service stability.
- Sorted out Frontend Vue2 framework, organized component libraries, adjusted security strategies, and optimized business-side key acquisition security.
- Organized refactoring of Customer Service IM Client, Server, IM Message Service, and Customer Service System. Completed two versions, iteratively improving load capacity.
- Adjusted and planned business-side project team members, managed and controlled Code Quality, CI/CD Standards, Git Standards, O&M and Development Standards, etc.
- Re-sorted and simplified the Search System. Used SpringBoot to complete Game Account Recall, Filtering, Fine Ranking, and Business Re-ranking, reducing RT by 80%.
- Implemented Scheduled Tasks using Golang, ensuring task stability and reliability.
- Implemented Canary/Rolling Release and Distributed Traffic Governance using OpenResty, reducing production risks.
- Used Canal to implement MySQL binlog synchronization to Elasticsearch, achieving large text search functionality via Elasticsearch.
- Used RabbitMQ to implement Async Decoupling and Async Message Processing, while splitting Cold/Hot Data Sources to improve data reading performance.

## 2021.3 - 2021.6 | Hangzhou Taoyou Technology Co., Ltd. | Technical Director
**Project Description**: Quandoumai E-commerce <br/>
**Role**: Technical Director <br/>
**Technology**: Gin, gRPC, Protobuf, Nacos, Consul, ElasticSearch (Microservices) <br/>
**Content**: Developed Mall from 0-1, completed all work from deployment architecture to final delivery.
- Design and Code Standards for Gin framework middleware, toolsets, and project framework.
- Module splitting: User Module, Trading Module, Payment Management Module (including 3rd party payment), Log Module, etc.
- Used Nacos, Consul, Kafka, gRPC, etc., for Microservice Governance, Discovery, and Communication.
- Used Docker-Compose to orchestrate services, achieving service consistency and rapid horizontal expansion.
- Automated Compilation and Deployment based on GitLab-Runner O&M.
- Troubleshooting and resolution of difficult problems like Golang Memory Overflow and Full-link Troubleshooting.
- Multiple Flash Sale activities, using OpenResty, Redis, Golang to build High Concurrency scenarios.

<div STYLE="page-break-after: always;"></div>
## 2020.6 - 2021.12 | Hangzhou Taoyou Technology Co., Ltd. | Technical Director
**Project Description**: Juxiangyou Refactoring <br/>
**Role**: Technical Director <br/>
**Technology**: PHP, Java, SpringBoot 2.7, MyBatis-Plus, Redis, Docker-Compose, etc. <br/>
**Content**: Refactored Core Modules of PHP Project using Java.
- SpringBoot refactoring of PHP project core modules: User, User Finance, Background Service Scripts.
- Implemented gRPC and HTTP interaction between PHP project and Java project.
- Transformed KVM Virtual Machines to Docker-Compose orchestration.
- Automated Compilation and Deployment using GitLab-Runner.
- Handled difficult problems like PHP Process Fake Death.

## 2020.6 - 2022.6 | Hangzhou Taoyou Technology Co., Ltd. | Technical Director
**Project Description**: Juxiangyou Architecture Optimization & Adjustment <br/>
**Role**: Technical Director <br/>
**Technology**: OpenResty, Lua, Golang, Java, Redis, Docker, etc. <br/>
**Content**: Built High Availability Multi-Active Architecture, improving project robustness.
- Hidden IP, built DDOS Defense Layer.
- OpenResty + Golang as Gateway, defending against CC Attacks.
- Implemented Downgrade, Rate Limiting, achieving protection for the Business Layer.
- Withstood hybrid attacks of up to 400G DDOS and 5G Bandwidth CC.
- Upgraded Captcha to Puzzle Captcha.
- Deployed SQL Audit, Bastion Host, Zabbix Log Monitoring, DingTalk Robot, and SMS Alarms.

<div STYLE="page-break-after: always;"></div>

## 2018.11 - 2020.6 | Hangzhou Tianzuan Network Technology | Technical Director
**Project Description**: Tiaotiaozhu Project <br/>
**Role**: Technical Director <br/>
**Technology**: OpenResty, ThinkPHP, Docker-Compose, Golang, Redis, etc. <br/>
**Content**: Tiaotiaozhu PC and H5 Project
- Developed Tiaotiaozhu PC project from 0 to 1 using ThinkPHP.
- Built a 5-person team, developed Tiaotiaozhu H5 project and Golang refactoring.
- Docker-Compose service orchestration, ensuring service consistency and reducing maintenance difficulty.
- Used OpenResty as Gateway, PHP for Business Development, Script Services developed using Golang.
- Used Redis to complete multiple Red Packet Rain activities.
- Completed Automated O&M using GitLab-Runner.

## 2017.1 - 2018.11 | Horgos Tuomei Entertainment | PHP Development Engineer
**Project Description**: Gem Planet Project (APP)<br/>
**Role**: PHP Development Engineer <br/>
**Technology**: Yii2, MySQL, Redis, RabbitMQ, etc. <br/>
**Content**: Gem Planet Project (APP)
- Used Redis to complete Mining Service for millions of cold users, generating revenue daily according to algorithms.
- Used RabbitMQ to asynchronously calculate Mining Service for 700k DAU hot users, calculating revenue.
- Backend for Cocos games like Pipile, Farm, etc.

## 2015.8 - 2017.1 | Horgos Tuomei Entertainment | PHP Development Engineer
**Project Description**: Online Earning Projects<br/>
**Role**: PHP Development Engineer <br/>
**Technology**: ThinkPHP, MySQL, Redis, etc. <br/>
**Content**: Online Earning Projects
- Maintenance of Web Game Trial Module.
- Completed Chess Module and all related activities from 0 to 1.
- Backend componentization of Chess Management, making Chess Ad updates simple and easy to understand.
- Script maintenance for Platform Entertainment Games.

<div STYLE="page-break-after: always;"></div>

# Solved Technical Challenges
- **Withstood 400G DDOS and 5G Bandwidth CC Hybrid Attacks**
  - Adjusted architecture, differentiated based on user models.
  - Monitored server performance metrics, set alarms, and early warnings.
  - Strengthened log review, customized WAF.
- **Mongo Replica Set Sharding Master-Slave Arbitration Docker Containerization & Full Data Sync**
  - Docker-Compose orchestration of Sharding Replica Sets, forming One Master, Multiple Slaves, One Arbiter.
  - Full migration of 10T data.
- **Distributed High Availability Load, Nginx Process Cannot Restart/Kill**
- **Imitation Geetest Puzzle Captcha**
    - [PHP Version](https://github.com/Allen-LPL/tncode), Production used [Golang Version](https://github.com/Allen-LPL/Captcha-Pic) Puzzle Captcha.
- **PHP Process Massive Fake Death Troubleshooting**
    - PHP-FPM parameter tuning, process count adjustment.
    - MySQL Slow Query troubleshooting.
    - Xhprof analysis.
- **Seamless Migration of Massive MySQL Data**
  - Full Migration: Batch dump of data.
    - Default used MySQL tools.
    - Used go-dumper when dump exceptions occurred.
  - Incremental Migration:
    - Read binlog, import data into Message Queue (Kafka), asynchronously import data.
- **Accelerated Domestic Access to Overseas Servers**
- **Business Service Migration & Expansion**
  - Docker image orchestration and container management for rapid deployment.
  - GitLab-Runner for Automated O&M.
- **HTTPS Inbound/Outbound SSL Version Issues**

# Open Source Projects
- [AI Paper Plagiarism Check](https://github.com/Allen-LPL/seven-server) Demo: [https://seven.weilantech.com/](https://seven.weilantech.com/)
    - Provides batch upload detection for PDF documents and images. Supports intra-document, strategy, and full-library check modes. Integrates SIFT, SURF, and other feature point matching algorithms for image similarity analysis. Implements a three-level expert review process and automatically generates standardized detection reports.
- [Captcha-Pic](https://github.com/Allen-LPL/Captcha-Pic)
    - Puzzle Captcha made with Golang, HTML version and API interface version.
- [Laradock Secondary Development](https://github.com/Allen-LPL/Laradock)
    - [laradock](https://github.com/laradock/laradock) is an open source project for PHPers. On this basis, through modification and improvement of Docker image management, it is made more suitable for use in production environments. Added OpenResty, OpenResty-Waf, OpenResty-Lor, VeryNginx, Golang, Python, Walle, Xhgui, Xhprof, GitLab-Runner, Filebeat.
- [webcron](https://github.com/Allen-LPL/webCron) (https://github.com/Allen-LPL/webCron)
    - Developed with Golang language and Beego framework. Features permission management, email notification, fuzzy task query, and task termination control.

# Technical Articles
- [Long Connection Management of IM Project](https://liupengliang.com/posts/%E9%A1%B9%E7%9B%AE%E4%BC%98%E5%8C%96/im%E7%9A%84%E9%95%BF%E8%BF%9E%E6%8E%A5%E7%AE%A1%E7%90%86/)
- [Deep Dive into Golang Map Expansion Source Code](https://liupengliang.com/posts/golang/golang-%E6%BA%90%E7%A0%81%E7%90%86%E8%A7%A3map%E7%9A%84%E6%89%A9%E5%AE%B9/)
- [Golang Slice Expansion Mechanism & Source Analysis](https://liupengliang.com/posts/golang/golang-%E6%BA%90%E7%A0%81%E7%90%86%E8%A7%A3%E5%88%87%E7%89%87%E7%9A%84%E6%89%A9%E5%AE%B9/)
- [Distributed Storage HDFS Architecture Principles & Practice Notes](https://liupengliang.com/posts/lfblog/hadoop/hdfs%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)
- [ETL Tool Kettle Data Processing Practice Notes](https://liupengliang.com/posts/lfblog/hadoop/hdfs%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/)

# Tech Stack
- **Primary Languages**: Java, Python, PHP, Golang, Lua, Vue/TypeScript
- **Frameworks**: Spring Boot, ThinkPHP, Yii, Hyperf, Beego, Gin
- **RPC**: gRPC, Protobuf
- **Data Storage**: MySQL, Redis, MongoDB, Memcache, go-cache, BigCache, Milvus
- **Retrieval/Search**: Elasticsearch (incl. Filebeat+Grafana link)
- **Messaging & Async**: RabbitMQ, Kafka
- **Gateway & WAF**: Nginx, OpenResty (incl. self-developed WAF strategies)
- **Container & Orchestration**: Docker, Docker Compose, Kubernetes
- **CI/Configuration**: GitLab Runner, Webhook, Ansible, CMDB
- **Monitoring & Observability**: Zabbix, Grafana, Elasticsearch Log Platform, PProf
- **HA & Registry**: Nacos, Consul, HA, Keepalived
- **Project Governance**: Project Plan/Docs/Code Standards/Defect Tracking/Automated O&M/Production Environment Isolation & Audit
- **Algorithms**: SIFT, SURF, CLIP, DINOv2, Swin Transformer, ResNet50, DenseNet121