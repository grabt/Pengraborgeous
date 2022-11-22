from setuptools import setup

setup(
    name="three-body-problem",
    version="1.0.0",
    author="Tyler & Norton",
    packages=["three_body_problem"],
    install_requires=["pydantic", "pandas", "numpy"],
    extras_require={"dev": ["pydocstyle", "pylint", "black", "isort"]},
)
