# instagram
# Como usar

1- Certifique-se de que o Firefox está instalado no seu sistema e que está instalado no local padrão <br>
   Se o Firefox não estiver instalado no local padrão, você pode especificar sua localização usando a opção  <br>
   ao criar uma instância do Firefox. 'binary_location'

2- Talvez seja necessário especificar a capacidade de dizer ao Selenium onde encontrar o binário do Firefox. <br>
   Por exemplo, você pode passar o caminho para o binário do Firefox como um argumento ao criar uma instância do Firefox: 'moz:firefoxOptions.binary'
<br>
<br>
<br>

from selenium.webdriver import Firefox, FirefoxOptions <br>
<br>
options = FirefoxOptions() <br>
options.binary_location = '/path/to/firefox/binary' <br>
driver = Firefox(options=options) <br>
