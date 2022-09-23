# ⚕ Extract Data Anvisa

## 📝 Descrição:
O projeto extrai de uma planilha em excel disponibilizada no site da anvisa ([Link](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/cmed/precos)) o preço mínimo e máximo de todos os remêdios vendidos no Brasil, após extair os dados criamos criamos um backend (Firebase) para ser consumido por um aplicativo mobile e assim será possível escanear o codigo de barras do medicamento e verificar se o valor praticado na farmácia esta próximo o distante do valor máximo estipulado pela Anvisa. 

## 🔧 Tecnologias utilizadas:
* Python
* Firebase 

## 🚀 Rodando o projeto:
* Criar credenciais do firebase ([Link](https://firebase.google.com/docs/database/admin/start))
* git clone 
* python pip install -r /path/to/requirements.txt
* python main.py