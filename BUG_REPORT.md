Bug Tracking

Django:

- Not correctly displaying GPU data from database.
  - Wrong configuration for mapping URL path to views.
- Forms unable to submit data about subscribers to the database.
  - Information is being stored incorrectly in the model that does not respond correct POST error code
- Subscription Form not rendering GPUs in correct format
  - Entry method of GPU corrupted which would affect how HTML is populating (Result of poorly formatted data that modifies HTML rendering process)
  - Subscription objects not created due to subscriber and GPU field mismatch in database
- GPU alias mismatch in database (ask Milan to clarify what alias represents)
  - Getter methods for GPU fields doesn&#39;t return correct fields
  - Need to add testing for field assignment to catch errors in database update process
  - Maximum length of URLField and CharField reached which requires resetting of field initialization
- Duplicate entries of subscribers in database which case incorrect subscription rendered to user view page
  - Check if user created duplicate account and use hashing key to encode unique identifier for user accounts
  - Allow users to be differentiated not only based off username/password combination
- Data overload causing stale page with non-functioning subscription form
  - Need to check if form request is being processed in the backend database correctly. Throws exception that handles and provide user context to blank form (currently being shown)

Notifier:

- Message being sent out incorrectly.
  - Notification message should not be sent out when the GPU is out of stock.
  - Check if all conditions are evaluated as expected. Need to update what&#39;s being returned (should be &quot;Null&quot;) when GPU is out of stock.
- Incorrect formatting error when attempting to send email.
  - Fails to send the message due to invalid formatting.
  - Should be a base64url encoded email object.
  - Expecting the message to be created in the correct format, then sent to the user.
- Unable to use testing credentials.
  - Structure of the method that sends texts assumes use of live credentials, which actually sends a text to a verified user.
  - Need to be able to pass in sender number, which either goes with the live credentials or testing credentials.

- Issue with credentials since Twilio tokens keep recycling.
  - Running tests for the texting notifier fails due to invalid credentials.
  - Need to be updated to be able to set up the client and send texts.
  - Expecting tests to run and show results.

Scraper:

- BeautifulSoup not recognized by the system
  - Scraper throws errors on BeautifulSoup related lines despite being imported at the top of the page.
  - Need to check if BeautifulSoup was properly installed on the machine
- BeautifulSoup on BestBuy scraper Add to Cart button returns the wrong in stock status
  - Scraper looks for add to cart button that has the following text: &quot;Sold out&quot; and has the add to cart button be unclickable
  - If the text says sold out, the method returns false as it means the item is not in stock
  - It turned out the add to cart button unclickable button can also say &quot;Coming Soon&quot; when its not in stock
  - When it said those things, the scraper would return true as &quot;Coming Soon&quot; was not equal to &quot;Sold Out&quot; and thus the program would return that the item was in stock when it was not
- BeautifulSoup on BestBuy scraper Add to Cart button returns the wrong in stock status (again)
  - Scraper looks for add to cart button that has the following text: &quot;Sold out&quot; and has the add to cart button be unclickable
  - If the text says sold out, the method returns false as it means the item is not in stock
  - It turned out the add to cart button unclickable button can also say &quot;Unavailable Nearby&quot; in addition to &quot;Coming Soon&quot; when its not in stock
  - When it said those things, the scraper would return true as &quot;Unavailable Nearby&quot; was not equal to &quot;Sold Out&quot; and thus the program would return that the item was in stock when it was not
- BeautifulSoup on BestBuy scrapes against page with no Add to Cart button
  - When a Best Buy webpage does not have an Add to Cart button the scraper doesn&#39;t work as it doesn&#39;t find the proper html tags to check against
  - The code assumes that the html tag can be found every time but in this case it can&#39;t and when code is ran against it an error is returned
  - This seems to be the case when an item is never set to return on the site ever
- Best Buy pages were listed as invalid when request were ran on despite being fully functional on the web
  - Current web requests do not go through and we can&#39;t get necessary info
  - Further research into the matter it seems like we need to add headers in order to access the page
- Selenium on BestBuy scraper Add to Cart button returns the wrong in stock status
  - Scraper looks for add to cart button that has the following text: &quot;Sold out&quot; and has the add to cart button be unclickable
  - If the text says sold out, the method returns false as it means the item is not in stock
  - It turned out the add to cart button unclickable button can also say &quot;Coming Soon&quot; and &quot;Unavailable Nearby&quot; when its not in stock
  - When it said those things, the scraper would return true as &quot;Coming Soon&quot; was not equal to &quot;Sold Out&quot; and thus the program would return that the item was in stock when it was not
