#!/usr/bin/env python
from setuptools import find_packages, setup

with open("wagtail_meta_preview/version.py", "r") as f:
    version = None
    exec(f.read())

with open("README.md", "r") as f:
    readme = f.read()

testing_extras = ["black==19.10b0", "coverage==5.2.1"]

setup(
    name="wagtail-meta-preview",
    version=version,
    description="Add preview panels for meta data to wagtail",
    long_description=readme,
    author="Andreas Bernacca",
    author_email="ante.bernacca@gmail.com",
    url="https://github.com/rinti/wagtail-meta-preview",
    install_requires=["wagtail>=2.7",],
    extras_require={"testing": testing_extras,},
    setup_requires=["wheel"],
    zip_safe=False,
    license="MIT License",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={},
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "License :: OSI Approved :: MIT License",
    ],
)
