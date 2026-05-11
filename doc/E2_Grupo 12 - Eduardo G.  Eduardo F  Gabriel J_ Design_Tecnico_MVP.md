# Entrega — Design Técnico e MVP
**Solicitação de Entrega | Estrutura de Dados**
**Prazo:** 14/05| **Peso na nota:** 25% da nota final
---

## Identificação do Grupo

| Campo | Preenchimento |
|-------|---------------|
| Nome do Projeto | TickFlow |
| Repositório GitHub | https://github.com/Yuoneeh/Tickflow_Projeto_Estrutura_de_Dados.git |
| Integrante 1 | Eduardo Felipe Braga — RA 43533758 |
| Integrante 2 | Eduardo Gabriel de Souza Cardozo — RA 45704321|
| Integrante 3 | Gabriel Jose Couto Pereira — RA 43809707|

---

## Contexto

Esta entrega combina duas etapas essenciais: **projetar antes de implementar** e **entregar software funcionando**. Primeiro você define como o sistema será construído — estruturas, arquitetura e backlog — e então implementa o núcleo funcional com as primeiras telas reais.

> **O que "funcionando de ponta a ponta" significa:**
> O usuário informa dados (via arquivo ou entrada manual), o sistema executa as operações da estrutura e exibe o resultado na tela. Se a estrutura funciona internamente mas nada é exibido, não está completo.

---

## O que entregar

### 1. Escolha e Justificativa das Estruturas de Dados

Para cada estrutura escolhida (mínimo 1, máximo 3):

- **Nome completo e categoria** (linear, hierárquica, etc.)
- **Complexidade de tempo e espaço** das operações principais em notação Big-O (inserção, remoção, busca, acesso)
- **Justificativa:** por que esta estrutura foi escolhida para este problema específico?
- **Comparação com ao menos 1 alternativa descartada** e motivo da exclusão
- **Limitações conhecidas** no contexto do problema
- **Referência bibliográfica** (livro ou artigo — ABNT ou IEEE)

---

- **Fila** (linear, hierárquica, etc.)
- **Complexidade de tempo e espaço** das operações principais em notação Big-O (inserção, remoção, busca, acesso)
- **Justificativa:** por que esta estrutura foi escolhida para este problema específico?
- **Comparação com ao menos 1 alternativa descartada** e motivo da exclusão
- **Limitações conhecidas** no contexto do problema
- **Referência bibliográfica** (livro ou artigo — ABNT ou IEEE)



---

### 2. Arquitetura em Camadas

Diagrama e descrição da arquitetura com as **3 camadas mínimas exigidas:**

| Camada | Responsabilidade |
|---|---|
| **Apresentação (UI/CLI)** | Interação com o usuário — menus, entradas e saídas |
| **Aplicação (Service)** | Orquestração das operações e regras de negócio |
| **Domínio (Core)** | Implementação das estruturas de dados e suas operações |

> O diagrama pode ser feito em qualquer ferramenta (draw.io, Mermaid, etc.) e entregue como imagem ou bloco de código no próprio `.md`.

---

### 3. Estrutura de Diretórios

Proposta de organização do repositório. Modelo sugerido:

```
/
├── src/
│   ├── core/          # Implementação das estruturas (Lista, Pilha, Fila)
│   ├── service/       # Lógica de negócio e orquestração
│   └── ui/            # Interface com o usuário (CLI ou GUI)
├── tests/             # Testes unitários
├── data/              # Arquivos de entrada/exemplo
├── doc/               # Documentação (este arquivo)
└── README.md
```

Justifique qualquer desvio do modelo acima.

---

### 4. Backlog do Projeto

Lista priorizada de funcionalidades, separada em:

- **In-Scope:** o que será implementado **(mínimo 5 itens)**
- **Out-of-Scope:** o que não será feito e por quê **(mínimo 3 itens)**

Cada item **In-Scope** deve ter um critério de aceite no formato:

> **Dado** [contexto/entrada], **quando** [ação executada], **então** [resultado esperado e verificável].

**Exemplo:**
> Dado uma pilha com 5 elementos, quando o usuário executar a operação `pop`, então o sistema remove e retorna o elemento do topo em O(1) e exibe o novo estado da pilha.

---

### 5. Repositório GitHub

- Repositório **público** com nome descritivo (ex.: `gerenciador-tarefas-pilha`, `fila-atendimento-ed`)
- Arquivo `.gitignore` configurado para a linguagem escolhida
- `README.md` com: nome do projeto, descrição em 2 linhas e **como executar** (passo a passo)
- **Mínimo de 5 commits** com prefixos semânticos: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`

---

### 6. Implementação do Núcleo

Classe/módulo da estrutura com as operações básicas implementadas:

| Estrutura | Operações obrigatórias |
|---|---|
| Lista | `inserir`, `remover`, `buscar`, `exibir` |
| Pilha | `push`, `pop`, `peek`, `está_vazia` |
| Fila | `enqueue`, `dequeue`, `frente`, `está_vazia` |

- Ao menos **1 estrutura completamente implementada** e executável
- Leitura de dados a partir de arquivo (JSON, CSV ou TXT)

---

### 7. MVP — Mínimo Produto Viável (Telas da Interface)

A interface não precisa ser polida — **precisa funcionar**. O MVP prova que os dados fluem entre as camadas e que o resultado é exibível ao usuário.

#### 7.1 Telas obrigatórias

São exigidas **3 telas mínimas**, independentemente do tipo de interface (CLI, GUI ou web):

| Tela | Descrição | O que deve conter |
|---|---|---|
| **Tela de boas-vindas / menu principal** | Ponto de entrada do sistema | Nome do sistema, opções disponíveis (operações da estrutura), opção de sair |
| **Tela de entrada de dados** | Onde o usuário informa os dados | Campo ou prompt para inserir valor, opção de carregar arquivo, confirmação da ação |
| **Tela de resultado** | Onde o sistema exibe o estado da estrutura | Resultado da operação executada, estado atual completo da estrutura, mensagem de erro em caso de operação inválida |

#### 7.2 Comportamentos mínimos esperados

- Exibir **mensagem de erro clara** para operações inválidas (ex.: `pop` em pilha vazia)
- Exibir o **estado atual da estrutura** após cada operação
- Permitir **repetição de operações** sem encerrar o programa (loop de menu)
- Permitir **encerrar o programa** de forma limpa

#### 7.3 Exemplos de interface aceitável

**CLI (linha de comando):**
```
=== Gerenciador de Pilha ===
[1] Push  [2] Pop  [3] Ver topo  [4] Exibir pilha  [0] Sair
Escolha: 1
Valor: 42
>> Elemento 42 inserido no topo.
Estado atual: [10, 25, 42]

Escolha: 2
>> Elemento removido: 42
Estado atual: [10, 25]

Escolha: 2
>> ERRO: pilha vazia. Nenhum elemento para remover.
```

**GUI simples (ex.: Tkinter, JavaFX, HTML):**
- Botões para cada operação disponível
- Campo de texto para entrada do valor
- Área de exibição do estado atual da estrutura atualizada em tempo real

#### 7.4 O que não é MVP

- Protótipo estático (imagem ou mockup sem código)
- Interface que apenas imprime o resultado final sem interação
- Programa que encerra após uma única operação

---

### 8. Testes Unitários

Para cada estrutura implementada, **3 testes unitários:**

| Teste | Descrição |
|---|---|
| **Caso base** | Entrada válida com resultado esperado conhecido |
| **Caso vazio** | Comportamento com estrutura vazia (ex.: `pop` em pilha vazia) |
| **Caso com múltiplos elementos** | Operações em sequência sobre uma estrutura populada |

---

## Critérios de Avaliação

| Critério | Peso | Mínimo para aprovação |
|---|---|---|
| Big-O correto para as operações principais de cada estrutura | 15% | Ao menos inserção e remoção declaradas |
| Justificativa técnica coerente com o problema | 10% | Estrutura adequada ao domínio escolhido |
| Diagrama de arquitetura com 3 camadas mínimas | 10% | Camadas identificadas no diagrama |
| Backlog com ≥5 itens In-Scope e ≥3 Out-of-Scope | 5% | Itens listados e diferenciados |
| Critérios de aceite no formato 'dado / quando / então' | 5% | Ao menos 3 critérios no formato correto |
| Repositório público com estrutura correta e `.gitignore` | 10% | Repositório acessível e organizado |
| Estrutura executa sem erros e produz resultado correto | 15% | Resultado correto em ≥ 2 casos de teste |
| MVP com 3 telas funcionando (menu, entrada e resultado) | 15% | Fluxo entrada → resultado demonstrável com loop de menu |
| 3 testes unitários por estrutura passando | 15% | Ao menos caso base passando |

---

## Regras de Entrega

- Preencher o template disponibilizado: `E2_Template.md` **(obrigatório)**
- Entregar o link do repositório GitHub público via sistema da disciplina
- A pasta `/doc` deve conter este arquivo
- Nome do arquivo: `E2_<grupo>_Design_Tecnico.md`

> Dúvidas no fórum da disciplina.
