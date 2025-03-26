# Bibliotecas necessárias
from requests import get        # Para fazer requisições HTTP
from colorama import Fore       # Para colorir a saída no terminal
from bs4 import BeautifulSoup   # Para fazer o parsing do HTML


# Função para realizar a requisição HTTP
def requisicao(url):

    try:
        resp = get(url)

        if resp.status_code == 200:

            resp_html = resp.text

            return resp_html

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Erro de Requisição: {e}!{Fore.RESET}")

    return None


# Função para fazer o parsing do HTML
def parsing_soup(resp_html):

    try:

        # Converte HTML em objeto BeautifulSoup
        soup = BeautifulSoup(resp_html, "html.parser")
        return soup

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Erro ao fazer o parsing: {e}!{Fore.RESET}")

    return None


# Função para buscar as notícias mais lidas
def noticias_g1():

    try:

        url = "https://g1.globo.com/"

        # Obtém o HTML da página
        resp_html = requisicao(url)

        if resp_html:

            # Converte o HTML em BeautifulSoup
            soup = parsing_soup(resp_html)

            if soup:

                # Busca pelas notícias
                div = soup.find_all("div", class_="feed-post-body")

                for i in div:

                    # Encontra o link da notícia
                    link = i.find("a")

                    if link:

                        href = link["href"]
                        titulo = link.get_text(strip=True)

                        print(f"{Fore.LIGHTGREEN_EX}Título: {titulo}{Fore.RESET}")
                        print(f"{Fore.LIGHTYELLOW_EX}Link: {href}{Fore.RESET}\n")

    except Exception:
        pass


# Função principal
def main():

    # Executa a função de buscar notícias
    noticias_g1()


# Executa o script
if __name__ == '__main__':
    main()