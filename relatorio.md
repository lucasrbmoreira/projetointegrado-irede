# 🚀 Relatório Técnico: Projeto Integrador - Unidade 05

**Instituição:** Faculdade CDL  
**Programa:** Residência em TIC 2.0 (Capacita iRede / MCTI Futuro)  
**Aluno:** João Lucas Ribeiro Lima Moreira
**Professor:** Alberson Dantas

---

## 🏗️ 1. Planejamento da Arquitetura (Tarefa 1)

O modelo de serviço escolhido para este projeto foi o **PaaS (Platform as a Service)**.

**Justificativa:**

- **Equilíbrio entre controle e facilidade de gerenciamento:** o PaaS oferece uma base robusta sem exigir administração completa da infraestrutura.
- **Foco no código:** esse modelo permite concentrar esforços no desenvolvimento da aplicação Python e na configuração do container Docker.
- **Abstração da infraestrutura:** o provedor de nuvem gerencia sistema operacional e infraestrutura física, garantindo maior agilidade e foco na lógica de negócio.

---

## 🐳 2. Preparação do Ambiente com Docker (Tarefa 2)

A aplicação foi containerizada para garantir **portabilidade** e **isolamento**.

**Tecnologias utilizadas:**

- Python `3.10-slim`
- Framework Flask

**Configurações aplicadas:**

- **Rede isolada:** criação da `rede-projeto` para simular um ambiente de rede seguro e controlado.
- **Volume persistente:** uso do `meu_volume` mapeado para `/app/dados`, garantindo persistência dos logs gerados, essencial para auditoria em ambientes de nuvem.

---

## 🔄 3. Simulação de Deploy e CI/CD (Tarefa 3)

Foi implementada uma estratégia de **Entrega Automatizada**.

**Ferramentas e processo:**

- **GitHub Actions:** uso da extensão oficial no VS Code para monitorar e gerenciar fluxos de automação.
- **Pipeline de CI/CD:** ao realizar um `git push`, o workflow automatizado executa o build da imagem Docker e simula o deploy na plataforma de nuvem.

**Vantagem:**

- Redução de erros humanos.
- Garantia de disponibilidade da versão mais recente do código para o usuário final.

---

## 📊 4. Análise de Modelos e Conceitos (Tarefa 4)

### Comparativo de Modelos de Serviço

| Modelo | Responsabilidade do Desenvolvedor | Nível de Controle |
|---|---|---|
| IaaS | SO, Docker, Código, Rede, Segurança | Total / Complexo |
| PaaS (Usado) | Container e código Python | Equilibrado |
| SaaS | Nenhuma (apenas uso do software) | Nenhum |

### Conceitos Aplicados

- **Escalabilidade e Elasticidade:** a containerização permite que o serviço cresça (scale-up) ou diminua (scale-to-zero) automaticamente conforme a demanda de acessos.
- **Responsabilidade Compartilhada:** o provedor de nuvem responde pela segurança da infraestrutura, enquanto a equipe responde pela segurança do código e das dependências no `requirements.txt`.

---

## 🛠️ Como Reproduzir

1. Realize o clone deste repositório.
2. Construa a imagem Docker:

```bash
docker build -t minha-app-python .
```

3. Execute o container:

```bash
docker run -d -p 8080:8080 --network rede-projeto -v meu_volume:/app/dados minha-app-python
```

