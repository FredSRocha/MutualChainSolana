// server.js

const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const FetchAIAgent = require('./fetchai_agent');
const app = express();

app.use(cors());
app.use(bodyParser.json());

const fetchAgent = new FetchAIAgent();

// Lista para armazenar transações simuladas
let transacoes = [];

// Função para simular transações em tempo real
async function simularTransacoesEmTempoReal() {
  console.log("\n=== SIMULAÇÃO DE TRANSAÇÕES EM TEMPO REAL NA BLOCKCHAIN SOLANA ===");
  const transacoesSimuladas = [
    { entidadeId: 'entidade_001', sender: 'Sender1', receiver: 'Receiver1', amount: 3, ramoSeguro: 'saude' },
    { entidadeId: 'entidade_002', sender: 'Sender2', receiver: 'Receiver2', amount: 6, ramoSeguro: 'acidentes' },
    { entidadeId: 'entidade_003', sender: 'Sender3', receiver: 'Receiver3', amount: 2, ramoSeguro: 'agrícola' },
    { entidadeId: 'entidade_001', sender: 'Sender4', receiver: 'Receiver4', amount: 10, ramoSeguro: 'saude' }
  ];

  for (const transacao of transacoesSimuladas) {
    // Pausa para simular tempo de processamento
    await new Promise(resolve => setTimeout(resolve, 1000));

    console.log(`\nProcessando transação na blockchain Solana via Solana Pay:`);
    console.log(`Entidade: ${transacao.entidadeId}`);
    console.log(`Remetente: ${transacao.sender}`);
    console.log(`Destinatário: ${transacao.receiver}`);
    console.log(`Valor: ${transacao.amount} SOL`);
    console.log(`Ramo de Seguro: ${transacao.ramoSeguro}`);

    // Simular análise de conformidade pela Fetch.AI
    const complianceResult = await fetchAgent.analyzeTransaction({
      sender: transacao.sender,
      receiver: transacao.receiver,
      amount: transacao.amount,
      entidadeId: transacao.entidadeId,
      ramoSeguro: transacao.ramoSeguro
    });

    if (complianceResult.isCompliant) {
      console.log(`Status de Conformidade: ✅ Conforme`);
    } else {
      console.log(`Status de Conformidade: ❌ Não Conforme - Motivo: ${complianceResult.reason}`);
    }

    // Armazenar a transação e seu status de conformidade
    transacoes.push({
      ...transacao,
      complianceStatus: complianceResult.isCompliant ? 'Compliant' : 'Non-Compliant',
      complianceReason: complianceResult.reason || 'N/A'
    });
  }
  console.log("\n===============================\n");
}

// Endpoint para obter todas as transações
app.get('/transactions', (req, res) => {
  res.status(200).json(transacoes);
});

// Endpoint para processar uma nova transação
app.post('/process-transaction', async (req, res) => {
  const { entidadeId, sender, receiver, amount, ramoSeguro } = req.body;

  try {
    // Analisar a transação quanto à conformidade
    const complianceResult = await fetchAgent.analyzeTransaction({
      sender,
      receiver,
      amount,
      entidadeId,
      ramoSeguro
    });

    if (!complianceResult.isCompliant) {
      return res.status(403).json({ error: complianceResult.reason });
    }

    // Armazenar a transação conforme
    const newTransaction = {
      entidadeId,
      sender,
      receiver,
      amount,
      ramoSeguro,
      complianceStatus: 'Compliant'
    };
    transacoes.push(newTransaction);

    res.status(200).json(newTransaction);
  } catch (error) {
    console.error('Erro ao processar transação:', error);
    res.status(500).json({ error: 'Erro ao processar transação: ' + error.message });
  }
});

// Declaração e inicialização do servidor
let server;

// Verifique se estamos em modo de teste
if (process.env.NODE_ENV !== 'test') {
  const PORT = process.env.PORT || 4000;
  server = app.listen(PORT, async () => {
    console.log(`Servidor rodando na porta ${PORT}`);
    await simularTransacoesEmTempoReal();
    console.log('Simulação de transações concluída. O servidor está pronto para receber novas requisições.');
  });
} else {
  // Se estivermos em modo de teste, o servidor será inicializado em uma porta dinâmica
  server = app.listen(0);
}

// Exportar o servidor para testes
module.exports = { app, server };
