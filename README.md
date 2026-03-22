# Health-Tracker-App-using-Flask
A simple, interactive web application built with Python and Flask to log, track, and visualize daily health metrics including exercise, meditation, and sleep using Chart.js.
Here is a short repository description and a comprehensive `README.md` file based on the files you uploaded for your Flask Health Tracker application.

### GitHub Repository Description

**Short Description (for the "About" section):**

simple, interactive web application built with Python and Flask to log, track, and visualize daily health metrics including exercise, meditation, and sleep using Chart.js.

# Health Tracker Dashboard 🧘‍♂️🏃‍♀️💤

A simple and intuitive web application built with Python and Flask that allows users to track their daily health habits. Log your exercise, meditation, and sleep hours, and visualize your progress over time through an interactive dashboard powered by Chart.js.

## ✨ Features

* **Data Logging**: Easy-to-use forms with validation to input daily metrics:
    * Exercise (in minutes)
    * Meditation (in minutes)
    * Sleep (in hours)
* **Interactive Dashboard**: Visualizes your logged health data over time using dynamic bar and line charts.
* **Responsive Design**: Built with Bootstrap 4, ensuring the app looks great on both desktop and mobile devices.
* **Database Integration**: Uses SQLAlchemy (SQLite by default, easily configurable to PostgreSQL) to securely store your health records.

## 🛠️ Technologies Used

* **Backend**: Python, Flask
* **Database**: Flask-SQLAlchemy (SQLite / PostgreSQL)
* **Forms & Validation**: Flask-WTF, WTForms
* **Frontend**: HTML5, CSS3, Bootstrap 4
* **Data Visualization**: Chart.js

## 📁 Project Structure

```text
├── app.py               # Main Flask application and database models
├── forms.py             # WTForms form definitions and validators
├── static/              
│   └── css/
│       └── style.css    # Custom CSS styling
└── templates/           # HTML templates
    ├── base.html        # Base layout with Bootstrap and navbar
    ├── index.html       # Landing page
    ├── form.html        # Data entry form
    ├── dashboard.html   # Charts and data visualization
    └── ...              # Other utility templates (success, users, etc.)
````

## 🚀 Installation and Setup

Follow these steps to get the project running on your local machine.

### Prerequisites

  * Python 3.7+ installed
  * `pip` (Python package installer)
## 💡 Usage

1.  **Home Page**: Navigate to the home page to read a brief introduction.
2.  **Enter Health Data**: Click on "Enter Health Data" in the navigation bar. Pick a date and enter your exercise minutes, meditation minutes, and sleep hours. Submit the form.
3.  **Dashboard**: Head over to the "Dashboard" to see your newly logged data dynamically plotted on the interactive charts.


### Next Steps for your Repo:
1. Don't forget to replace `yourusername` in the clone URL with your actual GitHub username.
2. It is highly recommended to create a `requirements.txt` file in your project folder so others can easily install the dependencies. You can generate it by running `pip freeze > requirements.txt` in your terminal while your virtual environment is active. Add this file to your repository as well!
```
