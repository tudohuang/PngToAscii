from setuptools import setup

setup(
    name='PngToAscii',
    version='0.1',
    packages=['png_to_ascii'],
    entry_points={
        'console_scripts': [
            'pngtoascii=png_to_ascii:main',
        ],
    },
    install_requires=[
        'Pillow',
    ],
)
