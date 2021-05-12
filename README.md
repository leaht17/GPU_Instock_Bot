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
1. Clone the respository
