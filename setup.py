from setuptools import setup, find_packages

setup(name="django-greta",
      version="0.1",
      # url='http://github.com/michaelwisely/django-greta',
      license='BSD',
      description="A Django app for displaying Git repos",
      author='Michael Wisely',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=['setuptools',
                        'django>1.6,<1.7',
                        'PyYAML==3.10',
                        'pygments==1.6',
                        'dulwich==0.9.4',
                        'factory_boy==2.3.1',
                        'django-guardian==1.1.1',
                        'django-celery==3.1.9',
                        'South==0.8.4',
                        ],
      )
