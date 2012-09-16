from setuptools import setup

setup(
  name = "hubb",
  version="0.0.1",
  description="Twisted PubSubHubbub Hub",
  
  author="Randell Benavidez",
  author_email="josephrandell.benavidez@gmail.com",
  url="http://github.com/randell/hubb/tree/master",
  classifiers=[
    ],
  packages=['hubb', 'hubb.test'],
  data_files=[('hubb/static', ['hubb/static/styles.css']),
              ('hubb/template', ['hubb/template/index.html'])],
  scripts=['bin/hubb'],
)
