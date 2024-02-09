from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

#Scheduler
driver.get(" We need to provide URL")

# Locate and fill in the event creation form
event_name_input = driver.find_element(By.NAME, "username")
event_date_input = driver.find_element(By.ID, "userid")
participant_emails_input = driver.find_element(By.NAME, "username")

event_name_input.send_keys('Test Event')
event_date_input.send_keys('2024-02-12')  # Replace with the desired date
participant_emails_input.send_keys('ripan899258.com, ripan899259.com')

# Submit the form to create a new event
submit_button = driver.find_element(By.ID, "userid")
submit_button.click()

# Verify that the event appears in the user's event list
created_event = driver.find_element(By.XPATH, ".use-")
assert 'Test Event' in created_event.text
assert '2024-02-12' in created_event.text
assert 'ripan899258.com' in created_event.text
assert 'ripan899259.com' in created_event.text

# Close the browser window
driver.quit()