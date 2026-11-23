from pathlib import Path

from setuptools import find_packages, setup

version = None
exec(Path("wagtail_meta_preview/version.py").read_text(encoding="utf-8"))  # noqa: S102

readme = Path("README.md").read_text(encoding="utf-8")

testing_extras = ["coverage>=7"]

setup(
    name="wagtail-meta-preview",
    version=version,
    description="Add preview panels for meta data to wagtail",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Andreas Bernacca",
    author_email="ante.bernacca@gmail.com",
    url="https://github.com/Frojd/wagtail-meta-preview",
    python_requires=">=3.11",
    install_requires=["wagtail>=7.4"],
    extras_require={
        "testing": testing_extras,
    },
    zip_safe=False,
    license_expression="MIT",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    package_data={},
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: 3.15",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Framework :: Django :: 6.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 7",
        "Framework :: Wagtail :: 8",
    ],
    project_urls={
        "Source": "https://github.com/Frojd/wagtail-meta-preview/",
        "Changelog": "https://github.com/Frojd/wagtail-meta-preview/blob/main/CHANGELOG.md",
    },
)
