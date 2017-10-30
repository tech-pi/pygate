from setuptools import setup, find_packages

setup(name='dxl-pygate',
      version='0.7.0',
      description='A simplified python interface for Gate.',
      url='https://github.com/Hong-Xiang/pygate',
      author='Hong Xiang',
      author_email='hx.hongxiang@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['fs', 'click', 'pyyaml',
                        'rx', 'jinja2', 'dxl-dxpy>=0.5'],
      scripts=['bin/pygate'],
      zip_safe=False)
