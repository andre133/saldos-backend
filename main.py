from fastapi import FastAPI
from pydantic import BaseModel
from database import init_db, add_site, get_all_sites
from saldo_scraper.multi_bet import extrair_saldo_multi

app = FastAPI()
init_db()

class Site(BaseModel):
    nome: str
    url: str
    login: str
    senha: str
    tipo: str  # multi_bet, outro_site, etc

@app.post("/adicionar")
def adicionar_site(site: Site):
    add_site(site.nome, site.url, site.login, site.senha, site.tipo)
    return {"mensagem": "Site adicionado com sucesso"}

@app.get("/saldos")
def atualizar_saldos():
    sites = get_all_sites()
    saldos = []
    for nome, url, login, senha, tipo in sites:
        if tipo == "multi_bet":
            from saldo_scraper.multi_bet import extrair_saldo_multi
            saldo = extrair_saldo_multi(url, login, senha)
        else:
            saldo = "Scraper não implementado"
        saldos.append({"nome": nome, "saldo": saldo})
    return {"saldos": saldos}
