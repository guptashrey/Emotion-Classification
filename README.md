[![Python Continuous Integration](https://github.com/guptashrey/Emotion-Classification/actions/workflows/main.yml/badge.svg)](https://github.com/guptashrey/Emotion-Classification/actions/workflows/main.yml)

# Emotion-Classification
**Duke AIPI 561 MLOPS Project 1 by Shrey Gupta**

## Project Description
This CLI tool allows you to classify the given text into different classes of emotions. It predicts Ekman's 6 basic emotions, plus a neutral class:
- anger 🤬
- disgust 🤢
- fear 😨
- joy 😀
- neutral 😐
- sadness 😭
- surprise 😲

The tool uses the `j-hartmann/emotion-english-distilroberta-base` model from [Hugging Face](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base). The user needs to provide the tool with the path to the text file, and it will predict the top 3 emotions.

## Setting up the Tool
**1. The tool has been packaged into a package, and can be installed using the following command:**  
```
make install
```
This upgrades pip, installs the requirements and sets up the cli tool with `emoclassify` as the command input

**2. To run the formatting on the code:**  
```
make format
```

**3. To run linting on the code:**  
```
make lint
```  

**4. To run unit tests on the code:**  
```
make test
```  

**5. To run all the steps including setup, code formating using black, linting and testing:**  
```
make all
```

## Using the Tool
The CLI tool has an entry point `emoclassify` which can be used to run the tool. The tool takes in one argument: `--file-path` i.e. the path to the text file.

To run the tool, you can use the following command:
```
emoclassify --file-path <path_to_text_file>
```

## Continuous Integration using Github Actions
The tool has been integrated with Github Actions to run the following steps on every push to the main branch:
1. Installing dependencies and environment setup using make setup
2. Linting the code using pylint
3. Formatting the code using black
4. Running unit tests on the code usoing pytest

The github workflow yaml file can be found [here](.github/workflows/main.yml)

## Project Structure
The project data and code files are arranged in the following manner:

```
├── .github                           <- directory for github templates
    ├── workflows                     <- directory for github actions workflow
        ├── main.yml                  <- github actions workflow file
├── tests                             <- directory for unit tests   
    ├── test_emoclassify.py           <- script to run unit tests on the model
    ├── test_1.txt                    <- sample text file 1 to run the unit test
    ├── test_2.txt                    <- sample text file 2 to run the unit test
├── .gitignore                        <- git ignore file
├── emoclassify.py                    <- script to run the hugging face model 
├── LICENSE                           <- license file
├── Makefile                          <- makefile to run the setup, linting and testing
├── README.md                         <- description of project and how to set up and run it
├── requirements.txt                  <- requirements file to document dependencies
├── setup.py                          <- setup file for the package
```