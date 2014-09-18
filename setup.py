from setuptools import setup

setup(name='assemblyassets',
      version='0.1',
      author='Andrew Barisser',
      author_email='barisser@gmail.com',
      license='MIT',
      description='Digital Tokens on the Bitcoin Blockchain',
      packages=['assemblyassets'],
      install_requires=[
      Flask==0.10.1
      Flask-SQLAlchemy==1.0
      MarkupSafe==0.23
      SQLAlchemy==0.9.7
      Werkzeug==0.9.6
      bitcoin==1.1.10
      ecdsa==0.11
      gunicorn==19.1.0
      itsdangerous==0.24
      psycopg2==2.5.3
      redis==2.10.3
      requests==2.3.0
      virtualenv==1.11.6
      wsgiref==0.1.2
      pytest
      Flask-Scss

      ]
    )
