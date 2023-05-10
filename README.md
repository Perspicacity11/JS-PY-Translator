# JS-PY-Translator

JS-PY-Translator is a tool for translating snippets of Javascript code into equivalent, formatted Python code using the ChatGPT DaVinci engine API. This project was built with Django and Python 3 in the PyCharm IDE.

## Installation
To get started, you will need to clone this repository to your local machine:

```
git clone https://github.com/Perspicacity11/JS-PY-Translator.git
```

Before running the project, you will need to install its dependencies by running the following command:
```
pip install -r requirements.txt
```
## Environment variables

The OpenAI plugin requires a unique secret key, which you can get through your OpenAI account (this is the best step-by-step guide that I've found: https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/). You need to save the key to a variable called OPENAI_KEY, in a .env file in the top directory of the project. Please be aware that free users can only make limited calls to the API on these keys; I had $18 as standard and each call seems to cost about $0.01.


## Running the project
Once you have installed the dependencies, you can run the project using the following command:

```
python manage.py runserver
```
The project should now be running on http://localhost:8000.

## Contributing
If you would like to contribute to this project, please follow these steps:

- Fork the repository
- Create a new branch for your feature or bug fix
- Make your changes and commit them to your branch
- Push your changes to your forked repository
- Create a pull request to merge your changes into the main repository

## License

This project is distributed under the MIT License.
