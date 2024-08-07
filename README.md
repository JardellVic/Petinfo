# PetInfo

PetInfo é um sistema de emergência desenvolvido para resolver um problema crítico em um ambiente onde o ERP pode ficar fora do ar. O script utiliza o Firebase para verificar os valores dos produtos quando o ERP está indisponível.

## Descrição

Em um ambiente de trabalho dinâmico, a indisponibilidade do ERP pode causar grandes transtornos, principalmente na verificação dos valores dos produtos. Para contornar esse problema, foi criado o PetInfo, um sistema simples com Firebase. Este script atua como um backup emergencial para acessar os valores dos produtos, garantindo a continuidade das operações até que o ERP seja restabelecido.

## Funcionalidades

- **Verificação de Valores de Produtos:** Permite consultar os valores dos produtos diretamente do Firebase.
- **Backup Emergencial:** Serve como uma solução temporária quando o ERP principal está fora do ar.

## Requisitos

- **Python**: Certifique-se de que você está usando uma versão do Python que inclui o `tkinter`. A maioria das instalações padrão do Python inclui o `tkinter`. Se você estiver usando uma distribuição mínima do Python ou um ambiente que não inclui `tkinter`, você precisará instalá-lo separadamente.

    - **No Windows**: `tkinter` geralmente está incluído na instalação padrão do Python. Caso não esteja, você pode reinstalar o Python e garantir que a opção para `tkinter` esteja marcada.

- **firebase-admin**: Biblioteca para interação com o Firebase. Isso pode ser instalado via `requirements.txt`.

## Instalação

1. Clone este repositório:

2. Navegue até o diretório do projeto:

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
4. Configure o Firebase com suas credenciais. Crie um arquivo `firebaseConfig.json` e adicione suas configurações do Firebase:
    ```json
    {
      "apiKey": "SUA_API_KEY",
      "authDomain": "SEU_AUTH_DOMAIN",
      "projectId": "SEU_PROJECT_ID",
      "storageBucket": "SEU_STORAGE_BUCKET",
      "messagingSenderId": "SEU_MESSAGING_SENDER_ID",
      "appId": "SEU_APP_ID",
      "measurementId": "SEU_MEASUREMENT_ID"
    }
    ```
5. Certifique-se de que o `tkinter` está instalado (verifique a seção de requisitos acima).

## Uso

1. Execute o script:
    ```sh
    python app.py
    ```
2. Utilize a interface de pesquisa para verificar os valores dos produtos no Firebase.

## Contato

Para mais informações, entre em contato:

- **Nome:** Jardell Silva
- **Email:** jardellvictor12@gmail.com
- **LinkedIn:** [Jardell Silva](https://www.linkedin.com/in/jarsilva/)
