# sentry_analyzer

Projeto para auxiliar a leitura e analise de exceções registradas no relatório de ocorrencias de determinada issue do Sentry.

## Como gerar o CSV no Sentry

1. Abra a página da ISSUE que deseja fazer a analise
2. Clique no botão `Open in discovery`
<img width="800" src="https://github.com/WallysonRodrigues/sentry_analiser/assets/8863478/c4756ddd-b886-412b-8d5a-c55a51519ba2" alt="android image" /> 

3. Filtre pelo período desejado
4. Clique no botão `Columns` para manipular o grid e formata-lo da forma correta
<img width="800" src="https://github.com/WallysonRodrigues/sentry_analiser/assets/8863478/f4220338-479f-407d-8e25-61a86005709c" alt="android image" />

5. Configure da forma abaixo
<img width="800" src="https://github.com/WallysonRodrigues/sentry_analiser/assets/8863478/4110004d-7fd6-4f0d-90ac-2da5b1eb87e9" alt="android image" />

6. Clique no botão `Export All`
<img width="800" src="https://github.com/WallysonRodrigues/sentry_analiser/assets/8863478/f5a22bca-5c28-4346-9376-d96edd0aaa52" alt="android image" />

7. Abra o seu email, o mesmo que utiliza para logar no Sentry.
8. Você receberá um email do Sentry, com o acesso para baixar o CSV.
<img width="800" src="https://github.com/WallysonRodrigues/sentry_analiser/assets/8863478/2aae0ec6-0594-456e-8664-b20012fa97e6" alt="android image" />


## Como usar

1. Certifique se de que possui o Python3 instalado em seu dispositivo, usando o seguinte comando no terminal
```
python3 --version
```
2. Execute o arquivo `analyzer.py` pelo terminal, lembrando que deve estar na pasta do arquivo .py
```
python3 analyzer.py
```
