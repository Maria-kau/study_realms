# RealMify — Documentação Técnica

> Plataforma de estudos gamificada desenvolvida com Python e Django, criada para transformar a rotina de estudos em uma experiência visual, progressiva e interativa.

---

# Sumário

1. Sobre o projeto
2. Objetivo
3. Problema
4. Solução proposta
5. Funcionalidades implementadas
6. Sistema de gamificação
7. Sistema de XP e níveis
8. Evolução do reino
9. Arquitetura da aplicação
10. Tecnologias utilizadas
11. Modelos principais
12. Camada de serviços
13. Autenticação
14. Biblioteca
15. Cronograma
16. Lista de tarefas
17. Progresso
18. Perfil e configurações
19. Banco de dados
20. Testes
21. Deploy
22. Estrutura do projeto
23. Fluxo da aplicação
24. Desafios encontrados
25. Possíveis melhorias futuras
26. Conclusão

--

# Sobre o projeto

O **RealMify** é uma plataforma de estudos gamificada desenvolvida com **Python e Django**.

O projeto foi criado com o objetivo de tornar o acompanhamento da rotina de estudos mais visual e motivador. Em vez de registrar apenas o tempo estudado, a aplicação transforma o progresso do usuário em elementos visuais dentro de um reino virtual.

À medida que o usuário avança em seus estudos, ele acumula experiência, evolui de nível e desenvolve seu próprio reino.

O projeto reúne conceitos de desenvolvimento backend, banco de dados, autenticação, regras de negócio, testes e deploy em uma única aplicação.

---

# Objetivo

O RealMify busca incentivar a constância nos estudos utilizando mecanismos de gamificação.

A aplicação permite que o usuário:

* organize seus conteúdos;
* planeje seus estudos;
* acompanhe seu progresso;
* acumule experiência;
* evolua de nível;
* visualize sua evolução através de um reino virtual.

A proposta é transformar a rotina de estudos em uma experiência mais interativa sem perder o foco na organização acadêmica.

---

# Problema

Muitas pessoas têm dificuldade em manter uma rotina de estudos porque o progresso nem sempre é percebido de forma clara.

Por exemplo:

* estudar 30 minutos;
* estudar uma hora;
* concluir uma tarefa.

Essas ações geram resultados, mas muitas vezes parecem abstratas.

O RealMify busca resolver esse problema transformando o progresso em uma representação visual.

---

# Solução proposta

A aplicação conecta as atividades de estudo a um sistema de progressão.

O fluxo funciona da seguinte forma:

```text
Estudo
   ↓
Progresso
   ↓
XP
   ↓
Nível
   ↓
Evolução do reino
```

Dessa forma, o usuário consegue visualizar sua constância através do crescimento do seu reino.

---

# Funcionalidades implementadas

Atualmente, o RealMify possui as seguintes funcionalidades:

* autenticação de usuários;
* perfil do usuário;
* sistema de XP;
* sistema de níveis;
* mapa do reino;
* evolução do reino;
* biblioteca de conteúdos;
* cronograma de estudos;
* lista de tarefas;
* acompanhamento de progresso;
* configurações do perfil;
* deploy da aplicação.

---

# Sistema de gamificação

A gamificação é o principal diferencial do RealMify.

O sistema relaciona o progresso acadêmico do usuário à evolução de um reino virtual.

Cada avanço nos estudos pode contribuir para:

* ganhar XP;
* subir de nível;
* adicionar construções ao reino;
* visualizar a evolução do mapa.

A gamificação não substitui a organização dos estudos, mas funciona como um incentivo adicional para manter a constância.

---

# Sistema de XP e níveis

O XP representa a experiência acumulada pelo usuário.

Conforme o usuário progride, sua experiência aumenta e pode resultar em evolução de nível.

A regra utilizada para a progressão considera o nível atual do usuário.

A fórmula utilizada é:

```text
XP necessário = nível × 100
```

Exemplo:

| Nível | XP necessário |
| ----- | ------------: |
| 1     |           100 |
| 2     |           200 |
| 3     |           300 |
| 4     |           400 |

Essa abordagem cria uma progressão simples e previsível.

---

# Evolução do reino

O reino representa visualmente a evolução do usuário.

Ele possui diferentes tipos de construções.

## Árvores

Representam os primeiros avanços dentro do sistema.

Exemplo de progressão:

```text
30 minutos de estudo → árvore
```

## Casas

Representam uma evolução maior.

Exemplo:

```text
1 hora de estudo → casa + árvores
```

## Construções especiais

Representam marcos mais importantes dentro da progressão.

## Castelos

Representam conquistas maiores dentro do reino.

A evolução do mapa é calculada pelo backend de acordo com as regras de negócio da aplicação.

---

# Posicionamento das construções

As construções não são exibidas todas na mesma posição.

O projeto possui lógica responsável por gerar posições para os elementos do mapa.

O serviço responsável é:

```python
get_random_positions()
```

Essa abordagem permite distribuir visualmente as construções pelo reino.

---

# Geração do reino

A geração do reino é centralizada em uma camada de serviços.

O serviço:

```python
generate_realm()
```

é responsável por gerar ou atualizar o reino de acordo com os dados de progresso.

Essa separação evita concentrar regras complexas diretamente nas views.

---

# Adição de construções

A criação de novos elementos no reino é realizada por uma regra específica.

O serviço:

```python
add_building()
```

centraliza essa operação.

Dessa forma, as regras relacionadas à evolução do reino permanecem organizadas em um único local.

---

# Reset semanal

O projeto também possui uma mecânica de reset semanal do reino.

O serviço responsável é:

```python
reset_weekly_realm()
```

Essa funcionalidade atualiza o reino de acordo com o ciclo definido pela aplicação.

A regra é validada por testes automatizados.

---

# Arquitetura da aplicação

O RealMify utiliza o framework Django.

A organização geral segue a separação entre:

* Models;
* Views;
* Templates;
* Services.

Representação simplificada:

```text
Usuário
   ↓
Templates
   ↓
Views
   ↓
Services
   ↓
Models
   ↓
PostgreSQL
```

A camada de serviços é utilizada para concentrar regras de negócio relacionadas à progressão e ao reino.

---

# Tecnologias utilizadas

## Backend

* Python
* Django

## Banco de dados

* PostgreSQL

## Frontend

* HTML5
* CSS3
* JavaScript

## Infraestrutura

* Render
* Gunicorn
* WhiteNoise

## Controle de versão

* Git
* GitHub

---

# Modelos principais

## Profile

O modelo `Profile` complementa os dados do usuário.

Ele armazena informações relacionadas à progressão, como:

* nível;
* XP;
* dados do perfil.

## Realm

O modelo `Realm` representa o reino do usuário.

Entre seus dados estão contadores de construções, como:

* árvores;
* casas;
* construções especiais;
* castelos;
* informações relacionadas ao último reset.

Representação conceitual:

```text
Realm
├── arvores
├── casas
├── especiais
├── castelos
└── ultimo_reset
```

## Avatar

O projeto também possui uma entidade relacionada ao avatar do usuário.

---

# Relacionamento entre usuário e reino

Cada usuário possui seus próprios dados de progressão.

```text
User
│
├── Profile
│
└── Realm
    ├── Árvores
    ├── Casas
    ├── Especiais
    └── Castelos
```

Essa estrutura garante que os dados de cada usuário permaneçam separados.

---

# Camada de serviços

As regras mais específicas da aplicação foram separadas em serviços.

Entre elas estão:

```text
get_random_positions()
add_building()
generate_realm()
reset_weekly_realm()
```

Essa organização facilita a manutenção e a realização de testes.

---

# Autenticação

O sistema possui autenticação de usuários.

O fluxo geral é:

```text
Cadastro
   ↓
Usuário criado
   ↓
Perfil associado
   ↓
Reino associado
   ↓
Login
   ↓
Acesso à aplicação
```

As informações de progresso e do reino são associadas ao usuário autenticado.

---

# Biblioteca

A biblioteca permite organizar conteúdos de estudo.

Os conteúdos podem ser estruturados de forma a facilitar a organização da jornada de aprendizagem.

Ela funciona como uma área central para os materiais utilizados pelo usuário.

---

# Lista de tarefas

A lista de tarefas permite registrar atividades que precisam ser concluídas.

O fluxo conceitual é:

```text
Tarefa criada
   ↓
Tarefa pendente
   ↓
Tarefa concluída
```

Ela auxilia o usuário na organização das atividades do dia a dia.

---

# Progresso

O sistema de progresso conecta as atividades realizadas à mecânica de gamificação.

Ele é responsável por fornecer os dados utilizados pelos sistemas de XP, níveis e evolução do reino.

Assim, existe uma ligação direta entre a rotina do usuário e o crescimento visual do mapa.

---

# Perfil e configurações

A aplicação possui áreas destinadas ao perfil e às configurações.

Essas seções permitem ao usuário acessar e gerenciar informações relacionadas à sua conta dentro do sistema.

---

# Banco de dados

O projeto utiliza **PostgreSQL** como banco de dados relacional.

Ele armazena informações persistentes da aplicação, incluindo dados relacionados a:

* usuários;
* perfis;
* reinos;
* progresso;
* conteúdos;
* cronogramas;
* tarefas.

O uso de um banco relacional facilita o gerenciamento dos relacionamentos entre essas entidades.

---

# Transações e integridade dos dados

Operações que envolvem múltiplas alterações no banco utilizam mecanismos de transação.

Um exemplo é a criação de um usuário e das entidades associadas.

O uso de:

```python
transaction.atomic()
```

garante que a operação seja executada de forma consistente.

Fluxo conceitual:

```text
Início da transação
   ↓
Criação do usuário
   ↓
Criação do Profile
   ↓
Criação do Realm
   ↓
Commit
```

Caso ocorra um erro, a operação pode ser revertida, evitando dados incompletos.

---

# Testes

O projeto utiliza os testes automatizados fornecidos pelo Django.

Os testes ajudam a validar regras importantes da aplicação.

Entre os comportamentos verificados estão:

* criação de usuários;
* criação do perfil;
* criação do reino;
* regras de progressão;
* reset semanal do reino.

Um dos testes está relacionado ao reset semanal:

```text
RealmResetTest
```

Esse teste verifica se os dados do reino são atualizados corretamente durante o processo de reset.

---

# Deploy

A aplicação está hospedada no **Render**.

O ambiente de produção utiliza:

* Django;
* Gunicorn;
* PostgreSQL;
* WhiteNoise.

Durante o deploy são executadas etapas como:

* instalação das dependências;
* coleta dos arquivos estáticos;
* migrações do banco de dados.

Exemplo do processo de build:

```bash
pip install -r requirements.txt && cd project_realms && python manage.py collectstatic --noinput && python manage.py migrate && python create_admin.py
```

---

# Estrutura geral do projeto

A organização geral segue uma estrutura semelhante a:

```text
study_realms/
│
├── project_realms/
│   ├── manage.py
│   ├── apps/
│   ├── templates/
│   ├── static/
│   └── settings/
│
├── requirements.txt
├── README.md
├── DOCUMENTACAO.md
└── ...
```

A estrutura exata pode variar conforme a organização atual do repositório.

---

# Fluxo da aplicação

O funcionamento geral pode ser representado assim:

```text
Usuário
   ↓
Autenticação
   ↓
Biblioteca / Cronograma / To-List
   ↓
Estudos
   ↓
Progresso
   ↓
XP
   ↓
Nível
   ↓
Evolução do reino
   ↓
Mapa
```

---

# Desafios encontrados

Durante o desenvolvimento foram encontrados desafios relacionados a:

* configuração de URLs;
* integração entre views e templates;
* regras de negócio;
* testes automatizados;
* reset semanal do reino;
* persistência dos dados;
* deploy da aplicação.

Um exemplo foi o erro `NoReverseMatch`, que ocorre quando o Django não consegue encontrar uma URL associada ao nome utilizado.

A solução envolveu revisar a correspondência entre:

```text
URL
 ↓
name
 ↓
view
 ↓
template
```

Outro desafio foi garantir que o reset semanal realmente atualizasse os dados do reino, comportamento posteriormente validado por testes.

---

# Possíveis melhorias futuras

As funcionalidades abaixo são **ideias para futuras versões** e ainda não fazem parte da versão atual da aplicação.

* sistema de conquistas;
* sequência de dias estudando;
* gráficos mais detalhados;
* recomendações personalizadas;
* integração com inteligência artificial;
* aplicativo mobile;
* API REST.

Essas melhorias poderiam ampliar a experiência do usuário e permitir a evolução do projeto.

---

# Como executar localmente

## Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

## Entrar no projeto

```bash
cd study_realms
```

## Criar ambiente virtual

```bash
python -m venv .venv
```

## Ativar ambiente

Windows:

```bash
.venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar migrações

```bash
python manage.py migrate
```

## Executar servidor

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

---

# Links

**Aplicação:**

https://realmify.onrender.com/

**Repositório:**

https://github.com/Maria-kau/study_realms

---

# Conclusão

O **RealMify** é uma aplicação de estudos gamificada que reúne conceitos importantes do desenvolvimento de software em um único projeto.

A aplicação combina:

* backend com Python e Django;
* banco de dados PostgreSQL;
* autenticação;
* regras de negócio;
* testes automatizados;
* deploy;
* gamificação.

O principal diferencial do projeto é transformar o progresso nos estudos em uma evolução visual dentro de um reino virtual, criando uma experiência mais interativa e motivadora para o usuário.

Além de seu objetivo funcional, o projeto serviu como uma experiência prática no desenvolvimento de aplicações web completas, envolvendo desde a modelagem dos dados até a publicação da aplicação em produção.

---

## Desenvolvedora

**Maria_Kauéllene**

Projeto desenvolvido para estudo e portfólio profissional.

> **RealMify — Transformando progresso em um reino.**
