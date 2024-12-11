# MutualChain: Compliance e Automação no Mercado de Seguros com Solana Blockchain e IA da Fetch.AI

Bem-vindo ao MutualChain, uma revolução tecnológica no mercado de seguros. Este projeto foi desenvolvido para garantir transparência, conformidade regulatória e automação no setor de seguros privados utilizando a tecnologia da blockchain Solana, transações via Solana Pay e análise de conformidade pela IA da Fetch.AI. Nosso objetivo é criar um ambiente seguro e confiável para sociedades anônimas e cooperativas que desejam operar dentro das normas legais, combatendo o mercado não regulado e protegendo os consumidores.

# Sobre

A Taurum (https://taurum.org) é uma proposta de negócios sobre De-Fi, Payments e Consumer Apps. Usamos blockchain e Inteligência Artificial (IA) com a seguinte missão: "oferecer serviços úteis para todos na blockchain". Orgulhosamente, a nossa primeira solução é a MutualChain, uma plataforma inovadora que visa transformar o setor de entidades mutualistas e de seguros, oferecendo uma solução automatizada e transparente para garantir a conformidade regulatória e a eficiência operacional. Com a integração da tecnologia blockchain Solana e da Inteligência Artificial da Fetch.AI, a Taurum capacita entidades a cumprirem suas missões de forma mais eficiente e segura.

Nossa solução foi motivada pela recente aprovação do Projeto de Lei Complementar nº 519/2018 na Câmara dos Deputados. A lei busca regulamentar as entidades patrimoniais mutualistas. Agora, o projeto seguiu para o Senado Federal, onde recebeu nova numeração (PLP n° 143/2024). É impossível identificar um negócio bilionário e complexo como este e desenvolver toda a solução em tão pouco tempo. O sucesso deste negócio requer uma abordagem colaborativa multissetorial complexa desde a sua regulamentação e justamente por isso tecnologias emergentes estimam expectativas consideráveis de sucesso.

Sobre o fundador da Taurum, Fred Rocha (Frederico Stefano Rocha, @fredsrocha): aluno responsável por projetos de iniciação Científica e Extensão do Ecossistema Anima Educação. Programador desde 2014. Gestor de T.I. e Bacharel em Direito. Especialista em Direito Digital e Proteção de Dados Pessoais. Possui MBA em Web 3.0. Atualmente cursa MBA em IA e está se especializando em Ciência de Dados e Big Data.

Por que participar da competição se toda a solução não foi desenvolvida? Sou universitário e aluno responsável por Projetos de Pesquisa e Extensão Universitária. Apaixonado por tecnologia e Direito. Acredito que a conexão entre as pessoas pode inspirar profissionais excepcionais a se aprofundarem no potencial bilionário dessa proposta, criando e propondo soluções inovadoras. Isso permitirá superar o maior desafio que encontrei, assegurar a eficiência da abordagem multissetorial, garantindo o sucesso deste negócio por meio de tecnologias como blockchain e Inteligência Artificial (IA) de forma colaborativa. O que costumo denominar "compliance descentralizado" é uma aposta pessoal para o futuro da governança em grandes corporações." - Fred Rocha, Fundador da Taurum.

## Contexto e Propósito

O mercado de seguros está passando por uma transformação, e o MutualChain está aqui para ser o protagonista dessa mudança. Ao considerar as normas impostas pela regulação PLP-519-2018 do Brasil, nossa solução visa garantir que apenas entidades autorizadas possam operar no mercado de seguros privados. Utilizando a blockchain da Solana, proporcionamos segurança, descentralização e imutabilidade para transações, enquanto a Fetch.AI assegura a conformidade das operações com a regulamentação vigente.

## Problema a ser Resolvido

No mercado de seguros privados, muitos participantes não autorizados (associações e clubes de benefícios) acabam operando de forma irregular, oferecendo produtos sem a devida autorização e colocando consumidores em risco. O PLP-519-2018 destaca a necessidade de um controle mais rigoroso, garantindo que apenas cooperativas e sociedades anônimas devidamente autorizadas possam operar, limitando o escopo das cooperativas e proibindo associações não regulamentadas.

## Nossa Proposta

Utilizando a tecnologia da Solana e a inteligência artificial da Fetch.AI, criamos uma plataforma transparente e segura para transações no mercado de seguros. Essa solução integra:

1. Blockchain da Solana: Para registro imutável de transações, auditabilidade e segurança.
2. Solana Pay: Para pagamento seguro e registro automático de transações financeiras.
3. IA da Fetch.AI: Para verificação da conformidade e automação do monitoramento regulatório, garantindo que apenas operações autorizadas sejam executadas.

## Visão Geral do Projeto

### Estrutura do Contrato Inteligente em Rust

O contrato inteligente foi desenvolvido em Rust e implementado na blockchain Solana. Ele garante que as transações só sejam executadas por entidades autorizadas, conforme os artigos do PLP-519-2018:

1. **Art. 24:** Somente sociedades anônimas e cooperativas autorizadas podem operar seguros privados. Nosso contrato garante que apenas essas entidades sejam aceitas.
2. **Art. 24, § 1º:** Cooperativas só podem operar seguros nos ramos de agricultura, saúde e acidentes de trabalho. O contrato possui uma lógica que valida se a cooperativa está em conformidade.
3. **Art. 24, § 2º:** Associações, clubes de benefícios e pessoas não autorizadas são explicitamente bloqueadas no contrato.

### Solana Pay e Blockchain Solana

Solana Pay é utilizado para realizar as transações financeiras de forma segura e transparente. Cada transação é registrada na blockchain da Solana, proporcionando:

1. Velocidade: Transações em segundos com baixas taxas.
2. Segurança: Dados imutáveis e auditáveis por todas as partes interessadas.

### Fetch.AI: IA para Análise de Conformidade

Integrado com agentes de inteligência artificial da Fetch.AI, cada transação é analisada em tempo real para garantir que todas as operações respeitem as normas regulatórias. A IA verifica:

1. Autorização da Entidade: A entidade está registrada e possui permissão para operar?
2. Escopo da Cooperativa: A cooperativa está atuando apenas nos ramos permitidos?
3. Bloqueio de Associações e Clubes: Verifica se não há operações por associações ou clubes de benefícios proibidos.
4. Análise em Tempo Real e Compliance Descentralizado

Os agentes de IA da Fetch.AI desempenham um papel crucial na análise e verificação das transações antes de serem registradas na blockchain. Cada transação passa por um processo de análise de conformidade que inclui:

1. **Verificação Automática de Autorização:** Antes que a transação seja realizada, os agentes de IA consultam uma base de dados descentralizada de entidades autorizadas. Caso a entidade não seja autorizada a operar seguros privados, a transação é bloqueada imediatamente. Isso garante que apenas sociedades anônimas e cooperativas devidamente autorizadas participem do mercado, conforme o Art. 24 do PLP-519-2018.
2. **Detecção de Irregularidades e Fraudes:** A IA da Fetch.AI utiliza aprendizado de máquina para identificar padrões suspeitos e comportamentos fraudulentos. Caso seja identificada alguma irregularidade, a transação é interrompida, e uma notificação é registrada no contrato inteligente para auditorias futuras. Isso ajuda a prevenir fraudes e garantir a conformidade com a regulamentação.
3. **Validação do Escopo de Operação:** No caso de cooperativas, os agentes verificam se o ramo de seguro oferecido está de acordo com as permissões estabelecidas no Art. 24, § 1º. Caso uma cooperativa esteja operando fora dos ramos de saúde, agricultura ou acidentes de trabalho, a transação é rejeitada. Isso impede que cooperativas operem seguros em áreas não permitidas.
4. **Registro de Auditoria Descentralizado:** Cada decisão dos agentes de IA é registrada no contrato inteligente de forma automática. Isso inclui informações sobre o motivo pelo qual uma transação foi bloqueada, qual regra foi violada e quem era a entidade envolvida. Esse registro de auditoria descentralizado permite que reguladores e outras partes interessadas façam verificações futuras para garantir que o sistema esteja cumprindo suas obrigações regulatórias.
5. **Feedback Automático e Melhoria Contínua:** A IA da Fetch.AI aprende continuamente com as transações analisadas e com os resultados das auditorias. Dessa forma, o sistema melhora sua capacidade de detecção de irregularidades ao longo do tempo, aumentando a eficiência e a eficácia da conformidade.

Esses agentes de IA permitem uma forma de Compliance Descentralizado, na qual as regras são aplicadas de maneira automática e transparente, sem a necessidade de intervenção humana, garantindo que todas as transações estejam em conformidade com a legislação vigente antes de serem registradas na blockchain. Essa abordagem reduz significativamente o risco de fraudes e práticas irregulares no mercado de seguros.

## Tecnologias Utilizadas

1. **Rust:** Linguagem de programação segura e eficiente para o desenvolvimento de contratos inteligentes.
2. **Solana Blockchain:** Rede blockchain para registro de transações de forma segura, descentralizada e escalável.
3. **Solana Pay:** Protocolo de pagamentos na blockchain Solana para transações rápidas e seguras.
4. **Fetch.AI:** Plataforma de inteligência artificial para monitoramento e conformidade regulatória descentralizada.
5. **React + Bootstrap:** Interface responsiva para interagir com a plataforma.

## Estrutura do Projeto

**/backend:** Inclui a interação simulada da blockchain Solana nas transações Solana Pay e simula também agentes de IA da FetchAI verificando as transações em tempo real.
**contracts:** Inclui o contrato inteligente em Rust para a blockchain Solana.
**/frontend:** Interface do usuário desenvolvida em React para interação amigável com a plataforma MutualChain.

## Exemplo Prático de Uso

Imagine uma cooperativa que oferece seguros de saúde a seus membros. Com o MutualChain:

1. A cooperativa inicia uma transação para registrar um contrato de seguro.
2. A transação é enviada à blockchain Solana via Solana Pay.

Antes do registro, a IA da Fetch.AI analisa a transação para garantir a conformidade:

1. Verifica se a cooperativa está autorizada e se o ramo de seguro está dentro dos permitidos.
2. Detecta possíveis irregularidades ou fraudes.

Caso a transação esteja em conformidade, ela é registrada de forma transparente, e o seguro é aprovado, beneficiando o consumidor com seguridade. Entretanto, caso haja alguma violação, a transação é bloqueada e um registro é adicionado ao contrato inteligente para auditoria futura.

## Como Executar o Projeto

**Contracts (Solana)**

**Compile o contrato:** cargo build-bpf
**Implemente na blockchain:** solana program deploy target/deploy/mutualchain.so

**Backend**

**Clone o repositório:** git clone https://github.com/taurumorg/MutualChain.git
**Entre na pasta do backend:** cd backend
**Instale as dependências:** npm install
**Inicie o servidor:** npm start

**Frontend**

**Entre na pasta do frontend:** cd frontend
**Instale as dependências:** npm install
**Inicie a aplicação:** npm start

![DAPP](https://taurum.org/assets/screenshots/1.png)

![DAPP](https://taurum.org/assets/screenshots/2.png)

![DAPP](https://taurum.org/assets/screenshots/3.png)

**DataScience**

Contém uma simulação em tempo real do painel administrativo de transações por geolocalização.

![DAPP](https://taurum.org/assets/screenshots/dashboard.gif)

## Benefícios da MutualChain

1. **Transparência Total:** Todas as transações são registradas na blockchain, permitindo auditoria e segurança aos clientes.
Conformidade Automática: A inteligência artificial da Fetch.AI garante que todas as operações sigam as normas estabelecidas.
2. **Eficiência Operacional:** Utilização de Solana Pay para transações instantâneas com baixas taxas.
3. **Segurança Regulamentar:** Bloqueio automático de entidades não autorizadas, protegendo consumidores contra fraudes.

## Conclusão

O MutualChain traz o futuro para o presente no mercado de seguros, garantindo segurança, transparência e, principalmente, conformidade. Com a combinação poderosa de blockchain Solana, Solana Pay e inteligência artificial da Fetch.AI, somos capazes de oferecer uma solução única e altamente segura para cooperativas e seguradoras em todo o Brasil.

🌍 Junte-se a nós e seja parte da transformação digital no mercado de seguros! Explorando tecnologia de ponta e regulação, o MutualChain está mudando o futuro do mercado mutualista para melhor.

## Licença

Este projeto está licenciado sob a licença MIT.
