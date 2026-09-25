# a_notebook

一个基于 Django 框架开发的轻量级错题/知识点管理 Web 应用。提供题目的创建、查看与管理功能，支持标签分类与掌握状态标记，内置 Django Admin 后台便于管理。

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/EzraX21/a_notebook/">
    <img src="https://img.shields.io/badge/a__notebook-Django%205.x-blue?style=for-the-badge&logo=django" alt="Logo">
  </a>

  <h3 align="center">a_notebook</h3>
  <p align="center">
    一个基于 Django 的轻量级错题/知识点管理 Web 应用
    <br />
    ·
    <a href="https://github.com/EzraX21/a_notebook/issues">报告Bug</a>
    ·
    <a href="https://github.com/EzraX21/a_notebook/issues">提出新特性</a>
  </p>

</p>


 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [版权说明](#版权说明)
- [鸣谢](#鸣谢)

### 上手指南

请将所有链接中的"EzraX21/a_notebook"改为"your_github_name/your_repository"



###### 开发前的配置要求

1. Python >= 3.13
2. MySQL >= 5.7

###### **安装步骤**

1. 克隆项目

```sh
git clone https://github.com/EzraX21/a_notebook.git
cd a_notebook
```

2. 安装依赖

```sh
uv sync
```

3. 配置环境变量

复制环境变量模板文件并修改为实际配置：

```sh
cp a_notebook/.env.example a_notebook/.env
```

编辑 `.env` 文件，填写你的 MySQL 数据库信息：

```
db_name=a_notebook_db
user_name=admin
db_password=your_password
db_host=127.0.0.1
db_port=3306
```

4. 创建数据库

在 MySQL 中创建项目数据库：

```sql
CREATE DATABASE a_notebook_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

5. 运行迁移

```sh
python manage.py migrate
```

6. 创建超级用户（可选）

```sh
python manage.py createsuperuser
```

7. 启动开发服务器

```sh
python manage.py runserver
```

访问以下地址：

- 应用首页：http://127.0.0.1:8000/notes/
- 添加题目：http://127.0.0.1:8000/notes/add/
- 管理后台：http://127.0.0.1:8000/admin/

### 文件目录说明
eg:

```
a_notebook/
├── a_notebook/                  # Django 项目配置目录
│   ├── __init__.py
│   ├── asgi.py                  # ASGI 配置
│   ├── settings.py              # 项目设置（数据库、中间件、模板等）
│   ├── urls.py                  # 根 URL 路由
│   ├── wsgi.py                  # WSGI 配置
│   └── .env.example             # 环境变量模板
├── notes/                       # 错题管理应用
│   ├── __init__.py
│   ├── admin.py                 # Django Admin 注册
│   ├── apps.py                  # 应用配置
│   ├── forms.py                 # 表单定义
│   ├── migrations/              # 数据库迁移文件
│   ├── models.py                # 数据模型（Question）
│   ├── templates/               # HTML 模板
│   ├── tests.py                 # 单元测试
│   ├── urls.py                  # 应用 URL 路由
│   └── views.py                 # 视图逻辑
├── manage.py                    # Django 管理脚本
├── pyproject.toml               # 项目元信息与依赖声明
├── uv.lock                      # uv 依赖锁定文件
├── .gitignore                   # Git 忽略规则
├── .python-version              # Python 版本指定
├── LICENSE                      # MIT 许可证
└── README.md                    # 项目说明文档
```





### 开发的架构 

本项目采用 Django 的 MVT（Model-View-Template）架构模式：

- **Model（模型）**：定义数据模型（Question），通过 Django ORM 与 MySQL 数据库交互
- **View（视图）**：处理 HTTP 请求与响应，包含 question_list（列表展示）和 add_question（新增题目）两个视图
- **Template（模板）**：使用 Django 模板引擎渲染 HTML 页面

项目采用 Django 内置的 Admin 后台进行数据管理，通过 forms.py 中的 QuestionForm 实现表单验证与数据提交。

### 部署

暂无（项目尚处于开发阶段）

### 使用到的框架

- [Django](https://www.djangoproject.com/) - Web 框架
- [PyMySQL](https://pymysql.readthedocs.io/) - MySQL 数据库驱动
- [python-dotenv](https://github.com/theskumar/python-dotenv) - 环境变量管理
- [uv](https://github.com/astral-sh/uv) - Python 包管理与项目构建工具


### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

EzraX21

*您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE](https://github.com/EzraX21/a_notebook/blob/main/LICENSE)

### 鸣谢


- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)

<!-- links -->
[your-project-path]:EzraX21/a_notebook
[contributors-shield]: https://img.shields.io/github/contributors/EzraX21/a_notebook.svg?style=flat-square
[contributors-url]: https://github.com/EzraX21/a_notebook/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EzraX21/a_notebook.svg?style=flat-square
[forks-url]: https://github.com/EzraX21/a_notebook/network/members
[stars-shield]: https://img.shields.io/github/stars/EzraX21/a_notebook.svg?style=flat-square
[stars-url]: https://github.com/EzraX21/a_notebook/stargazers
[issues-shield]: https://img.shields.io/github/issues/EzraX21/a_notebook.svg?style=flat-square
[issues-url]: https://github.com/EzraX21/a_notebook/issues
[license-shield]: https://img.shields.io/github/license/EzraX21/a_notebook.svg?style=flat-square
[license-url]: https://github.com/EzraX21/a_notebook/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ezrax21
