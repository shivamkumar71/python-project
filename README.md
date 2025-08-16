# 🐍 Python Projects Collection

A comprehensive collection of Python applications showcasing various programming concepts, from basic utilities to complex simulations and games. This repository contains 10 distinct Python projects, each demonstrating different aspects of Python programming.

## 📁 Project Overview

| Project | Category | Description | Features |
|---------|----------|-------------|----------|
| **Number Guessing Game** | Game | Interactive number guessing game with difficulty levels | Random number generation, user input validation |
| **Alarm Clock** | Utility | Feature-rich alarm clock with voice announcements | GUI interface, text-to-speech, time management |
| **WeatherPro** | API Integration | Professional weather application with GUI | Real-time weather data, forecast, beautiful UI |
| **ATM Simulation** | Banking | Complete ATM system simulation | PIN authentication, transactions, history |
| **Snake Game** | Game | Classic snake game implementation | Game logic, user interaction |
| **Train Status** | Utility | Train status checking application | Real-time updates, scheduling |
| **College Library System** | Management | Library management system | Book tracking, user management |
| **URL Shortener** | Web Utility | URL shortening service | Link management, analytics |

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Required packages (install via pip):
```bash
pip install -r requirements.txt
```

### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-projects-collection.git
cd python-projects-collection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📋 Individual Project Details

### 1. Number Guessing Game (`number_guess.py`)
**Category:** Game Development  
**Description:** A simple yet engaging number guessing game where the computer generates a random number between 1-100 and the player has to guess it.

**How to Run:**
```bash
python number_guess.py
```

**Features:**
- Random number generation (1-100)
- Attempt tracking
- Input validation
- Success feedback with attempt count

### 2. Alarm Clock (`alarm.py`)
**Category:** Utility Application  
**Description:** A functional alarm clock with voice announcements using text-to-speech technology.

**How to Run:**
```bash
python alarm.py
```

**Features:**
- Set custom alarm time
- Voice announcements using pyttsx3
- Simple command-line interface
- Real-time time checking

### 3. WeatherPro (`weather_professional.py`)
**Category:** API Integration / GUI Application  
**Description:** A professional-grade weather application with modern GUI using CustomTkinter. Provides real-time weather data and forecasts.

**How to Run:**
```bash
python weather_professional.py
```

**Features:**
- Modern GUI with CustomTkinter
- Real-time weather data from Open-Meteo API
- 7-day forecast
- Recent searches history
- Beautiful weather icons and animations
- Responsive design

**Dependencies:**
```bash
pip install customtkinter pillow requests
```

### 4. ATM Simulation (`ATM_simulation.py`)
**Category:** Banking Simulation  
**Description:** A comprehensive ATM system simulation with PIN authentication, transactions, and history tracking.

**How to Run:**
```bash
python ATM_simulation.py
```

**Features:**
- PIN authentication (4-digit)
- Balance inquiry
- Cash deposit
- Cash withdrawal
- PIN change functionality
- Transaction history
- Account locking after failed attempts

### 5. Snake Game (`snake.game.py`)
**Category:** Game Development  
**Description:** A simple implementation of the classic Snake game with basic game mechanics.

**How to Run:**
```bash
python snake.game.py
```

**Features:**
- Snake movement logic
- Food generation
- Score tracking
- Game over detection

### 6. Train Status (`train_status.py`)
**Category:** Utility / API Integration  
**Description:** Application to check real-time train status and schedules.

**How to Run:**
```bash
python train_status.py
```

**Features:**
- Real-time train status
- Schedule checking
- Route information

### 7. College Library System (`college.libraby.system.py`)
**Category:** Management System  
**Description:** A comprehensive library management system for colleges.

**How to Run:**
```bash
python college.libraby.system.py
```

**Features:**
- Book catalog management
- Student/user management
- Issue/return tracking
- Search functionality
- Fine calculation

### 8. URL Shortener (`main.sorten.py`)
**Category:** Web Utility  
**Description:** A URL shortening service similar to bit.ly.

**How to Run:**
```bash
python main.sorten.py
```

**Features:**
- URL shortening
- Custom aliases
- Click analytics
- Link management

## 🛠️ Technical Stack

### Core Technologies
- **Python 3.7+** - Primary programming language
- **Standard Library** - Utilizing Python's built-in modules
- **Third-party Libraries** - Specific to each project

### GUI Frameworks
- **CustomTkinter** - Modern GUI framework for desktop applications
- **Tkinter** - Standard GUI toolkit for Python

### API Integrations
- **Open-Meteo API** - Weather data
- **Various REST APIs** - For different utility services

### Development Tools
- **VS Code** - Recommended IDE
- **Git** - Version control
- **Virtual Environment** - Isolated development environment

## 📊 Project Structure

```
python-projects-collection/
├── number_guess.py              # Number guessing game
├── alarm.py                     # Alarm clock with voice
├── weather_professional.py      # Professional weather app
├── ATM_simulation.py           # ATM system simulation
├── snake.game.py               # Classic snake game
├── train_status.py             # Train status checker
├── college.libraby.system.py   # Library management
├── main.sorten.py              # URL shortener
├── requirements.txt            # Project dependencies
├── README.md                   # This file
├── recent_searches.json        # Weather app data
└── __pycache__/               # Python cache directory
```

## 🎯 Learning Objectives

By exploring these projects, you'll learn:

1. **Python Fundamentals** - Variables, loops, functions, classes
2. **File I/O** - Reading and writing files
3. **API Integration** - Working with REST APIs
4. **GUI Development** - Creating desktop applications
5. **Game Development** - Basic game mechanics
6. **Error Handling** - Exception management
7. **Data Structures** - Lists, dictionaries, sets
8. **Object-Oriented Programming** - Classes and objects
9. **Third-party Libraries** - Using external packages
10. **Best Practices** - Code organization and documentation

## 🚀 Getting Started with Each Project

### For Beginners
Start with these projects:
1. `number_guess.py` - Simple game logic
2. `snake.game.py` - Basic game development
3. `alarm.py` - Simple utility with timing

### For Intermediate Users
Try these projects:
1. `ATM_simulation.py` - Complex state management
2. `weather_professional.py` - API integration with GUI

### For Advanced Users
Challenge yourself with:
1. `college.libraby.system.py` - Database management
2. `main.sorten.py` - Web service development

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Bug Reports

If you find a bug, please create an issue with:
- A clear and descriptive title
- Steps to reproduce the problem
- Expected vs actual behavior
- Python version and operating system

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Shivam Kumar** - Initial work - [GitHub Profile](https://github.com/shivamkumar)

## 🙏 Acknowledgments

- Python community for excellent documentation
- Open-Meteo for free weather API
- CustomTkinter team for modern GUI framework
- All contributors who helped improve these projects

## 📞 Contact

For questions or suggestions, feel free to reach out:
- Email: deepkumar14379@gmail.com
- GitHub Issues: [Create an issue](https://github.com/shivamkumar/python-projects/issues)

---

**Happy Coding!** 🎉  
*Start with any project that interests you and happy learning!*
