# Care for Your Own - Personal Assistant

This personal assistant application helps you with daily tasks, scheduling, and information access using natural language. It understands your requests and provides personalized responses.

## Getting Started

Here's how to download and use the "Care for Your Own" personal assistant:

1.  **Download the application:**

    *   **Easiest way (if available):** Go to the "Releases" page on GitHub ([https://github.com/Jobeer1/Care-for-your-own/releases](https://github.com/Jobeer1/Care-for-your-own/releases)).  If there's a pre-built version (like an `.exe` file), download it. This is the simplest option.

    *   **If no pre-built version:** If there are no releases, you'll need to download the code directly. Click the green "Code" button on the main repository page ([https://github.com/Jobeer1/Care-for-your-own](https://github.com/Jobeer1/Care-for-your-own)). Then, click "Download ZIP".

2.  **Install (if you downloaded the code):**

    *   If you downloaded a pre-built version, you can skip this step.

    *   If you downloaded the code as a ZIP file, extract the ZIP file to a folder on your computer.

    *   **Important:** This application needs Python.  If you don't have Python, download it from [https://www.python.org/downloads/](https://www.python.org/downloads/). Install Python.

    *   Open the folder where you extracted the code.

    *   Open a "Command Prompt" (on Windows) or "Terminal" (on Mac/Linux).

    *   In the command prompt or terminal, navigate to the folder where you extracted the code. You can do this by typing `cd` followed by the path to the folder. For example: `cd C:\Users\YourName\Downloads\Care-for-your-own`.

    *   Type `pip install -r requirements.txt` and press Enter. This will install all the necessary components. If you don't have `requirements.txt` file, type the following instead: `pip install flask azure-cognitiveservices-speech google-generativeai python-dotenv`

3.  **Get API Keys (Important!):**

    This application uses API keys to work.  You'll need to get your own keys from the following services:

    *   **Gemini API Key:** You'll need to sign up for a Google Cloud account and enable the Gemini API. You can find instructions on how to do this in the Gemini documentation.

    *   **Azure Cognitive Services API Keys:** You'll need to create an Azure account and subscribe to the Azure Cognitive Services for Speech. You can find instructions on how to do this in the Azure documentation.

4.  **Configuration (Setting up the keys):**

    *   Find the file named `config.ini.example` in the application folder.

    *   Make a copy of this file and rename the copy to `config.ini`.  (Right-click on the file, select "Copy," then right-click in the same folder and select "Paste". Then, right-click on the new file and select "Rename.")

    *   Open the `config.ini` file in a text editor (like Notepad).

    *   Inside the `config.ini` file, you'll see places to enter your API keys.  Paste the Gemini API key where it says `GEMINI_API_KEY =`, and the Azure keys where it says `AZURE_SUBSCRIPTION_KEY =` and `AZURE_REGION =`.

    *   Save the `config.ini` file.

5.  **Run the application:**

    *   **If you downloaded a pre-built version:** Double-click the `.exe` file to run the application.

    *   **If you downloaded the code:** Open the command prompt or terminal, go to the application folder, and type `python app.py` and press Enter.

6.  **Using the application:**

    Describe how to use your application.  For example:

    *   "Type your requests in the command prompt or terminal."
    *   "The application will respond with text and/or speech."

## Troubleshooting

If you have any problems, please check the following:

*   Make sure you have installed all the required components.
*   Make sure you have entered the API keys correctly in the `config.ini` file.
*   Check the application's output in the command prompt or terminal for any error messages.

If you still have problems, you can create an "Issue" on GitHub (go to the "Issues" tab on the repository page) to ask for help.

## Contact

ysterjobeer@gmail.com 
