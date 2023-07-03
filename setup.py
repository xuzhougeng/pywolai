from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8' ) as f:
    long_description = f.read()


setup(
    name='pywolai',
    version='0.1.0',
    author='xuzhougeng',
    author_email='xuzhougeng@163.com',
    description='Python wrapper for wolai API',
    packages=find_packages(),
    install_requires=[
        'requests',  
    ],
)

