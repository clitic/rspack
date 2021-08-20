import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="rspack",
    version="0.1.0",
    description="pack resource files to a python script",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=[],
    url="https://github.com/360modder/rspack",
    author="360modder",
    author_email="apoorv9450@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["rspack"],
    include_package_data=True,
)
