# Password Generator 🔐

A simple yet powerful web-based password generator built with Django. Generate secure, random passwords with customizable options including length, uppercase letters, numbers, and special characters.

## ✨ Features

- **Customizable Length**: Generate passwords from 6 to 14 characters long
- **Uppercase Letters**: Option to include uppercase letters (A-Z)
- **Numbers**: Option to include numeric digits (0-9)
- **Special Characters**: Option to include special characters (!@#$%^&*+-?)
- **Clean UI**: Simple and intuitive Bootstrap-based interface
- **Instant Generation**: Get your secure password with a single click

## 🚀 Getting Started

### Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Django 1.11 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/apadlo/password_generator.git
   cd password_generator
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   
   Open your web browser and navigate to: `http://127.0.0.1:8000/`

## 📖 Usage

1. **Select Password Length**: Choose a password length between 6 and 14 characters from the dropdown menu (default is 12)

2. **Choose Options**: 
   - Check "Uppercase" to include uppercase letters
   - Check "Numbers" to include numeric digits
   - Check "Special Characters" to include special symbols
   - All options are enabled by default

3. **Generate**: Click the "Generate Password" button

4. **Copy**: Your new secure password will be displayed on the next page. Copy it to use wherever needed!

## 🏗️ Project Structure

```
password_generator/
├── generator/              # Main application
│   ├── templates/         # HTML templates
│   │   └── generator/
│   │       ├── home.html       # Home page with form
│   │       ├── password.html   # Password display page
│   │       └── about.html      # About page
│   ├── views.py           # View functions
│   ├── models.py          # Database models
│   └── admin.py           # Admin configuration
├── password_generator/     # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
└── db.sqlite3             # SQLite database
```

## 🛠️ Technologies Used

- **Django**: Web framework for building the application
- **Python**: Backend programming language
- **Bootstrap 5**: Frontend CSS framework for responsive design
- **SQLite**: Database for development

## 🔒 Security Note

⚠️ **Important**: This password generator currently uses Python's `random` module, which is **NOT** cryptographically secure. For production use or generating passwords that protect sensitive data, the code should be updated to use Python's `secrets` module instead.

**Recommended improvement**: Replace `random.choice()` with `secrets.choice()` in `generator/views.py` for cryptographically secure password generation.

**Note on password length**: The current maximum length is 14 characters. For stronger security, modern guidelines recommend passwords of at least 16-20 characters. Consider this when using generated passwords for sensitive accounts.

## 📝 About

This is a simple Django web application created to demonstrate:
- Basic Django project structure
- Form handling in Django
- Template rendering
- URL routing
- Random password generation logic

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📄 License

This project is open source and available for educational purposes.

## 👤 Author

**apadlo**

- GitHub: [@apadlo](https://github.com/apadlo)

## 🌟 Show Your Support

Give a ⭐️ if this project helped you!

---

Made with ❤️ using Django
