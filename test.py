import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.chrome.options import Options

# WINDOW_SIZE = "1920,1080"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

# browser = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://wax.atomichub.io/market?collection_name=mlb.topps&order=asc&sort=price&symbol=WAX')
assert "AtomicHub" in browser.title


############################################## Log In ########################################

# Click 'Login'
try:
  btn_login = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div[3]/div/button[1]')
  btn_login.click()
  print('Success: click "Login"')
except Exception as e:
  print('Err: clicking "LOGIN"')
  print(e)
finally:
  pass

# Click 'Cloud Wallet'
try:
  btn_cloud_wallet = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[1]/div/button')))
  assert btn_cloud_wallet is not None
  btn_cloud_wallet.click()
  print('Success: click "Cloud Wallet"')
except Exception as e:
  print('Err: clicking "CLOUD WALLET"')
  print(e)
finally:
  browser.implicitly_wait(4)

# Click 'login' of wallet modal
try:
  browser.switch_to.window(browser.window_handles[1])
  # print(browser.title)
  # print(browser.current_url)
  btn_logins = browser.find_element(By.XPATH, '//*[@id="root"]/div/section/div[2]/div/div/button')
  btn_logins.click()
  print('Success: click "Login" of wallet modal')
except Exception as e:
  print('Err: clicking "LOGIN" of wallet')
finally:
  browser.implicitly_wait(2)

# Input email and password
try:
  browser.switch_to.window(browser.window_handles[2])
  input_email = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[5]/div/div/div/div[1]/div[1]/input')))
  time.sleep(0.3)
  input_email.send_keys('bright113gene@gmail.com', Keys.TAB)
  print('Success: input email')
  time.sleep(0.3)
  input_pass = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[5]/div/div/div/div[1]/div[2]/input')))
  input_pass.send_keys('$$K1c1h3$$')
  print('Success: input password')
except Exception as e:
  print('Err: inputing wallet info')
  print(e)
finally:
  pass


# Click 'login' of wallet modal
try:
  browser.switch_to.window(browser.window_handles[2])
  # print(browser.title)
  # print(browser.current_url)
  time.sleep(0.3)
  btn_wallet_login = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[5]/div/div/div/div[4]/button')))
  # print(btn_wallet_login.is_displayed())
  # print(btn_wallet_login.get_attribute("disabled"))
  # btn_wallet_login.submit()
  print('We are bypassing reCaptcha')
  print('Please wait for 10 sec')
  time.sleep(9)
  btn_wallet_login.click()
  print('Success: click "Login" of wallet modal')
  # btn_wallet_login.screenshot('1.png')
except Exception as e:
  print('Err: clicking "LOGIN" of wallet')
finally:
  browser.implicitly_wait(2)
  time.sleep(7)

# click 'VERIFY ME'
try:
  browser.switch_to.window(browser.window_handles[0])
  btn_verify_me = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button[2]')))
  btn_verify_me.click()
  print('Success: click "VERIFY ME"')
except Exception as e:
  print('Err: click "VERIFY ME"')
  print(e)
finally:
  browser.implicitly_wait(1)

# click 'CLOSE'
try:
  btn_close = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[3]/button')))
  btn_close.click()
  print('Success: click "CLOSE"')
except Exception as e:
  print('Err: click "CLOSE"')
  print(e)
finally:
  browser.implicitly_wait(1)


  

############################################## Select Collection ########################################

# click 'Collection'
try:
  ele_select = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div[2]/div/img')))
  assert ele_select is not None
  ele_select.click()
  print('Success: click "Collection"')
except Exception as e:
  print('Err: click "Collection"')
  print(e)
finally:
  pass

# select collection
try:
  ele_collection_container = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]')))
  print(ele_collection_container)
  # ele_collection_container = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div[2]')
  assert ele_collection_container is not None
  ele_collections = ele_collection_container.find_elements(By.TAG_NAME, 'button')
  assert ele_collections is not None
  print('Number of collections are: ', len(ele_collections))
  for button in ele_collections:
    coll_name = button.get_attribute('data-testid')
    print('> ', coll_name)
  idx = int(input('Please select collection by number: ')) - 1
  # idx = 2
  ele_collections[idx].click()
finally:
  pass

# click 'SELECT AND CLOSE'
try:
  btn_sel_close = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/button')
  btn_sel_close.click()
  print('Success: click "SELECT AND CLOSE"')
except Exception as e:
  print('Err: click "SELECT AND CLOSE"')
  print(e)
finally:
  pass

# close 'cookie panel'
try:
  btn_accept_all = browser.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div/div[3]/button[1]')
  btn_accept_all.click()
  print('Success: click "cookie panel"')
finally:
  pass

# setting for sniping NFT
try:
  input_max_price = browser.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[6]/div/span[2]/input')
  print(input_max_price.get_attribute('placeholder'), 'success')
  input_max_price.send_keys('5', Keys.RETURN)
  input_max_mint = browser.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/div[7]/div/span[2]/input')
  print(input_max_mint.get_attribute('placeholder'), 'success')
  input_max_mint.send_keys('150', Keys.RETURN)
finally:
  pass

# scroll to top
try:
  body = browser.find_element(By.TAG_NAME, 'body')
  body.send_keys(Keys.CONTROL + Keys.HOME)
except Exception as e:
  print('Err: scroll to top')
  print(e)

# click 'BUY'
try:
  btn_buy = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div[3]/button')))
  btn_buy.click()
  print('click "BUY" success')
except Exception as e:
  print('Err: click "BUY"')
  print(e)
finally:
  browser.implicitly_wait(2)

############################################## Confirmation ########################################

# click 'CLOUD WALLET'
try:
  btn_cloud_wallet = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/div[1]/div/button')))
  assert btn_cloud_wallet is not None
  btn_cloud_wallet.click()
except Exception as e:
  print('Err: clicking "CLOUD WALLET"')
  print(e)
finally:
  browser.implicitly_wait(4)

# click 'Approve'
try:
  browser.switch_to.window(browser.window_handles[1])
  btn_approve = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/section/div[2]/div/div[6]/button')))
  btn_approve.click()
  print('click "Approve" success')
  browser.implicitly_wait(2)
except Exception as e:
  print('Err: click "Approve"')
  print(e)
finally:
  # TODO: Click 'login'
  browser.switch_to.window(browser.window_handles[0])
  btn_verify_me = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button[2]')))
  btn_verify_me.click()
  print('click "VERIFY ME" success')

# click 'Approve'
try:
  browser.switch_to.window(browser.window_handles[1])
  btn_approve = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/section/div[2]/div/div[5]/button')))
  btn_approve.click()
  print('click "Approve" success')
  browser.implicitly_wait(2)
except Exception as e:
  print('Err: click "Approve"')
  print(e)
finally:
  browser.switch_to.window(browser.window_handles[0])

# click 'CLOSE'
try:
  btn_approve = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[3]/button')))
  btn_approve.click()
  print('click "CLOSE" success')
  browser.implicitly_wait(2)
except Exception as e:
  print('Err: click "CLOSE"')
  print(e)
finally:
  browser.implicitly_wait(1)

############################################## Buy ########################################

# click 'BUY'
try:
  btn_buy = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[3]/div/div[2]/div[4]/div/div/div/div/div/div/div/div[2]/div[3]/button')))
  btn_buy.click()
  print('click "BUY" success')
except Exception as e:
  print('Err: click "BUY"')
  print(e)
finally:
  browser.implicitly_wait(2)

# click 'OKEY, LETS BUY'
try:
  btn_buy = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button')))
  btn_buy.click()
  print('click "OKEY, LETS BUY" success')
except Exception as e:
  print('Err: click "OKEY, LETS BUY"')
  print(e)
finally:
  browser.implicitly_wait(2)

# click 'BUY' finally
try:
  btn_buy = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/div/div[3]/div[5]/button[2]')))
  btn_buy.click()
  print('click "BUY" success')
except Exception as e:
  print('Err: click "BUY"')
  print(e)
finally:
  browser.implicitly_wait(2)
  # input()

# click 'Approve' finally
try:
  browser.switch_to.window(browser.window_handles[1])
  btn_approve = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/section/div[2]/div/div[5]/button')))
  btn_approve.click()
  print('click "Approve" success')
  browser.implicitly_wait(2)
except Exception as e:
  print('Err: click "Approve"')
  print(e)
finally:
  browser.switch_to.window(browser.window_handles[0])
  input()



# browser.quit()
