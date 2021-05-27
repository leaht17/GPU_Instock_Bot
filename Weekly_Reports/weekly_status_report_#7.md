**GPU Instock Bot Weekly Summary #7**

**Team Report**

- **Last Week&#39;s Goals**
  - Verify that the steps for building on Windows are accurate.
  - Work towards Dockerizing the build.
  - Unsubscribe button functionality working.
- **Progress and Issues**
  - Continued working on Dockerizing the build.
  - Cleaning up frontend code and interface.
- **Plans and Goals**
  - Fix any pending issues with building and running the program.
  - Finish refactoring and cleaning up the code.

**Contributions**

- **Last Week&#39;s Goals**
  - Milan will continue work on the interface, focusing on providing informative messages to the user.
  - Derek and Andy will be taking steps towards Dockerizing the program
- **Progress and Issues**
  - Andy and Derek worked on Dockerizing the program.
    - Cannot dockerize backend due to the problem of authenticating our Gmail account in the user flow (which needs to be done manually). Dockerizing our backend service didn&#39;t allow for us to be able to pop open the web browser to manually verify the access to our gmail account. The alternative was to find a way to avoid this manual authentication by having it automatically go through (navigating around the Oauth2.0), but _because we are not paying for a Gsuite account_ for higher level permissions to be able to use a service account with those permissions, we ultimately decided to keep the old method of just running the python file and having the user verify the account themselves.
    - A similar issue with using free level accounts, Twilio won&#39;t let us send notifications to phone numbers that have not been manually verified (this was mentioned before in our beta release) and we are going to keep it this way because we don&#39;t have funds from this class to support that feature either.
    - Ultimately led to the decision to avoid dockerizing the front end alone since the backend won&#39;t be dockerized. (The app is still meant to be run on a server though).
  - Derek and Andy worked on creating a config file for initializing the database settings and also for easy placement of the Twilio authorization values.
  - Milan added functionality so users could subscribe with either phone or email, not requiring both fields, and integrated informational messages displayed to the user on certain actions.
  - Milan worked on figuring out how to add filters for the GPU list in the UI, but this is a stretch goal so it may not be completed in time.
  - Leah, Liz, and David worked on refactoring and cleaning up the code.
- **Plans and Goals**
  - Derek will work on editing the scraper to utilize the new config file.
  - Milan will continue work on getting sorting functionality added to the front end user interface.
  - David, Leah, and Liz will work on preparing our final presentation
  - Elizabeth will continue refactoring and cleaning up necessary code / documentation and help Milan with sorting functionality.
