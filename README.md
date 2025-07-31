📞 Phonebook Application
A simple, interactive phonebook application built with Python and Streamlit. It allows users to manage contacts through a clean web-based user interface. The backend is powered by SQLite for persistent data storage.

✨ Features
Add Contacts: Easily add new contacts with a first name, last name, and phone number.

View All Contacts: Display a complete list of all saved contacts in a clean format.

Search Contacts: Quickly find a specific contact by searching for their first name.

Interactive UI: A user-friendly interface built with Streamlit for seamless navigation.

🛠️ Technologies Used
Python: The core programming language.

Streamlit: For creating the interactive web application UI.

SQLite: For the relational database to store contact information.

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites

Make sure you have Python 3.8+ installed on your system.

Installation & Setup

Clone the repository:

Bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Create and activate a virtual environment:

Windows:

Bash
python -m venv venv
.\venv\Scripts\activate
macOS / Linux:

Bash
python3 -m venv venv
source venv/bin/activate
Install the required packages:
The only external dependency for this project is Streamlit.

Bash
pip install streamlit
Run the application:
Execute the following command in your terminal. Streamlit will start a local server and open the application in your web browser.

Bash
streamlit run app.py
The application will be available at http://localhost:8501.

Usage
Once the application is running, you can use the main menu buttons to navigate:

Add Phone Number: Opens a form to enter and save a new contact.

View Phone Numbers: Displays all contacts currently stored in the database.

Search Phone Numbers: Provides a search bar to look up a contact by their first name.

The database file PhoneBook.db will be automatically created in the project directory on the first run.

Contributing
Contributions are welcome! If you have ideas for improvements or find any bugs, please feel free to open an issue or submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request
