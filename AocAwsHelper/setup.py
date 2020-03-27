import os
import setuptools

readme_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.MD")
with open(readme_file, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AocAwsHelper",
    version="0.0.4",
    author="Shine Solutions",
    author_email="opensource@shinesolutions.com",
    description="AEM on AWS API Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shinesolutions/pyaemaws",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "boto3==1.9.71",
        "coverage==5.0.3",
        "python-dateutil==2.8.0"
    ]
)
