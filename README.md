# 📞 Phonebook Application

A simple, interactive phonebook application built with Python and Streamlit. It allows users to manage contacts through a clean web-based user interface. The backend is powered by SQLite for persistent data storage.

***

## ✨ Features

- **Add Contacts**: Easily add new contacts with a first name, last name, and phone number.
- **View All Contacts**: Display a complete list of all saved contacts in a clean format.
- **Search Contacts**: Quickly find a specific contact by searching for their first name.
- **Interactive UI**: A user-friendly interface built with Streamlit for seamless navigation.

***

## 🛠️ Technologies Used

- **Python**: The core programming language.
- **Streamlit**: For creating the interactive web application UI.
- **SQLite**: For the relational database to store contact information.

***

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment:**
    - **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    Install all dependencies from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    Execute the following command in your terminal. Streamlit will start a local server and open the application in your web browser.
    ```bash
    streamlit run app.py
    ```
    The application will be available at `http://localhost:8501`.

***

## Usage

Once the application is running, you can use the main menu buttons to navigate:
- **Add Phone Number**: Opens a form to enter and save a new contact.
- **View Phone Numbers**: Displays all contacts currently stored in the database.
- **Search Phone Numbers**: Provides a search bar to look up a contact by their first name.

The database file `PhoneBook.db` will be automatically created in the project directory on the first run.

***

## Contributing

Contributions are welcome! If you have ideas for improvements or find any bugs, please feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request
