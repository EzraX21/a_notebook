a-notebook
一个基于 Django 框架开发的轻量级笔记/问答管理 Web 应用。提供问题的创建、查看与管理功能，支持标签分类与完成状态标记，内置 Django Admin 后台便于管理。

技术栈
| 技术 | 说明 |

|------|------|

| Python 3.13+ | 编程语言 |

| Django 5.x | Web 框架 |

| MySQL | 数据库 |

| uv | 包管理与项目构建工具 |

| python-dotenv | 环境变量管理 |

项目结构
```

a_notebook/

├── a_notebook/ # Django 项目配置目录

│ ├── __init__.py

│ ├── asgi.py # ASGI 配置

│ ├── settings.py # 项目设置（数据库、中间件、模板等）

│ ├── urls.py # 根 URL 路由

│ ├── wsgi.py # WSGI 配置

│ └── .env.example # 环境变量模板

├── notes/ # 笔记应用

│ ├── __init__.py

│ ├── admin.py # Django Admin 注册

│ ├── apps.py # 应用配置

│ ├── forms.py # 表单定义

│ ├── migrations/ # 数据库迁移文件

│ ├── models.py # 数据模型（Question）

│ ├── templates/ # HTML 模板

│ ├── tests.py # 单元测试

│ ├── urls.py # 应用 URL 路由

│ └── views.py # 视图逻辑

├── manage.py # Django 管理脚本

├── pyproject.toml # 项目元信息与依赖声明

├── uv.lock # uv 依赖锁定文件

├── .gitignore # Git 忽略规则

├── .python-version # Python 版本指定

├── LICENSE # MIT 许可证

└── README.md # 项目说明文档

```

功能特性
**问题/笔记管理** — 创建、查看笔记条目，支持标题、内容、标签和完成状态管理
**Django Admin 后台** — 内置管理界面，可直观管理数据
**表单验证** — 基于 Django Form 的输入验证
**环境配置** — 通过 `.env` 文件管理数据库等敏感配置，避免硬编码
**中文本地化** — 界面与后台已配置为简体中文，时区设为 Asia/Shanghai
**MIT 开源许可** — 可自由使用、修改和分发
环境要求
Python >= 3.13
MySQL >= 5.7
uv（推荐安装：`pip install uv`）
快速开始
1. 克隆项目
```bash

git clone https://github.com/EzraX21/a_notebook.git

cd a_notebook

```

2. 安装依赖
```bash

uv sync

```

3. 配置环境变量
复制环境变量模板文件并修改为实际配置：

```bash

cp a_notebook/.env.example a_notebook/.env

```

编辑 `.env` 文件，填写你的 MySQL 数据库信息：

```

DB_NAME=a_notebook_db

USER_NAME=admin

DB_PASSWORD=your_password

DB_HOST=127.0.0.1

DB_PORT=3306

```

4. 创建数据库
在 MySQL 中创建项目数据库：

```sql

CREATE DATABASE a_notebook_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

```

5. 运行迁移
```bash

python manage.py migrate

```

6. 创建超级用户（可选）
```bash

python manage.py createsuperuser

```

7. 启动开发服务器
```bash

python manage.py runserver

```

访问以下地址：

应用首页：http://127.0.0.1:8000/notes/
添加笔记：http://127.0.0.1:8000/notes/add/
管理后台：http://127.0.0.1:8000/admin/
URL 路由
| 路径 | 视图函数 | 功能 |

|------|----------|------|

| /admin/ | Django Admin | 后台管理 |

| /notes/ | question_list | 笔记列表 |

| /notes/add/ | add_question | 添加笔记 |

数据模型
**Question（笔记）**

| 字段 | 类型 | 说明 |

|------|------|------|

| title | CharField (200) | 笔记标题 |

| content | TextField | 笔记内容 |

| tag | CharField (50) | 标签（默认：笔记） |

| is_mastered | BooleanField | 是否已掌握 |

| created_at | DateTimeField | 创建时间 |

许可证
本项目采用 MIT 许可证 开源。