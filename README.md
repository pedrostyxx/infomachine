# Script Ifomachine.py

![enter image description here](https://i.pinimg.com/564x/d5/be/ec/d5beec6d05ada464103d46ef52e24a7d.jpg)

Este script em Python foi desenvolvido para fornecer informações detalhadas sobre o sistema operacional, a CPU, a memória e os discos de uma máquina. Ele utiliza a biblioteca `psutil` para acessar essas informações e formata a saída para exibir no terminal.

## Requisitos

- Python 3.x instalado.
- Biblioteca `psutil` instalada (`pip install psutil`).

## Como Usar

1. **Executando o Script:**

   Para executar o script, siga os passos abaixo:

   - Abra um terminal ou prompt de comando.
   - Navegue até o diretório onde o script está localizado.
   - Execute o script com o comando `python infomachine.py`.

2. **Limpeza do Terminal:**

   O script inicia limpando o terminal para proporcionar uma apresentação mais limpa das informações. Isso é feito usando o comando `clear` no Linux ou `cls` no Windows.

3. **Informações Exibidas:**

   O script exibe as seguintes informações:

   - Informações gerais do sistema operacional, incluindo tempo de inicialização, nome do sistema operacional, versão do sistema operacional e arquitetura da CPU.
   - Informações sobre a CPU, como o número de núcleos físicos e lógicos e o uso da CPU em porcentagem.
   - Informações sobre a memória, incluindo a quantidade total de memória, memória disponível e memória em uso.
   - Informações sobre os discos, incluindo a quantidade total de espaço em disco, espaço usado, espaço livre e a porcentagem de espaço usado para cada unidade.

4. **Cores no Terminal:**

   O script usa a biblioteca `colorama` para definir a cor do texto no terminal para vermelho (`Fore.RED`). Isso é usado para destacar o banner no início do script.

5. **Banner no Início:**

   O script exibe um banner decorativo no início da execução. Você pode personalizar o banner conforme necessário.

## Casos de Uso

Este script pode ser útil em várias situações, incluindo:

- Verificação rápida das informações do sistema em uma máquina.
- Diagnóstico de problemas de desempenho, como alta utilização de CPU ou memória.
- Monitoramento do espaço em disco disponível em unidades montadas.
- Configuração rápida de uma visão geral das especificações da máquina.
- Uso como parte de um script de automação ou monitoramento mais amplo.

## Observações

- Certifique-se de que as bibliotecas `psutil` e `colorama` estejam instaladas para o funcionamento correto do script.
- Este script fornece informações básicas sobre o sistema. Para informações mais avançadas ou detalhadas, podem ser necessárias ferramentas de monitoramento específicas.
- Os comandos de limpeza de terminal podem variar entre sistemas operacionais. O script usa `clear` para sistemas baseados em Unix (Linux e macOS) e `cls` para sistemas Windows. Certifique-se de que esses comandos sejam reconhecidos em seu ambiente.
