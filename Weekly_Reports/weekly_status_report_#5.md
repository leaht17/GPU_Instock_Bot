**GPU Instock Bot Weekly Summary #5**

**Team Report**

- **Last Week&#39;s Goals**
  - Complete first version of the web app with functioning UI and database.
- **Progress and Issues**
  - Due to time restraints, communication issues, and being held back due to other tasks being unfinished, progress had been stalled regarding integrating everything together and getting testing/CI in place for the previous assignment.
  - API credentials are exposed on the public GitHub repo, so our tokens keep being recycled and need to be updated manually often.
  - All team members worked towards getting a minimal viable product for the beta release and are contributing to documentation for the parts they have been working on.
  - All team members contributed to and participated in the presentation for beta.
- **Plans and Goals**
  - Polish up the prototype of the web app with functioning UI, backend, and tests.
  - Work towards getting the app to work on Windows systems.
  - Fix remaining bugs and issues.
  - Clean up the documentation.
    - Documentation for developers
    - Documentation for users (to host locally) as current documentation needs work across different operating systems.

**Contributions**

- **Last Week&#39;s Goals**
  - Milan and Liz will polish the UI and work on getting email and phone number forms linked to the database.
  - Andy will finish creating an abstract Notification module to be used with the Django backend
  - David will look into testing for scrapers and learning how to mock web pages to test on
  - Derek is finalizing integrating GPU stock info into the database and also is finishing up getting the stock scrapers to be able to interface with Django.
  - Leah will start setting up the testing framework using unittest.
- **Progress and Issues**
  - Milan, Liz, and Andy refined the UI and developed a functional form for subscribers to fill out.
  - Andy, Derek, and Milan worked on the functionality of the backend and PostgreSQL database for the beta release.
  - Derek created the setup script and Milan and Andy contributed to writing installation/setup documentation.
  - David and Milan set up the testing CI.
  - Leah, David, and Milan/Liz wrote tests for the notifiers, scrapers, and Django framework.
  - Leah drafted the reflection slides for the reflection presentation.
  - Derek edited that awesome project video demo that you are watching for the beta version submission
  - Andy worked on creating a new frontend using bootstrap. Also worked on incorporating PostgreSQL database as an alternative to sqlite3 due to foreseen issues with the finalized version.
- **Plans and Goals**
  - Leah, David, and Liz will work on finishing up writing tests for notifiers, scrapers, and Django.
  - Milan and Liz will work on developing a functional unsubscribe option for the UI and figure out how to allow a user to subscribe to a single notification method i.e. email OR phone rather than email AND phone.
  - Derek will be working to ensure a smooth automated build for Mac &amp; (resentfully) Windows systems. He will also be working on documenting and refactoring the current code. These plans will be further refined and solidified during the Thursday group meeting
  - Andy plans on working on containerizing the components of our system in order to host them on the cloud (AWS) so that others can access it.
