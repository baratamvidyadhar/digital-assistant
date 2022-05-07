# digital-assistant

This script will take the user query and get the result from the search engine internally and it will also take the matematical equations gives the result of the equation.

Packages used:
wx
requests
bs4
webbrowser
wolframalpha
wikipedia 

wx:
This is c++ wrapper package which provides the GUI to digital assistant for the user to enter query.

bs4:
This package is used for pull the content from the DOM elements pages and xml pages.

requests:
This package is used to send the request to google (we can define any search engine) and get the response of the result.

webbrowser:
This package is used to open the link which are fetched from the search engine, and open each link in new tab.

wolframalpha:
This package provided the api to wolframaplha which has induced AI which will get the mathematical queries to get answered.

wikipedia:
This package is used to fecth the few lines of the renowned keywords. if this search fails then it will get the results from search engnies and open in the browser.
