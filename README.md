# FOSSDB

[![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)  
![Django Test](https://github.com/kristoferssolo/FOSSDB/actions/workflows/test.yml/badge.svg)  
![Ruff](https://github.com/kristoferssolo/FOSSDB/actions/workflows/ruff.yml/badge.svg)  


FOSSDB is an open-source web application that helps users find, contribute, and collaborate on free and open-source software (FOSS) projects.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Clone the repository and `cd` into it.
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Enter your `SECRET_KEY` and database information into `config.json` file.
4. Run database migrations:
```sh
python manage.py migrate
```
5. Create a superuser:
```sh
python manage.py createsuperuser
```
6. Run the development server:
```sh
python manage.py runserver
```

## Usage
After following the installation steps, you can access the application at [https://localhost:8000](https://localhost:8000).
Here are some of the features:
- Browse projects by programming language, license, or search term
- View project details, including programming languages, licenses, and descriptions
- Create a new project and add programming languages and licenses
- Edit and delete existing projects

## Contributing
Contributions are always welcome! Here are some ways to get started:
1. Fork the repository and make your changes.
2. Submit a pull request.
3. Respond to open issues or submit new ones.
4. Improve documentation.

## License
This project is licensed under the [GPL3 License](https://www.gnu.org/licenses/gpl-3.0.en.html). See the [LICENSE](./LICENSE) file for details.
