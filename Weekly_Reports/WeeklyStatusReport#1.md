#GPU Instock Bot Weekly Summary #1

##**Team Report**
- ###**Last Week's Goals** 
    - N/A as this is the first summary
- ###**Progress & Issues**
    - Researched and defined  use cases for notifying users about their stocks s.a. adding or removing a tracked product.
    - Researched and defined use cases for pushing text or email notifications
        - AWS SNS backend will drive the notification pushing services.
    - Outlined functionality and how users will be able to interact with the service in order to toggle push notifications or remove themselves from the platform.
    - Differentiated team roles by spreading out specifics and general responsibilities.
    - Clarified the minimum viable product to mitigate potential challenges that could arise from costs of implementing text services and costs of virtual hardware overhead of having to scrape retailers & resellers.
        - BestBuy Stock Bot will utilize the BestBuy API and a web interface that allows user to select which model of GPU user wants to track and subscribe for email notifications.
        - The available models would be based on the skus from the BestBuy website
    - Discussed and defined external requirements within the assignment doc.
    - Planned out the schedule for each of the team roles.
    - Only troubles were time taken to finish the meeting and schedule conflicts that arose as a result.
        - Solution: Team will have to collaboratively develop different/separate meeting times via When2Meet/Slack Poll.
- ###**Plans & Goals**
    - Finalize wireframe and start implementing front-end (research frameworks to use).
    - Create a diagram for how scraped data will flow into AWS and the user interface to understand the data cycle and user interaction (backend and frontend diagrams).
    - Thursday meeting we will discuss meeting times for the following Tuesday and other possible meeting times.

##**Contributions**
- ###**Last Week's Goals** 
    - N/A as this is the first summary
- ###**Progress & Issues**
    - All team members discussed and contributed to the requirements and policies document, including minimal viable product, use cases and role responsibilities.
    - Andy contributed ideas for the functionality of the product and divided up the schedule for each subgroup.
    - Elizabeth worked on updating README with team progress and meeting notes.
    - David gave ideas about user interaction and suggestions to improve user experience.
    - Leah outlined the README, outlined more use cases in the Project overview document, and included notes for Team Report and Progress.
    - Milan made progress on updating README, defining External Requirements in the Project Overview document, and clarifying the responsibilities of his role on the front-end.
    - Derek created the README document and assigned deadlines for teams and scheduled out upcoming team meetings in addition to clarifying project specifications.
    - Milan & Liz foresee understanding and familiarizing themselves w/ Django as a potential challenge for the front end.
- ###Plans & Goals 
    - The following rough drafts will be due Tuesday, April 20th
    - Leah & Derek develop front end wireframe (go over this as a group on Thursday in addition to solo development)
    - Derek will code the Best Buy stock check using the API
    - Andy develop high level back-end architecture overview
    - Milan & Liz will figure out Django and get basic non-functional signup page
    - David will look into scraping retailers for GPU stock