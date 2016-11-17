"""
Setup script.
"""

from setuptools import setup, find_packages

if __name__ == '__main__':
    with \
            open('requirements.in') as requirements, \
            open('README.md') as readme:
        setup(
            name='mailmq',
            use_scm_version=True,
            description='Sendmail compatible SMTP relay over MQ',
            author='Danielle Madeley',
            author_email='danielle.madeley@squareweave.com.au',
            url='https://github.com/squareweave/mailmq',
            long_description=readme.read(),
            classifiers=[
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python',
                'Programming Language :: Python :: 3',
            ],

            packages=find_packages(exclude=['tests']),
            include_package_data=True,

            entry_points={
                'console_scripts': [
                    'mailmq = mailmq.client:main',
                ],
            },

            setup_requires=['setuptools_scm'],

            install_requires=requirements.readlines(),
        )
