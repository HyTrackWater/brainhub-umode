# VIX | RFI: Escopo - Alteração Configuração Homologada

ID: 83
Responsável pela RFI: Marina Santoro
Status: RFI Entregue ao Cliente
Resumo Assunto: Tech: SMB Integração de Imagens
Criado em: 1 de abril de 2026 15:22
Data Aceite do Cliente: 27 de março de 2026
Data Liberação RFI: 24 de abril de 2026
Demanda relacionada: VIX
Horas Estimadas: 52
Valor Calculado: R$ 15.600,00
Cobrada?: 🎁
👥 Clientes: VIX (https://app.notion.com/p/VIX-70a10ec2756f4842a04cb12675a09d22?pvs=21)
Task (Linear): https://linear.app/umode/project/vix-integr-escrita-integracao-de-imagem-smb-26bee6529c34/overview
criado por: Marina Santoro
Key Account: Julianne

<aside>

> Um RFI - *Request For Information* é um pedido de esclarecimento de escopo para que se possa determinar o prazo e as condições de viabilidade de sua execução, de acordo com os requisitos e necessidades da solicitação
> 
</aside>

---

| **Demanda Cliente** | **Detalhamento Cliente** | **Estimativa** **uMode**
(se a estimativa for maior que 10 horas, detalhar os motivos) | **Comentário uMode** |
| --- | --- | --- | --- |
| Alteração no IP para nome impactou protocolo SMB | “Identificamos que o servidor do linx teve alteração de caminho para o novo servidor. Com isso fizemos as alterações e de VPN e acesso SBM, para o novo domínio pra evitar que houvesse erros futuros nesse sentido alterado para o novo domínio.
Mas nesse momento se formos conectar usando o acesso antigo de VPN e SBM funciona, mas somente no servidor antigo que não é mais usado e nem atualizado.

Obs.:
**Alterações de SMB** \\192.168.2.12\linx_sql_8
**Pasta** imagenslinx

**Novo caminho** \\VIX-APP01G2.vixbrasil.lan\linx
**Pasta** imagenslinx

Usuário se manteve Umode, apenas com outra senha.

Aplicativo de VPN openvpn e com a mesma chave de autenticação, só mudando a senha." | 40h (5d) + 30% de margem | uMode desativou a integração de imagens no legado para não travar o processo do time da Vix.

Após falhas no acesso da integração de imagem, identificamos que o servidor do linx teve alteração na estrutura de pastas e no IP. Com isso vamos ter que reestruturar toda o nosso tunelamento via AWS para que isso volte a funcionar com o novo IP.
 |