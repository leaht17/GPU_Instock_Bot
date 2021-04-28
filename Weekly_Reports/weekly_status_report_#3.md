**GPU Instock Bot Weekly Summary #3**

**Team Report**

- **Last Week&#39;s Goals**
  - One newegg GPU scraper will be finished tonight by Derek. Another Best Buy scraper will be finished by David within the next couple days. This will allow Andy, Derek and David to start working on getting the scrapers onto AWS virtual servers by next Tuesday.
  - Liz, Milan and Leah will also meet to discuss the GUI for the website, and Liz and Milan will work on implementing a frontend with functional forms and buttons that are ready to start sending information to the backend AWS servers.
- **Progress and Issues**
  - Discussed the UI design: Considering a pop up for the subscribe notifications after selecting the GPU models where the user can type in email and/or phone number, or a single-page form that allows users to select GPU models and subscribe for notifications through email and/or text.
  - Due to costs, we discussed changing the backend system from AWS to something else, like a local backend where data is stored locally.
    - Discussed the possibility of using Docker and decided not to deal with hosting, as none of us have much experience with it.
    - Decided that having the web app run locally will eliminate costs associated with the project so we can focus on implementing the actual functionality of the app.
  - Clarified our plans for how the data will be stored, what sort of data will be stored, and how that interacts with the rest of the architecture.
  - Moved away from using API&#39;s to scrape Best Buy and instead will be using BeautifulSoup to perform that task.
- **Plans and Goals**
  - The front-end team will move towards getting a functional prototype of the website going
  - The backend team will be split between two things:
    - Learning about how Django will interface with the backend &amp; moving towards back end modules interfacing with front end
    - Building a notification python module that will be used to send email notifications and text notifications
  - Thinking up unit tests for when we move on to the testing phase

**Contributions**

- **Last Week&#39;s Goals**
  - Leah will continue working on the frontend wireframe and share the design with Milan and Liz to start implementing the GUI.
  - Andy will finish and go over backend design Thursday. Setting up AWS instances as the design gets closer to being finalized.
  - Milan and Liz will continue working with the Django frontend, focusing on implementing user interface based on Leah&#39;s wireframe.
  - David will continue working on setting up the scraper for GPU&#39;s in Best Buy, finding alternatives to the current web request with API key method that does not work. Find ways to print out stock status for each GPU.
  - Derek is working on finishing the newegg scraper and will work together with Andy and David on getting the scrapers working on AWS Lambda virtual servers.
- **Progress and Issues**
  - Liz, Leah, and Milan met on Thursday to discuss the wireframe, edit the design, and clarify what pages and features are needed.
  - Liz and Milan began setting up the frontend GUI.
  - Instead of AWS, Derek, Andy, and David are looked into using a local backend. They met up on Friday and Monday to discuss further implementation details for the back end.
  - Andy is getting familiarized and testing with Gmail API
  - David got the Best Buy scraper to work using BeautifulSoup instead of API&#39;s. Currently, it simply prints out the availability of a GPU.
- **Plans and Goals**
  - Andy will look into the possibility of getting the program to work with multiple users without having to host the site. Working on using Gmail API for notifier module. Looking into SMTP as an alternative if Gmail API takes too long.
  - Derek, Andy and David will continue working on finishing and implementing back end modules
  - Milan and Liz will continue implementing the frontend with any edits on the design of the UI from Leah.
  - Derek will look into figuring out how the Django front end and back end will interface together
  - Leah will start figuring different test cases that we need to account for once we start setting up testing.
