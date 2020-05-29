from setuptools import setup, find_packages

setup(
    name="theDarwinProject",
    version="0.6.1",
    description="easy web app to play with genetic algorythms",
    author="Alexandre Gazagnes",
    url="https://github.com/AlexandreGazagnes/theDarwinProject",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pytest",
        "black",
        "flask",
        "WTForms",
        "flask-wtf",
        "Flask-Scss",
        "libsass",
        "flask-session",
        "flask-login",
        "redis",
        "python-dotenv",
    ],
    entry_points="""
        [console_scripts]
        theDarwinProject=uwsgi:main
        """,
)
