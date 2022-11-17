from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requires.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_package1.1.3",
    version="0.1.2",
    author="Vanessa Brandao",
    author_email="vbrandadao.gel@gmail.com",
    description="Pacote de processamento de imagens em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VanessaBMizuno/Processamento-de-imagens-em-Python.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)