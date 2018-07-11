from setuptools import setup, find_packages


setup(
    name='django-collect-and-ignore',
    version='0.1.0',
    description='Custom collectstatic for django with ignoring commonly copied unnecessary files',
    url='https://github.com/marinko-peso/django-collect-and-ignore',
    author='Marinko Peso',
    author_email='marinko.peso@gmail.com',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='django collectstatic custom ignore',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Django'
    ],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
