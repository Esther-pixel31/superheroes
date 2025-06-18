# Superheroes API
## 📌 Overview

This is a Flask-based API designed for tracking heroes and their superpowers. The API allows clients to create, read, update, and associate heroes and powers through a join model. The API also handles validations and ensures proper cascading deletes of relationships.

## 🚀 Features

- Manage Heroes and their Powers

- Associate heroes and powers through HeroPowers

- Cascade deletes on relationships to clean up dependent data automatically

- Data validation rules for model integrity:

- HeroPower.strength must be: Strong, Weak, or Average

- Power.description must be present and at least 20 characters

## 🛠️ Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/Esther-pixel31/superheroes.git
cd superheroes
```

2. Create and activate a virtual environment

```bash
pipenv install
pipenv shell
```

3. Set up the database

```bash
cd server
flask db upgrade
```

4. Seed the database

```bash
python seed.py
```

5. Run the app

```bash
python app.py
```

## 🌐 API Endpoints

This API exposes the following routes:

- GET `/heroes`: Retrieve a list of all heroes.
- GET `/heroes/{id}`: Retrieve a specific hero by ID.
- GET `/powers`: Retrieve a list of all powers.
- GET `/powers/{id}`: Retrieve a specific power by ID.
- PATCH `/powers/{id}`: Update a specific power by ID.
- POST `/hero_powers`: Create a new HeroPower.

## ✍️ Author

Esther Mutua
[GitHub](https://github.com/Esther-pixel31)
[email](mailto:Estherwanza32@gmail.com)

## 📧 Support

If you have any questions or need further assistance, please don't hesitate to [contact me](mailto:Estherwanza32@gmail.com)

## ⚖️ License

This project is for educational purposes only. All rights reserved by the author.

