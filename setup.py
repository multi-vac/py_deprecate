import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_deprecate",
    version="0.0.4",
    author="multi-vac",
    author_email="multivac_7@protonmail.com",
    description="Python Deprecation Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/multi-vac/py_deprecate",
    project_urls={
        "Bug Tracker": "https://github.com/multi-vac/py_deprecate/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
)