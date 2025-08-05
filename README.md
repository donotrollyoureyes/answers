新版项目结构

backend/

├── app/

│   ├── __init__.py          # 初始化应用

│   ├── routes/              # 路由逻辑

│   │   ├── __init__.py

│   │   └── data_api.py      # 与前端交互的接口

│   ├── services/            # 业务逻辑层

│   │   └── data_service.py  # 处理数据处理/存储等逻辑

│   ├── models/              # 数据模型层

│   │   └── schema.py

│   └── utils/               # 工具函数模块

│       └── logger.py

├── tests/                   # 单元测试目录

│   └── test_data_api.py

├── config.py                # 配置文件

├── requirements.txt

└── README.md
