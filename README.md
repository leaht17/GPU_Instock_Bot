# GPU_Instock_Bot

# Description
GPUs are in high demand which makes them difficult to come by. Desirable GPUs are often sold out online almost as soon as they become available. As such, those seeking to purchase GPUs must act quickly once they come in stock. The GPU InStock Bot solves this problem by notifying users when GPUs come in stock on various online retailers and resellers. 

Target Audience:
Work professionals needing a card for simulations, machine learning, etc.
Gamers of all ages needing hobbies/entertainment in stay at home age 
Cryptocurrency miners looking to cash in on the current boom

Users will interface with the GPU InStock Bot through a simple web app where they can subscribe for notifications. The web app will allow users to choose which model of GPU they would like notifications for and opt-in to email notifications. The UI will be a single-page design where all the information is available at a glance.

The GPU InStock Bot will then periodically scrape the web to look for GPUs in stock. Whenever it finds new GPUs in stock, it will notify all the users who are interested in the GPU. The bot will check the following sites for GPU availability: BestBuy, Newegg

# Repository Layout
- The src folder contains the Django project components
    - The GPUInStockBotMain contains the core components of the Django webserver
        - urls.py defines the URL declarations for the project; a “table of contents” of the site.
        - settings.py defines the settings/configuration for the project.
        - asgi.py is an entry-point for ASGI-compatible web servers to serve the project
        - wsgi.py is an entry-point for WSGI-compatible web servers to serve the project The media folder contains any media files that are utilized by the site 
      
    - The static folder contains any static files that are utilized by the site such as stylesheets 
      
    - The templates folder contains any html files that will be utilized by the site 
      
    - The profiles folder stores a Django app; a logical sub-component of the webserver. This app will be used for storing user email information.
        - admin.py registers models with the site
        - apps.py defines the configuration of the app
        - models.py defines structural and logical components of the app
        - tests.py defines the unit tests for the app
        - urls.py defines the URL declarations for the app
        - views.py defines the webpage renderings that will be utilized by the app
    - manage.py drives the Django webserver's operation and allows the developer to interact with the service
   
- The Weekly_Reports folder contains a separate markdown document for each weekly summary.

- The GPU_Scrapers folder is where the .py files for each separate website specific GPU stock webscraper is stored. Newegg, Best Buy, etc.

- The requirements.txt file will contain our Python dependencies


# Installation Process:
## Mac Process:
1. Clone the respository
2. Open the terminal and change to the root directory of this github repo
3. Install virtualenv using the 'pip install virtualenv'
4. Run the command 'chmod u+x setup.sh' within the terminal
5. Run the command ./setupMac.sh


## Windows Process:
1. Buy a Mac
2. Refer to Mac Installation Process

# Mac user instructions:
1. Start the postgresql app. The setup script should have created a database with its credentials.
2. Start the Django app by going to the gpu_instock_bot_v2_src directory and running the command "python manage.py runserver". This will run the django server on default localhost:8000
3. To view the database using the Django interface, go to localhost:8000/admin to explore our database.
4. Now that the front end and database is working, you can now run the script by going back to the main directory, going into "scrapequerynotifiermicroservice" and running the command "python scrape_query_notify.py" to run the backend service.
5. Please use Python 3.5+ to run our service. 
6. Keep in mind, when testing this service out, the API token for twilio will be expired due to having exposed API keys resulting in a short lifecycle for our authentication tokens. PLEASE reach out via slack and I can reupload a new API token that will be live for about half a day.
7. Additionally, when first using our backend service on a new system, the Gmail API will go through authentication where it will need approval to send emails from our email. Please contact me via slack for our email credentials so that you can approve yourself (this is a email we made, so theres nothing really private on it and it was made just for this assignment)
