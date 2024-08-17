# Restaurant Name Generator

This is a Streamlit app that generates restaurant names and menu items based on selected cuisines using Langchain and OpenAI.

## Setup and Installation

Follow these steps to set up and run the Restaurant Name Generator:

1. **Clone the repository**

2. **Create a virtual environment**

It's recommended to use a virtual environment to avoid conflicts with other Python projects.

For Windows:
python -m venv venv
venv\Scripts\activate


For macOS and Linux:
python3 -m venv venv
source venv/bin/activate

3. **Install the requirements**
pip install -r requirements.txt

4. **Set up environment variables**

Create a `.env` file in the root directory of the project and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here

Replace `your_openai_api_key_here` with your actual OpenAI API key.

5. **Run the Streamlit app**
streamlit run app.py




This command will start the Streamlit server and should automatically open the app in your default web browser. If it doesn't, you can manually open the URL displayed in the terminal.

## Usage

Once the app is running:

1. Select a cuisine from the dropdown menu in the sidebar.
2. The app will generate a restaurant name and a menu with 10 items, each with its ingredients.
3. The restaurant name will be displayed as a header, followed by the menu items.
4. Each menu item will show its name in bold, with ingredients listed below in green text.

## Requirements

The main requirements for this project are:
- Python 3.7+
- Streamlit
- Langchain
- OpenAI

For a full list of requirements, see the `requirements.txt` file.

## Troubleshooting

If you encounter any issues:
- Ensure that your OpenAI API key is correctly set in the `.env` file.
- Check that all requirements are installed correctly.
- Make sure you're using a compatible Python version.

For any other problems, please open an issue in the GitHub repository.
