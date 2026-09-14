"""
Gera o pool completo de questões (Banco A + Banco B) e grava:
  - data/pool.json   (JSON legível, para inspeção/debug)
  - pool.js          (window.CPA_POOL = {...}; consumido pelo app.js)

O app.js sorteia, a CADA tentativa (clique em "Iniciar simulado"), 40 questões de
múltipla escolha + 10 árvores de decisão a partir deste pool maior, respeitando as
proporções por módulo definidas pelo edital, e embaralha a ordem das alternativas
de cada questão sorteada. Este script NÃO faz o sorteio — apenas consolida o
banco de origem (80 MCQ + 20 árvores) que o front-end usa como universo de sorteio.
"""
import json

# ---- Banco A: reaproveita a lógica original de build_questions.py -----------
ns_a = {}
exec(open("build_questions.py").read(), ns_a)
MCQ_A = ns_a["MCQ"]
TREES_A = ns_a["TREES"]

# ---- Banco B: novos itens gerados para dar variedade entre tentativas -------
ns_b1 = {}
exec(open("mcq_pool_b.py").read(), ns_b1)
MCQ_B = ns_b1["MCQ_B"]

ns_b2 = {}
exec(open("trees_pool_b.py").read(), ns_b2)
TREES_B = ns_b2["TREES_B"]

MCQ_POOL = MCQ_A + MCQ_B
TREES_POOL = TREES_A + TREES_B

assert len(MCQ_POOL) == 80, f"Esperado 80 MCQ no pool, obtido {len(MCQ_POOL)}"
assert len(TREES_POOL) == 20, f"Esperado 20 árvores no pool, obtido {len(TREES_POOL)}"


def counts_by_theme(items):
    out = {}
    for it in items:
        out[it["theme"]] = out.get(it["theme"], 0) + 1
    return out


mcq_pool_counts = counts_by_theme(MCQ_POOL)
tree_pool_counts = counts_by_theme(TREES_POOL)

SFN = "Sistema Financeiro Nacional"
PROD = "Produtos do mercado financeiro"
REL = "Relacionamento com o cliente"
INOV = "Inovação e desenvolvimento de mercado"

WEIGHTS = {SFN: 20, PROD: 40, REL: 30, INOV: 10}

# Composição-alvo de CADA tentativa (o que o app.js sorteia do pool acima)
SAMPLE_MCQ_COUNTS = {SFN: 10, PROD: 16, REL: 9, INOV: 5}
SAMPLE_TREE_COUNTS = {PROD: 4, REL: 6}

pool = {
    "meta": {
        "title": "Simulado CPA — Certificado Profissional ANBIMA",
        "subtitle": "Formato oficial 2026 · 50 questões · 2h30 · 70% para aprovação",
        "duration_minutes": 150,
        "total_questions": 50,
        "passing_pct": 70,
        "passing_correct": 35,
        "weights": WEIGHTS,
        # composição de cada tentativa (usada no front-end para sorteio e p/ exibir a distribuição na tela inicial)
        "mcq_counts": SAMPLE_MCQ_COUNTS,
        "tree_counts": SAMPLE_TREE_COUNTS,
        # tamanho e distribuição do banco de origem (informativo)
        "pool_mcq_total": len(MCQ_POOL),
        "pool_tree_total": len(TREES_POOL),
        "pool_mcq_counts": mcq_pool_counts,
        "pool_tree_counts": tree_pool_counts,
        "sources": [
            {"label": "ANBIMA — Estruturas das provas CPA, C-Pro R e C-Pro I", "url": "https://www.anbima.com.br/pt_br/noticias/definidas-as-estruturas-das-provas-para-as-novas-certificacoes-cpa-c-pro-r-e-c-pro-i-8A2AB2AE98F3AB840198FBE551005B27-00.htm"},
            {"label": "ANBIMA — Programa detalhado CPA", "url": "https://www.anbima.com.br/data/files/6A/52/6F/A1/BED73910B07B2739B82BA2A8/Programa-Detalhado-CPA-ANBIMA.pdf"},
            {"label": "ANBIMA — Edital dos Exames de Certificação Profissional", "url": "https://www.anbima.com.br/data/files/98/96/A6/10/9C24C910CF6A83C9F82BA2A8/Edital-dos-Exames-de-Certificacao-Profissional-Anbima.pdf"},
            {"label": "ANBIMA — Programa de estudos CPA, C-Pro I e C-Pro R (guia e cadernos de questões)", "url": "https://www.anbima.com.br/pt_br/especial/pds-certificacoes-distribuicao.htm"},
        ],
    },
    "mcq": MCQ_POOL,
    "trees": TREES_POOL,
}

import os
os.makedirs("data", exist_ok=True)

with open("data/pool.json", "w", encoding="utf-8") as f:
    json.dump(pool, f, ensure_ascii=False, indent=2)

with open("pool.js", "w", encoding="utf-8") as f:
    f.write("window.CPA_POOL = ")
    json.dump(pool, f, ensure_ascii=False)
    f.write(";\n")

print("Pool MCQ:", len(MCQ_POOL), mcq_pool_counts)
print("Pool Trees:", len(TREES_POOL), tree_pool_counts)
print("Sample MCQ target:", SAMPLE_MCQ_COUNTS, "=", sum(SAMPLE_MCQ_COUNTS.values()))
print("Sample Trees target:", SAMPLE_TREE_COUNTS, "=", sum(SAMPLE_TREE_COUNTS.values()))
