import setuptools

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywiz",
    version="0.0.2",
    author="Ron Gatewood",
    author_email="ronald.l.gatewood@gmail.com",
    description="A PyQt5 wizard package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xxRonaldxx/pywiz",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=['PyQt5'],

)
