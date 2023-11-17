
# # from selenium.webdriver import Firefox
# # user = ""
# # pass = ""
#
# url='https://senati.blackboard.com/ultra/profile'
#
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import textwrap
from selenium.webdriver.firefox.options import Options
# browser = webdriver.Firefox()
# browser.get('http://selenium.dev/')


# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)

# Create a FirefoxOptions instance and set the profile
firefox_profile_path = "/home/borous/.mozilla/firefox/i4mdlcja.Test"
# options = webdriver.FirefoxOptions()
options = Options()
options.headless = True
options.add_argument(f"--profile={firefox_profile_path}")


# salida  del service
log_filename = "geckodriver.log"
log_path = os.path.expanduser(f"~/Documents/code/Senati/NotaGeneral/{log_filename}")
service = webdriver.FirefoxService(log_output=log_path, service_args=['--log', 'debug'])

driver = webdriver.Firefox(options=options,service=service)

# driver.get("https://senati.blackboard.com/?new_loc=%2Fultra%2Fprofile")

# forma larga
# before = driver.find_element(By.CLASS_NAME, "p-icon-o365")
# submit = before.driver.find_element(By.CLASS_NAME, "icon-o365")

# forma corta
# submit = driver.find_element(By.CSS_SELECTOR,".p-icon-o365 .icon-o365")
# submit.click()


# TESTEO
# driver.get("https://www.selenium.dev/selenium/web/inputs.html")

#     # Click on the element 
# driver.find_element(By.NAME, "color_input").click()
#----------------------------------------------------------------
url="https://senati.blackboard.com/"
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"icon-o365")))
driver.find_element(By.CLASS_NAME, "icon-o365").click()


time_wait = 10
try:

    # Redirección al profile
    # redirection = "https://senati.blackboard.com/ultra/profile"
    # driver.get(redirection)
  
    # Espera  y compara si esta presente el elemento / Ruta PROFILE
    # waitE = WebDriverWait(driver, time_wait).until(
    #   EC.presence_of_element_located((By.CLASS_NAME, "makeStylesbaseText-0-2-34"))
    #   )    

    # Nombre del usuario
    # valueName = driver.find_element(By.CLASS_NAME,"makeStylesbaseText-0-2-34")
    # textName = valueName.text
    # print("Nombre: ", textName)
    #----------------------------------------------------------------
    
    # == CURSOS ACTUALES / RUTA CURSOS ==
    redirection = "https://senati.blackboard.com/ultra/course"
    driver.get(redirection)
    # Espera  y compara si esta presente el elemento / Ruta PROFILE
    WebDriverWait(driver, time_wait)

    # elementos = WebDriverWait(driver, 30).until(
    #   EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.js-course-title-element'))
    #   )
    time.sleep(5)
    # valueName = driver.find_elements(By.CLASS_NAME,'js-course-title-element')
    valueName = driver.find_elements(By.XPATH, "//h4[@class='js-course-title-element']")
    val = driver.find_elements(By.XPATH, "//div[@class='element-details summary']")
    # for i in valueName:
    #   print(f"""\
    #     ++++++++++++++++++++++++++++++++++++++++++++++++
    #     Curso:${i.text}        
    #     """,end="++++++++++++++++++++++++++++++++++++++++++++++++")
    #   print("Texto del elemento h4:", i.text)
    
    
    for i in val:
      pro = i.find_elements(By.XPATH, ".//div/div/div/div/bb-username/bb-ui-username/div/div/bdi")
      curso = i.find_elements(By.XPATH, ".//a/h4")
      for elemento_pro, elemento_curso in zip(pro, curso):
        # print("curso: ", elemento_curso.text )
        # print("instructor: ", elemento_pro.text)

        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"""Curso:${elemento_curso.text}\nInstructor:${elemento_pro.text}""")
        
        
    #
    #valueName = driver.find_elements(By.CLASS_NAME,"js-course-title-element")
    #select = Select(valueName)     

    # Realiza acciones en la siguiente página después de que se haya cargado
    # Puedes agregar aquí el código para interactuar con elementos en la siguiente página

except TimeoutException:
    print("Tiempo de espera agotado. No se pudo cargar la siguiente página a tiempo.")

    
# finally:
#     # Cerrar el navegador al finalizar
#     driver.quit()


with open(log_path, 'r') as fp:
    assert "geckodriver	INFO	Listening on" in fp.readline()

# driver.quit()

# #
#     option = webdriver.FirefoxOptions()
#     driver = webdriver.Firefox(options=option)
#     driver.get("https://google.com")
#     driver.quit()
# # driver = webdriver.Firefox(executable_path="/home/borous/Documents/code/Senati/NotaGeneral")
# # driver.get("https://dev.to") 
# #
#
#
# browser = webdriver.Firefox()
# browser.get('https://beginnerpythonprojects.com/')


# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get("https://www.google.com")
