#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ddddocr",
    version="1.4.7",
    author="sml2h3",
    description="带带弟弟OCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sml2h3/ddddocr",
    packages=find_packages(where='.', exclude=(), include=('*',)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'onnxruntime', 'Pillow', 'opencv-python-headless'],
    python_requires='<3.11',
    include_package_data=True,
    install_package_data=True,
)
