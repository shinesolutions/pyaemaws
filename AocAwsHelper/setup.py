import os
import setuptools

readme_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.MD")
with open(readme_file, "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AocAwsHelper",
    version="0.0.4",
    author="ShineSolutions",
    author_email="author@example.com",
    description="AWS Helper Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shinesolutions/pyaemaws",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "boto3==1.9.71",
        "python-dateutil==2.8.0",
        "coverage==5.0.3"
    ]
)
