# TED Talks Scraper

## Sobre

Crie documentos JSON estruturados com transcrições de palestras TED Talks extraindo diretamente da página, usando Python e Beautiful Soup 4

## Maratona Behind the Code

_Esse projeto foi desenvolvido como um subsídio para a resolução do [Desafio 3 - FIAP](https://github.com/maratonadev-br/desafio-3-2020), da [Maratona Behind the Code 2020](https://maratona.dev)._

Encontre no arquivo [ted.py](./ted.py) a lógica para extração de texto do TED Talks e criação do documento, e no arquivo [challenge.py](./challenge.py) as URLs pedidas no desafio 3 da Maratona Behind the Code 2020.

Para criar os documentos JSON de palestras TED Talks necessários para o desafio, siga esses passos:

1. [Instale Python 3](https://www.python.org/downloads/);
2. Abra um terminal de comandos e instale a biblioteca [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/) executando o seguinte comando: `pip install beautifulsoup4`;
3. [Instale Git](https://git-scm.com/download/), se ainda não tiver na sua máquina;
4. Clone esse repositório executando `git clone https://github.com/danitrod/ted-talks-scraper.git` e acesse o repositório com `cd ted-talks-scraper`;
5. Execute o programa com `python challenge.py`. Os arquivos JSON serão automaticamente criados na mesma pasta.

Observação: após a extração dos textos do TED Talks, recomendo fortemente que você crie um outro arquivo baseado no [ted.py](./ted.py) e modifique o que for necessário para extração dos textos da Olhar Digital.

## Licença

MIT License

Copyright (c) 2020 Daniel T. Rodrigues
