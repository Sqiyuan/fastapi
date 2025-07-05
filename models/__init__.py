from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base


DB_URL = 'mysql+asyncmy://root:123123@127.0.0.1:3306/fast_api?charset=utf8mb4'

engine = create_async_engine(
    DB_URL, # 数据库连接地址
    echo=True, # 是否打印sql语句
    pool_pre_ping=True, # 检查连接是否正常
    pool_recycle=3600 # 连接回收时间
)

AsyncSessionFactory = sessionmaker(
    engine, # 数据库引擎
    class_=AsyncSession, # 异步session
    expire_on_commit=False # 不会commit之后session就过期
)

Base = declarative_base() # 创建基类

#导入其他模型的Python文件
from models import users