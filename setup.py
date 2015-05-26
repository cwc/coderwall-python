from distutils.core import setup

setup(
        name='coderwall',
        version='1.3.0',
        author='Cameron Currie',
        author_email='me@cameroncurrie.net',
        url='http://github.com/cwc/coderwall-python',
        description='A Python module for accessing user data at http://coderwall.com',
        long_description=open('README.rst').read(),
        license='MIT',
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Development Status :: 6 - Mature',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Internet',
            'Topic :: Internet :: WWW/HTTP',
            'Environment :: Console',
            'Environment :: Web Environment'
        ],
        py_modules=['coderwall']
)
