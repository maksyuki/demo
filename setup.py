import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-taichi-HERE",
    version="0.0.3",
    author="taichidemo",
    author_email="taichidemo@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        'Documentation':
        'https://packaging.python.org/tutorials/distributing-packages/',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
        'Tracker': 'https://github.com/pypa/sampleproject/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MITAAAA',
    keywords='sample setuptools ddddddddd',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['taichi'],
    python_requires=">=3.7,<3.10",
)
