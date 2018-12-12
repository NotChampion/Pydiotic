import setuptools

description = "A Python Wrapper for the Idiotic API."
long_description = open("README.md").read()
version="1.2.0"

packages = ["pydiotic"]

setuptools.setup(
    name="pydiotic",
    version=version,
    description=description,
    long_description=long_description,
    url="https://github.com/TheRainbow/Pydiotic",
    author="The Rainbow",
    license="MIT",
    packages=packages,
    include_package_data=True,
    install_requires=["aiohttp>=2.0.0"]
)
