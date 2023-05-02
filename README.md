# instagram
#Como usar

1- Certifique-se de que o Firefox está instalado no seu sistema e que está instalado no local padrão <br>
Se o Firefox não estiver instalado no local padrão, você pode especificar sua localização usando a opção  <br>
ao criar uma instância do Firefox. 'binary_location'

2- Talvez seja necessário especificar a capacidade de dizer ao Selenium onde encontrar o binário do Firefox. <br>
Por exemplo, você pode passar o caminho para o binário do Firefox como um argumento ao criar uma instância do Firefox: 'moz:firefoxOptions.binary'

from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.binary_location = '/path/to/firefox/binary'
driver = Firefox(options=options)
