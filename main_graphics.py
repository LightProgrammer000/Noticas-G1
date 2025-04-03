# Bibliotecas
import tkinter as tk            # Importando Tkinter
from requests import get        # Para fazer requisições HTTP
from bs4 import BeautifulSoup   # Para fazer o parsing do HTML


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

    noticias = ""

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
                        noticias += f"Título: {titulo}\nLink: {href}\n\n"

    except Exception as e:
        print(f"Erro ao buscar notícias: {e}")

    return noticias


# Função para exibir as notícias no campo de texto do Tkinter
def exibir_noticias(campo_texto):

    # Garante que seja uma string
    noticia = noticias_g1() or "Nenhuma notícia encontrada."

    # Limpa o campo de texto
    campo_texto.delete(1.0, tk.END)

    # Insere as notícias no campo de texto
    campo_texto.insert(tk.END, noticia)


# Função principal
def main():

    janela = tk.Tk()
    janela.title("Notícias Principais G1")

    # Criando um campo de texto para exibir as notícias
    global campo_texto
    campo_texto = tk.Text(janela, width=180, height=30)
    campo_texto.pack(padx=10, pady=10)

    # Criando um botão para buscar as notícias
    botao_buscar = tk.Button(janela, text="Buscar Notícias", command=lambda: exibir_noticias(campo_texto))
    botao_buscar.pack(pady=10)

    # Inicia a interface gráfica
    janela.mainloop()


if __name__ == '__main__':

    try:
        main()

    except Exception as e:
        print(f"Erro na execução do programa: {e}")
