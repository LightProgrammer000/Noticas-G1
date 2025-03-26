# Bibliotecas
import tkinter as tk            # Importando Tkinter
from requests import get        # Para fazer requisições HTTP
from bs4 import BeautifulSoup   # Para fazer o parsing do HTML

# Criando a janela principal do Tkinter
global campo_texto

# Função para realizar a requisição HTTP
def requisicao(url):
    try:
        resp = get(url)

        if resp.status_code == 200:
            return resp.text

    except Exception as e:
        print(f"Erro de Requisição: {e}")

    return None


# Função para fazer o parsing do HTML
def parsing_soup(resp_html):

    try:

        # Converte HTML em objeto BeautifulSoup
        return BeautifulSoup(resp_html, "html.parser")

    except Exception as e:
        print(f"Erro ao fazer o parsing: {e}")

    return None


# Função para buscar as notícias mais lidas
def noticias_g1():

    global noticias

    try:
        url = "https://g1.globo.com/"

        resp_html = requisicao(url)  # Obtém o HTML da página

        if resp_html:
            soup = parsing_soup(resp_html)  # Converte o HTML em BeautifulSoup

            if soup:
                div = soup.find_all("div", class_="feed-post-body")  # Busca pelas notícias
                noticias = ""

                for i in div:
                    link = i.find("a")  # Encontra o link da notícia

                    if link:
                        href = link["href"]
                        titulo = link.get_text(strip=True)

                        noticias += f"Título: {titulo}\nLink: {href}\n\n"

    except Exception:
        return noticias # Retorna as notícias encontradas

    return None

# Função para exibir as notícias no campo de texto do Tkinter
def exibir_noticias(campo_texto):

    noticia = noticias_g1()                # Busca as notícias
    campo_texto.delete(1.0, tk.END)   # Limpa o campo de texto
    campo_texto.insert(tk.END, noticia)     # Insere as notícias no campo de texto


def main():

    janela = tk.Tk()
    janela.title("Notícias Principais G1")

    # Criando um botão para buscar as notícias
    botao_buscar = tk.Button(janela, text="Buscar Notícias", command=lambda: exibir_noticias(campo_texto))
    botao_buscar.pack(pady=10)

    # Criando um campo de texto para exibir as notícias
    campo_texto = tk.Text(janela, width=180, height=30)
    campo_texto.pack(padx=10, pady=10)

    # Inicia a interface gráfica
    janela.mainloop()

if __name__ == '__main__':

    try:
        main()

    except Exception as e:
        print(e)
