from setuptools import find_packages, setup

package_name = 'turtle_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        ('share/' + package_name + '/msg',
            ['msg/TurtleState.msg']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='astro',
    maintainer_email='ahmadtovichha@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'motion_publisher = turtle_control.motion_publisher:main',
            'pose_listener = turtle_control.pose_listener:main',
            'motion_controller = turtle_control.motion_controller:main',
            'state_publisher = turtle_control.state_publisher:main',
        ],
    },
)
