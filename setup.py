from setuptools import find_packages, setup

package_name = 'robosys_assignment2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Abdelrahman Alhanbali',
    maintainer_email='abdelrahman.alhanbali@gmail.com',
    description='For robosys2024 assignment2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wifispeed = assignment2.wifispeed:main',
        ],
    },
)