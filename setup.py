from setuptools import setup, find_packages

# parse version number from elo/__init__.py:
with open("elo/__init__.py") as f:
    info = {}
    for line in f.readlines():
        if line.startswith("version"):
            exec(line, info)
            break

setup_info = dict(
    name="elo-cli",
    version=info["version"],
    author="Bradley Wojcik",
    author_email="bradleycwojcik@gmail.com",
    license="MIT",
    description="Calculate ELO ratings in your terminal.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://bradleycwojcik.github.io/elo-cli/",
    project_urls={
        "Source": "https://github.com/bradleycwojcik/elo-cli/",
        "Bug Tracker": "https://github.com/bradleycwojcik/elo-cli/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click>=8", "peewee>=3", "loguru>=0.5.0"],
    extras_require={"dev": ["black", "pytest", "pytest-cov", "pytest-mock", "codecov"]},
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points="""
        [console_scripts]
        elo=elo.elo:cli
    """,
)

setup(**setup_info)
