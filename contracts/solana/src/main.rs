// SPDX-License-Identifier: MIT
// Contrato inteligente na linguagem RUST para a blockchain Solana
// Projeto MutualChain para operar transações via Solana Pay
// Objetivo: Regular operações de seguro conforme PLP-519-2018 e Decreto-Lei nº 73/1966.
// Observação:O projeto seguiu para o Senado Federal, onde recebeu nova numeração (PLP n° 143/2024).

// Importações necessárias para contratos inteligentes na blockchain Solana
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
};

// Módulo que define o ponto de entrada do programa
entrypoint!(process_instruction);

// Função de processamento de instruções, chamada cada vez que uma transação é executada na blockchain Solana
fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    _instruction_data: &[u8],
) -> ProgramResult {
    // Log para indicar início do processamento da transação
    msg!("Iniciando processamento da transação de seguro privado...");

    // Obtém a lista de contas envolvidas na transação
    let accounts_iter = &mut accounts.iter();

    // A primeira conta é a conta da entidade que está executando a transação
    let entidade_account = next_account_info(accounts_iter)?;

    // A segunda conta é a conta do destinatário da transação
    let destinatario_account = next_account_info(accounts_iter)?;

    // Verificação de autorização conforme Art. 24 do Decreto-Lei nº 73, de 1966
    // Apenas sociedades anônimas ou cooperativas devidamente autorizadas podem operar seguros privados.
    if !is_autorizada(entidade_account)? {
        msg!("Erro: Entidade não autorizada a operar seguros privados. (Art. 24)");
        return Err(ProgramError::Custom(0)); // Código de erro customizado para entidade não autorizada
    }

    // Verificar se a cooperativa está operando apenas nos ramos permitidos (Art. 24, § 1º)
    // Cooperativas podem operar apenas em seguros agrícolas, de saúde e de acidentes do trabalho.
    if is_cooperativa(entidade_account) && !is_ramo_permitido(entidade_account)? {
        msg!("Erro: Cooperativa operando fora dos ramos permitidos. (Art. 24, § 1º)");
        return Err(ProgramError::Custom(1)); // Código de erro customizado para ramo não permitido
    }

    // Verificação de proibição conforme Art. 24, § 2º
    // Associações, clubes de benefícios, pessoas naturais e jurídicas não autorizadas não podem operar seguros.
    if is_associacao(entidade_account) || is_clube_beneficio(entidade_account) {
        msg!("Erro: Associações e clubes de benefícios não podem operar seguros privados. (Art. 24, § 2º)");
        return Err(ProgramError::Custom(2)); // Código de erro customizado para operação não permitida
    }

    // Registro da transação na blockchain Solana via Solana Pay
    registrar_transacao(entidade_account, destinatario_account)?;

    // Sucesso ao processar a transação
    msg!("Transação de seguro privado processada com sucesso!");

    Ok(())
}

// Função auxiliar para verificar se a entidade está autorizada a operar seguros
fn is_autorizada(entidade: &AccountInfo) -> Result<bool, ProgramError> {
    // Simulação da verificação de autorização (por exemplo, verificando uma lista de entidades autorizadas)
    // Implementação futura pode incluir uma consulta a um registro externo
    if entidade.key.to_string().starts_with("autorizada") {
        Ok(true)
    } else {
        Ok(false)
    }
}

// Função auxiliar para verificar se a entidade é uma cooperativa
fn is_cooperativa(entidade: &AccountInfo) -> bool {
    // Supondo que o identificador de cooperativas comece com "coop"
    entidade.key.to_string().starts_with("coop")
}

// Função auxiliar para verificar se a entidade está operando em um ramo permitido
fn is_ramo_permitido(entidade: &AccountInfo) -> Result<bool, ProgramError> {
    // Verificar se a cooperativa está operando nos ramos: agrícola, saúde, ou acidentes do trabalho
    // Esta simulação usa o identificador de ramos no nome da conta para fins de exemplo
    let ramo = entidade.key.to_string();
    if ramo.contains("agricola") || ramo.contains("saude") || ramo.contains("acidentes") {
        Ok(true)
    } else {
        Ok(false)
    }
}

// Função auxiliar para verificar se a entidade é uma associação
fn is_associacao(entidade: &AccountInfo) -> bool {
    // Supondo que o identificador de associações comece com "assoc"
    entidade.key.to_string().starts_with("assoc")
}

// Função auxiliar para verificar se a entidade é um clube de benefícios
fn is_clube_beneficio(entidade: &AccountInfo) -> bool {
    // Supondo que o identificador de clubes de benefícios comece com "clube"
    entidade.key.to_string().starts_with("clube")
}

// Função auxiliar para registrar a transação na blockchain
fn registrar_transacao(entidade: &AccountInfo, destinatario: &AccountInfo) -> ProgramResult {
    // Lógica de registro da transação usando Solana Pay
    // Por enquanto, apenas um log indicando a execução da transação
    msg!(
        "Registrando transação: de {} para {} via Solana Pay.",
        entidade.key,
        destinatario.key
    );

    Ok(())
}
