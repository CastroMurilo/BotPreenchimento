# Automação de Preenchimento de Formulário com PyAutoGUI
Este script Python utiliza a biblioteca PyAutoGUI para automatizar o preenchimento de um formulário web a partir de dados fornecidos em um arquivo CSV. O formulário está disponível em https://www.gabrielcasemiro.com.br/atividade_pyautogui.

# Pré-requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:

PyAutoGUI
time
Você pode instalá-las utilizando o seguinte comando:

bash
Copy code
pip install pyautogui
# Instruções de Uso
Abra o prompt de comando do Windows (win + r) e execute o script Python.
Aguarde a abertura da página web fornecida no código (https://www.gabrielcasemiro.com.br/atividade_pyautogui).
O programa espera 5 segundos para garantir que a página esteja completamente carregada.
Abra o arquivo CSV "membros.csv" no mesmo diretório do script. Certifique-se de que o arquivo tem o formato adequado (nome;sexo;email;telefone), onde cada linha representa um conjunto de dados para preencher o formulário.
O programa irá iterar sobre as linhas do arquivo CSV, preenchendo o formulário com base nos dados fornecidos.
Detalhes do Código
Pausas e failsafe: Configura pausas entre ações e ativa o failsafe do PyAutoGUI, permitindo a interrupção do programa movendo o cursor para o canto superior esquerdo da tela.
Preenchimento de campos: Utiliza imagens (localizadas no diretório "img") para identificar os campos no formulário e preenchê-los com os dados do CSV.
Captura de screenshot: Tira uma screenshot do formulário preenchido, salvando-a com o nome "cadastro_nome.png".
Alerta de conclusão: Exibe um alerta indicando que o programa foi finalizado com sucesso após processar todas as linhas do arquivo CSV.
# Observações
Certifique-se de ter as imagens no diretório "img" e ajuste a confiança (confidence) de acordo com a precisão da localização das imagens no seu ambiente.
Esperamos que este script seja útil para automatizar o preenchimento de formulários com o PyAutoGUI. Caso encontre algum problema, consulte a documentação do PyAutoGUI para obter mais informações sobre configurações e uso: https://pyautogui.readthedocs.io/
