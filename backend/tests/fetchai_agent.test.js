// tests/fetchai_agent.test.js

const FetchAIAgent = require('../fetchai_agent');

describe('FetchAIAgent - Testes de Conformidade', () => {
  let fetchAgent;

  const entidadesAutorizadas = [
    { id: 'entidade_001', tipo: 'cooperativa', autorizada: true, ramosPermitidos: ['saude', 'acidentes', 'agrícola'] },
    { id: 'entidade_002', tipo: 'sociedade_anonima', autorizada: true },
    { id: 'entidade_003', tipo: 'associacao', autorizada: false }
  ];

  // Antes de cada teste, cria uma nova instância do agente com as entidades autorizadas
  beforeEach(() => {
    fetchAgent = new FetchAIAgent(entidadesAutorizadas);
  });

  test('deve retornar conforme para uma transação de valor <= 5 SOL', async () => {
    const transaction = {
      sender: 'Sender1',
      receiver: 'Receiver1',
      amount: 3,
      entidadeId: 'entidade_001',
      ramoSeguro: 'saude'
    };

    const result = await fetchAgent.analyzeTransaction(transaction);
    expect(result.isCompliant).toBe(true);
  });

  test('deve retornar não conforme para uma transação de valor > 5 SOL', async () => {
    const transaction = {
      sender: 'Sender1',
      receiver: 'Receiver1',
      amount: 6, // Valor acima do limite
      entidadeId: 'entidade_001',
      ramoSeguro: 'saude'
    };

    const result = await fetchAgent.analyzeTransaction(transaction);
    expect(result.isCompliant).toBe(false);
    expect(result.reason).toBe('Valor excede o limite permitido para operações não autorizadas.');
  });

  test('deve detectar entidade não autorizada', async () => {
    const transaction = {
      sender: 'Sender1',
      receiver: 'Receiver1',
      amount: 3,
      entidadeId: 'entidade_003', // Entidade não autorizada
      ramoSeguro: 'saude'
    };

    const result = await fetchAgent.analyzeTransaction(transaction);
    expect(result.isCompliant).toBe(false);
    expect(result.reason).toBe('Entidade não possui autorização para operar seguros.');
  });

  test('deve detectar cooperativa operando fora do escopo permitido', async () => {
    const transaction = {
      sender: 'Sender1',
      receiver: 'Receiver1',
      amount: 3,
      entidadeId: 'entidade_001', // Cooperativa
      ramoSeguro: 'automovel' // Ramo não permitido para cooperativas
    };

    const result = await fetchAgent.analyzeTransaction(transaction);
    expect(result.isCompliant).toBe(false);
    expect(result.reason).toBe('Cooperativa não está autorizada a operar no ramo de automovel.');
  });
});
