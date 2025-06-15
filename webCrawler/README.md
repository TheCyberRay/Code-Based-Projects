## Basic Web Crawler Documentation

## 1. Description

### **Project Aim:**

This project uses Python to create a simple web crawler. Its main purpose is to visit a website and pull out uall the links found on that page. The script is designed to work with sites that load content dynamically (using JavaScript) by simulating a real browser.

### **What It Does:**

- Opens a website automatically.
- Waits for the page to load completely.
- Looks for all clickable links.
- Prints out the list of links it finds.

## 2. Tools and Techniques

### Python

Python is the programming language used for this project. It is known for its readability and ease of use.

### Selenium

Selenium is a tool that automates web browsers. In this project, it does the following:

- **webdriver:** This is like a remote control for the browser, it tells the browser what to do.
- **ChromeDriverManager:** This automatically installs the right version of ChromeDriver (the helper that allows Selenium to control Google Chrome).
    - **ChromeOptions:** These are settings that help make the browser act like a real person. For example, it can run without opening a visible window (headless mode) and includes tweaks to avoid detection as a bot.
- **WebDriverWait & expected_conditions (EC):** These make the script pause until certain elements (like links) are present on the page. This ensures that the page is fully loaded before the script starts grabbing links.
- **By:** This is used to tell Selenium how to find things on the page (like looking for all `<a>` tags which represent links).

### Other Python Libraries

- **time:** A simple tool to add pauses in the script. This gives the website extra time to load.
- **urllib.parse (urljoin):** This helps convert any links that are written in a short (relative) form into complete (absolute) web addresses.

## 3. Installation and Setup

### Prerequisites

- Python 3 or later
- Google Chrome or Chromium installed on your machine

### Installing Required Libraries

Open your terminal or command prompt and run the following commands:

```bash
bash

pip install selenium webdriver-manager
```

### Setting Up ChromeDriver

The project uses `webdriver_manager` to handle ChromeDriver installation automatically, so you don’t need to download it manually.

---

## 4. Code Walkthrough

Below is the full code for the web crawler, with explanations in plain language.

![webCrawlerFullScript.png](attachment:f2a9244e-255c-4ade-9bd3-fae845512689:webCrawlerFullScript.png)

Full WebCrawler Script

### **Explanation of the Imports:**

![Screenshot (21).png](attachment:ee3e6fc9-fc49-4ac7-84a8-eb9afb0be076:Screenshot_(21).png)

- **Selenium and its modules:**
    - **webdriver:** Controls the browser.
    - **Service:** Helps start the ChromeDriver automatically.
    - **ChromeOptions:** Sets options like headless mode so the browser can run in the background.
    - **By:** Finds elements on the web page.
    - **WebDriverWait and EC:** Wait until the page shows what we need (like links).
- **webdriver_manager:** Automatically downloads the correct ChromeDriver.
- **urljoin:** Makes sure any short links become complete addresses.
- **time:** Lets us pause the script briefly to give the page time to load.

---

### The Main Function: `get_links_with_selenium`

![Screenshot (20).png](attachment:e0c095b1-7835-4b5f-85d3-7024fc6e67d6:Screenshot_(20).png)

**Plain Language Explanation:**

- **Setting Up the Browser:**
    
    The script sets options so that the browser acts like a normal person using it. For example, it runs in the background and opens fully maximized.
    
- **Opening the Website:**
    
    The script directs the browser to open the specified URL. It then waits a few seconds to allow the website to load properly.
    
- **Waiting for Links:**
    
    It waits until it finds at least one link on the page. This is important for pages that load content slowly or use JavaScript.
    
- **Previewing the Page Source:**
    
    For debugging, the script prints out a small portion of the page’s code. This helps to check if the page loaded correctly.
    
- **Collecting the Links:**
    
    The script goes through all the link elements, gets the web addresses, and saves them in a list without duplicates.
    
- **Handling Errors:**
    
    If something goes wrong (for example, the page doesn’t load), the script catches the error and prints a message.
    

---

### Main Execution

![Screenshot (22).png](attachment:6c4150c9-2696-4db1-8859-accb3c33bc07:Screenshot_(22).png)

**Plain Language Explanation:**

- **Target Website:** The script is set to work with "addSite".
- **Running the Function:** It calls the `get_links_with_selenium` function to get all links from that site.
- **Output:** The script prints out how many links it found and lists each one. If nothing is found or an error happens, it notifies you.

## 5. RESULTS

![pythonWebCrawlerResults.png](attachment:057f27a3-b9e7-48ac-a70c-0ab53416f798:pythonWebCrawlerResults.png)

We can see from the above image that, we are first shown the page source of the target which we can use to debug and diagnose an execution issues. We can also confirm that the target site has 16 links. This shows that our web crawler script is running effectively.

## 6. Why This Approach?

### Advantages:

- **Automation and Reliability:** Using Selenium with headless mode allows the crawler to render JavaScript and interact with dynamically loaded content.
- **Ease of Use:** With `webdriver_manager`, managing ChromeDriver becomes hassle-free.
- **Robustness:** The script includes error handling and debugging outputs (such as the page source preview) that help diagnose issues during execution.

### Considerations:

- **Cloudflare & Bot Detection:** While this script mimics a real browser using several Chrome options, some sites with advanced bot protection may still require additional methods (like using proxies or more advanced browser automation frameworks).
- **Performance:** Selenium may be slower than a simple HTTP-based crawler due to browser rendering overhead. For large-scale crawling, consider optimizing wait times or using asynchronous methods.

---

## 7. Conclusion

---

This documentation covers the design and implementation of a basic web crawler using Python and Selenium. It explains the code structure, rationale behind choosing Selenium for dynamic content, and how the code works step by step. It also include screenshots of code, debugging outputs, and final results to enrich the documentation further.
