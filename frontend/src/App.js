// src/App.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Navbar, Row, Col, Button, Table, Modal, Form, Spinner } from 'react-bootstrap';

function App() {
  const [transacoes, setTransacoes] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [newTransaction, setNewTransaction] = useState({
    entidadeId: '',
    sender: '',
    receiver: '',
    amount: '',
    ramoSeguro: ''
  });
  const [errorMessage, setErrorMessage] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchTransacoes();
  }, []);

  const fetchTransacoes = async () => {
    try {
      const response = await axios.get('http://localhost:4000/transactions');
      setTransacoes(response.data);
    } catch (error) {
      console.error("Erro ao buscar transações:", error);
    }
  };

  const handleModalClose = () => {
    setShowModal(false);
    setErrorMessage('');
    setLoading(false);
  };
  
  const handleModalShow = () => {
    setShowModal(true);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewTransaction({ ...newTransaction, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage('');
    setLoading(true); // Iniciar o estado de carregamento

    try {
      // Simular um atraso para análise do agente IA
      await new Promise(resolve => setTimeout(resolve, 2000));

      const response = await axios.post('http://localhost:4000/process-transaction', newTransaction);
      setTransacoes([...transacoes, response.data]);
      setShowModal(false);
    } catch (error) {
      const detailedMessage = error.response?.data?.error || 'Erro ao processar transação.';
      setErrorMessage(detailedMessage);
    } finally {
      setLoading(false); // Parar o carregamento ao finalizar
    }
  };

  return (
    <div>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand>✅ MutualChain - Compliance Descentralizado</Navbar.Brand>
        </Container>
      </Navbar>

      <Container className="mt-4">
        <Row>
          <Col>
            <h2>Transações Registradas</h2>
            <Button variant="primary" onClick={handleModalShow} className="mb-3">
              Nova Transação
            </Button>

            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>Entidade ID</th>
                  <th>Remetente</th>
                  <th>Destinatário</th>
                  <th>Valor (SOL)</th>
                  <th>Ramo de Seguro</th>
                  <th>Status de Conformidade</th>
                  <th>Motivo</th>
                </tr>
              </thead>
              <tbody>
                {transacoes.length > 0 ? (
                  transacoes.map((transacao, index) => (
                    <tr key={index}>
                      <td>{transacao.entidadeId}</td>
                      <td>{transacao.sender}</td>
                      <td>{transacao.receiver}</td>
                      <td>{transacao.amount}</td>
                      <td>{transacao.ramoSeguro}</td>
                      <td>{transacao.complianceStatus}</td>
                      <td>{transacao.complianceReason}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan="7" className="text-center">
                      Nenhuma transação encontrada.
                    </td>
                  </tr>
                )}
              </tbody>
            </Table>
          </Col>
        </Row>
      </Container>

      <Modal show={showModal} onHide={handleModalClose}>
        <Modal.Header closeButton>
          <Modal.Title>Processar Nova Transação</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3">
              <Form.Label>Entidade ID</Form.Label>
              <Form.Control
                type="text"
                name="entidadeId"
                value={newTransaction.entidadeId}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Remetente</Form.Label>
              <Form.Control
                type="text"
                name="sender"
                value={newTransaction.sender}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Destinatário</Form.Label>
              <Form.Control
                type="text"
                name="receiver"
                value={newTransaction.receiver}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Valor (SOL)</Form.Label>
              <Form.Control
                type="number"
                name="amount"
                value={newTransaction.amount}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Ramo de Seguro</Form.Label>
              <Form.Control
                type="text"
                name="ramoSeguro"
                value={newTransaction.ramoSeguro}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            {loading && (
              <div className="text-center mb-3">
                <Spinner animation="border" variant="primary" />
                <p>Analisando transação com agentes de IA...</p>
              </div>
            )}

            {errorMessage && <p className="text-danger">{errorMessage}</p>}

            <Button variant="primary" type="submit" disabled={loading}>
              {loading ? 'Processando...' : 'Processar Transação'}
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </div>
  );
}

export default App;
