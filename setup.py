import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tjbProjectTest",
    version="0.0.1",
    author="Tony Bailey",
    author_email="contact@tonyjb.me",
    description="Example package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tjb1092/testAutomation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)



