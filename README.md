# ChatScraper

ChatScraper is a web application that allows users to manage and save ChatGPT conversations. This application provides features for scraping conversation data from ChatGPT links and processing the text for further use.

## Features

- **Registration and Login**: Users can register and log in to the application.
- **Submit ChatGPT Link**: Users can enter a ChatGPT conversation link to save.
- **Data Scraping**: The application will scrape data from the provided link.
- **Text Preprocessing**: Conversation text will be processed to remove punctuation, numbers, and excessive spaces.
- **Conversation History**: Users can view saved conversation history.
- **Conversation Details**: Users can view details of processed conversations.
- **Export to CSV**: Users also can export the processed conversations into a csv file.

## Demonstration
[Demo Link](https://drive.google.com/file/d/1bpjwQ4yAxkXqSokcM4bS9xZr7OEAndK3/view?usp=drive_link)

## Installation

1. Clone this repository:

    ```sh
    git clone https://github.com/JasonSlav/scrape-gpt.git
    cd scrape-gpt
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # For Unix/macOS users
    venv\Scripts\activate     # For Windows users
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file based on `.env.example` and fill it with the appropriate configuration:

    ```sh
    cp .env.example .env
    ```

5. Run the database migration:

    ```sh
    flask db upgrade
    ```

6. Run the application:

    ```sh
    flask run
    ```

## Project Structure


```
.
├── .env
├── .env.example
├── .gitignore
├── app.py
├── config.py
├── index.html
├── models/
│   ├── __init__.py
│   ├── conversation.py
│   ├── user.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── scrape.py
├── scraper/
│   ├── preprocess.py
│   ├── scraper.py
├── static/
│   ├── flash.css
│   ├── index.js
│   ├── navbar.js
│   ├── script.js
│   ├── style.css
├── templates/
│   ├── chat.html
│   ├── history.html
│   ├── home.html
│   ├── index.html
│   ├── navbar.html
│   ├── preprocess.html
└── requirements.txt
```


## Usage

1. Open your browser and access `http://localhost:5000`.
2. Register a new account or log in with an existing account.
3. Enter a ChatGPT conversation link on the main page and click "Submit Link".
4. Click "Chat Description Name" on the left to view details of the processed conversation.
5. View history and details of preprocessed text on the "History" page.

## Contribution

If you would like to contribute to this project, please fork this repository and create a pull request with your proposed changes.

## License

This project is open source and licensed under the terms described in the [LICENSE](LICENSE) file.
