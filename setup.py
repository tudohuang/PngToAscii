from setuptools import setup, find_packages

setup(
    name="png_to_ascii",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pngtoascii=png_to_ascii.__main__:main',
        ],
    },
    install_requires=[
        Pillow
    ],
    include_package_data=True,
    license="MIT",
    description="A package to convert images to ASCII art.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tudohuang/PngToAscii",
    author="Tudo Huang",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
