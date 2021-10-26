from setuptools import setup, find_packages
import re


with open("README.md", "r") as f:
    long_description = f.read()


with open("opplast/__init__.py") as f:
    version = re.search(
        r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE
    ).group(1)


setup(
    name="autovideo",
    version=version,
    author="wanghaisheng",
    author_email="edwin.uestc@gmail.com",
    description="auto video machine,Upload videos to YouTube using geckodriver, Firefox profiles and Selenium.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/wanghaisheng/autovideo",
    download_url="https://github.com/wanghaisheng/autovideo/tarball/v" + version,
    packages=["autovideo"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["selenium"],
    python_requires=">=3.6",
)
