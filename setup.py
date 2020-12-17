from setuptools import find_packages, setup

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="github-demo",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["PyYAML", "lxml", "pydantic"],
    extras_require={
        "dev": ["black", "mypy", "wheel"],
        "distribute": ["twine"],
    },
    description="Demo: Bugout GitHub integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Neeraj Kashyap",
    author_email="neeraj@bugout.dev",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
    ],
    url="https://github.com/bugout-dev/github-demo",
    entry_points={
        "console_scripts": [
            "github.demo=demo.render:main"
        ]
    },
)
