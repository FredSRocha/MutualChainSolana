// tests/api.test.js

const request = require('supertest');
const { app, server } = require('../server');

// Variáveis para coleta de informações do relatório de cada teste
let testResults = [];

afterAll(done => {
  server.close(() => {
    console.log("Servidor encerrado após os testes.");
    done();
  });
});

describe('API de Transações - Testes de Integração', () => {
  it('deve obter a lista de transações (GET /transactions)', async () => {
    const response = await request(app).get('/transactions');
    expect(response.statusCode).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });

  it('deve processar uma nova transação conforme (POST /process-transaction)', async () => {
    const response = await request(app)
      .post('/process-transaction')
      .send({
        entidadeId: 'entidade_001',
        sender: 'Sender1',
        receiver: 'Receiver1',
        amount: 3,
        ramoSeguro: 'saude'
      });

    expect(response.statusCode).toBe(200);
    expect(response.body).toHaveProperty('complianceStatus', 'Compliant');
  });

  it('deve recusar uma transação de uma entidade não autorizada (POST /process-transaction)', async () => {
    const response = await request(app)
      .post('/process-transaction')
      .send({
        entidadeId: 'entidade_003',
        sender: 'Sender1',
        receiver: 'Receiver1',
        amount: 3,
        ramoSeguro: 'saude'
      });

    expect(response.statusCode).toBe(403);
    expect(response.body).toHaveProperty('error', 'Entidade não possui autorização para operar seguros.');
  });

  it('deve recusar uma transação com valor acima do limite permitido (POST /process-transaction)', async () => {
    const response = await request(app)
      .post('/process-transaction')
      .send({
        entidadeId: 'entidade_001',
        sender: 'Sender1',
        receiver: 'Receiver1',
        amount: 10,
        ramoSeguro: 'saude'
      });

    expect(response.statusCode).toBe(403);
    expect(response.body).toHaveProperty('error', 'Valor excede o limite permitido para operações não autorizadas.');
  });
});
