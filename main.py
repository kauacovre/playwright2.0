from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:

    # Definindo Browser
    browser = pw.firefox.launch(headless=False)

    # Gerenciar mais de uma página com Contexto
    context = browser.new_context()

    # Abrir navegador
    page = context.new_page()

    # Navegar para uma página
    page.goto("https://www.hashtagtreinamentos.com/")

    # Pegar infos da página
    print(page.title())

    # Selecionar elemento na tela - 2 opções
    # page.locator('xpath=/html/body/main/section[1]/div[2]/a').click()
    buttom = page.get_by_role("link", name="Quero aprender").first
    with context.expect_page() as page2_info:
        buttom.click()

    # Nova página -> criar contextos e depois:
    page2 = page2_info.value
    page2.goto("https://www.hashtagtreinamentos.com/pg-inscricao-python-impressionador?fonte=lespera&src=lespy-site&conversion=lcto-lpy26-fev26&curso=python")
    page2.get_by_role("link", name="quero garantir uma vaga").click()
    page2.locator("#botao-linkcomu-padrao1").click()
    page2.get_by_role("textbox", name="*Seu nome e sobrenome").fill("Patrick Viado")
    page2.get_by_role("textbox", name="*Seu melhor e-mail").fill("Sexo@gmail.com")
    page2.get_by_role("textbox", name="DDD").fill("99")
    page2.get_by_role("textbox", name="Seu celular").fill("9999999 ")

    # Criar nova página em branco
    # page2 = context.new_page()


    # Selecionar vários elementos
    # links = page.get_by_role("link").all()
    # for link in links:
    #    print(link)

    time.sleep(4)
    browser.close()