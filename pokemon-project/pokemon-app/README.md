# Pokémon Pokedex Application

This project is a web application that allows users to log in and manage their own Pokémon collections using a Pokédex. The application is built with Django for the backend and React for the frontend, utilizing a free Pokémon API to fetch Pokémon data.

## Features

- User authentication (login and registration)
- Add Pokémon to individual user Pokédexes
- View Pokémon details
- RESTful API for data handling

## Technologies Used

- Python
- Django
- Django REST Framework
- React
- Axios for API calls
- PostgreSQL (or any relational database)

## Project Structure

```
pokemon-app
├── backend
│   ├── manage.py
│   ├── backend
│   ├── pokedex
│   └── users
├── frontend
│   ├── public
│   └── src
├── package.json
└── requirements.txt
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Start the Django server:
   ```
   python manage.py runserver
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required npm packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

- Visit `http://localhost:3000` to access the application.
- Users can register, log in, and manage their Pokémon collections.

## License

This project is open-source and available under the MIT License.