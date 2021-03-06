import setuptools

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywiz",
    version="0.0.13",
    author="xxRonaldxx",
    author_email="xxRonaldxx@someplace.com",
    description="A PyQt5 wizard package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xxRonaldxx/pywiz",
    license='MIT',
    #packages=setuptools.find_packages(),
    py_modules=['pywiz'],
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ),
    install_requires=['PyQt5'],

)
