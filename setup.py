from setuptools import setup, find_packages

setup(
    # 以下为必需参数
    name='bsn-sdk',  # 模块名
    version='0.1.2',  # 当前版本
    description='SDK for BSN(Blockchain Service Network)',  # 简短描述
    packages=['bsn_sdk','bsn_sdk.common'], # 单文件模块写法
    install_requires=['certifi','requests', 'cryptography', 'fabric-sdk-py'],
    # ckages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法

    # 以下均为可选参数
    long_description="bsn-python-sdk is a Python library for communicating with [Blockchain Service Network](https://www.bsnbase.com/), It is used for building blockchain Apps with BSN.",# 长描述
    url='https://github.com/leeduckgo/bsn_py_sdk', # 主页链接
    author='李大狗Leeduckgo@SUIBE', # 作者名
    author_email='leeduckgo@gmail.com', # 作者邮箱
    classifiers=[
        'Intended Audience :: Developers', # 模块适用人群
        'License :: OSI Approved :: MIT License' # 模块的license
        ],
    keywords='blockchain bsn',  # 模块的关键词，使用空格分割
    )
