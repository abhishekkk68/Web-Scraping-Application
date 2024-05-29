Web Scraping Application

This project is a web scraping application built using Python, Flask, BeautifulSoup, and pandas. It provides a user-friendly web interface for scraping data from websites and storing it in an Excel file.

Features

	User-friendly Interface: The application provides a simple and intuitive interface for users to input the website URL and 	initiate the scraping process.

	Comprehensive Scraping: The web scraper extracts various elements from the webpage, including titles, headings, paragraphs, images, and links.

	Excel Export: The scraped data is stored in an Excel file, making it easy to analyze and manipulate.
	Responsive Design: The frontend is designed using Bootstrap, ensuring compatibility with various screen sizes and devices.

Usage

	Run the Flask application
	Open a web browser and navigate to http://127.0.0.1:5000/.
	Enter the URL of the website you want to scrape into the input field.
	Click the "Scrape" button to initiate the scraping process.
	The scraped data will be saved in an Excel file named scraped_data.xlsx, which will be automatically downloaded.

Configuration

	The default user agent used for scraping can be configured in the WebScraper class in app.py.
	Additional customization for the web scraping logic can be done in the WebScraper class, such as handling pagination or extracting specific elements.
