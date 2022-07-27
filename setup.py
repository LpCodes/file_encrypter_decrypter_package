from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file_encrypter_decrypter",
    version="0.0.3",
    author="Lpcodes",
    description="A package for Encrypting & Decrypting Files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LpCodes/file_encrypter_decrypter_package",
    project_urls={
        "Bug Tracker": "https://github.com/LpCodes/file_encrypter_decrypter_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    keywords="encryption decryption crypto Encryption secret cryptography password",
    install_requires=[
        "cryptography",
        "keyring",
    ],
    python_requires=">=3.6",
)
