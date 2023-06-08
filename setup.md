To Start the program:

1.) install dependencies mentioned in requirements.txt to run the project by running "pip install -r requirements.txt
". If not working install requirements from requirements.txt manually.

    Best practice is to make a virtual environment of your own and install dependencies mentioned in requirements.txt file there. Steps to do so are mentioned below
(source: chatGPT)
Clone the repository: First, clone the GitHub repository to your local machine using the git clone command. Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Then run the following command:

Copy code
git clone <repository_url>
Replace <repository_url> with the URL of the GitHub repository you want to clone.

Create a virtual environment: It's a good practice to create a virtual environment to isolate the project's dependencies. Navigate to the cloned repository's directory and run the following commands:

On Windows:

Copy code
python -m venv venv
venv\Scripts\activate
On macOS/Linux:

Copy code
python3 -m venv venv
source venv/bin/activate
This will create a virtual environment named "venv" and activate it.

Install dependencies: Once you have activated the virtual environment, you need to install the project's dependencies. Typically, the dependencies are listed in a requirements.txt file. Navigate to the cloned repository's directory and run the following command:

Copy code
pip install -r requirements.txt
This command will install all the required packages listed in the requirements.txt file.

Run the project: After installing the dependencies, you can now run the project. Depending on the project, there might be different ways to run it. Look for a file like main.py or run.py that serves as the entry point to the project. In your terminal or command prompt, run the appropriate command to start the project:

Copy code
python main.py
Replace main.py with the actual file name if it's different in your project


2.)Run the main.py file