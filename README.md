🎮 Game Recommender System
Welcome to the Game Recommender System! This is a simple web application built with Streamlit that helps you discover new games based on your preferences. Just pick a game you like, and it will suggest similar ones.

✨ Features
Game Recommendations: Get a list of games similar to your chosen title.

Live Game Posters: See the official poster for each recommended game directly from the RAWG API.

🚀 How It Works
This recommender system uses a smart approach to give you fast suggestions:

Smart Recommendations: We've already done the heavy lifting! Instead of calculating similarities on the fly, the app uses a pre-calculated "slice" of game similarities (a small 9 MB file!). This means recommendations appear almost instantly.

Dynamic Posters: When you ask for recommendations, the app reaches out to the RAWG API in real-time to grab the latest posters for the suggested games.

🛠️ Setup and Run
Follow these simple steps to get the Game Recommender running on your computer:

1. Prerequisites
Make sure you have:

Python 3.x installed on your computer.

Git installed (for cloning the project).

2. Get Your RAWG API Key
You'll need a free API key from RAWG to fetch game posters:

Go to the RAWG Developer Portal.

Sign up or log in.

Generate your API key. Keep this key safe and private!

3. Clone the Project
Open your terminal or command prompt and run:

git clone https://github.com/tousifT5/Game_Recommender.git
cd Game_Recommender


4. Set Up a Virtual Environment (Recommended)
It's good practice to create a virtual environment to keep your project's dependencies separate:

python -m venv venv
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

5. Install Dependencies
With your virtual environment activated, install all the necessary libraries:

pip install -r requirements.txt

6. Secure Your API Key
This is very important for security!

Create a new folder named .streamlit in the root of your project directory (where app.py is).

Inside the .streamlit folder, create a new file named secrets.toml.

Open secrets.toml and add your RAWG API key like this:

# .streamlit/secrets.toml
RAWG_API_KEY = "YOUR_ACTUAL_RAWG_API_KEY_HERE"

Make sure to replace "YOUR_ACTUAL_RAWG_API_KEY_HERE" with the key you got from RAWG.

Do NOT commit secrets.toml to GitHub! Your .gitignore file should already be set up to ignore this file.

7. Run the App
Finally, run your Streamlit application:

streamlit run app.py

Your web browser should automatically open a new tab with the Game Recommender System!

📂 Project Files
Here are the main files in this project:

app.py: The core Streamlit application code.

game_data.csv: Your dataset containing game titles and other relevant information.

sliced_similarity.npy: The small, pre-calculated file that powers the fast recommendations.

requirements.txt: Lists all the Python libraries needed for the app to run.

.streamlit/secrets.toml: (Hidden) Stores your API key securely.

.gitignore: Tells Git which files to ignore (like your API key).

⚠️ Important Notes
API Key Security: Your RAWG API key is sensitive. The .streamlit/secrets.toml method keeps it out of your public GitHub repository. When deploying to platforms like Streamlit Community Cloud, you'll add this secret directly in their settings.

Poster Loading Time: Since game posters are fetched live from the RAWG API, there might be a slight delay when recommendations first appear, depending on your internet connection and the API's response time.