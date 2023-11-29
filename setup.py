from setuptools import setup, find_packages

setup(
    name='IsraelSentimentAnalyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'pydantic',
        'gpt4all',
    ],
)
