from setuptools import setup, find_packages

setup(
    name='zamtelsms',
    packages = find_packages(),
    version='0.0.4',
    description='A small python Package for Zamtel bulk SMS API',
    author='Mathews Musukuma',
    author_email='sikaili99@gmail.com',
    url='https://github.com/Mathewsmusukuma/zamtel-sms',
    py_modules=['zamtelsms'],
    install_requires=['requests','python-decouple'],
    license='MIT License',
    zip_safe=False,
    keywords='zamtel sms package',
      classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ]
    )
