class EntityType:
    BLOCK = 'block'
    TRANSACTION = 'transaction'
    RECEIPT = 'receipt'
    LOG = 'log'
    TOKEN_TRANSFER = 'token_transfer'
    TRACE = 'trace'
    CONTRACT = 'contract'
    TOKEN = 'token'
    GETH_TRACE = 'geth_trace'

    ALL_FOR_STREAMING = [
        BLOCK,
        TRANSACTION,
        LOG,
        TOKEN_TRANSFER,
        TRACE,
        CONTRACT,
        TOKEN,
        GETH_TRACE,
    ]
    ALL_FOR_INFURA = [BLOCK, TRANSACTION, LOG, TOKEN_TRANSFER]
