from setuptools import setup, find_packages

# extract requirements from the requirements file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="emoclassify",
    version="1.0",
    description="A simple CLI app built with Click to classify emotions in text.",
    author="Shrey Gupta",
    author_email="s.gupta@duke.edu",
    packages=find_packages(),
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        emoclassify=emoclassify:main
    """,
    url="https://github.com/guptashrey/Emotion-Classification",
)
