# DATA FOLDERSsplit_credits_debits
REF_STAGE_FOLDER = 'data/ref_data/interim/'
REF_OUTPUT_FILE = 'data/ref_data/output/ref_master_data.csv'
REF_ARCHIVE_FOLDER = 'data/ref_data/archive/'

DATA_CHECKS_STAGE_FOLDER = 'data/checks/interim/'
DATA_CHECKS_OUTPUT_FILE = 'data/checks/output/checks_master_data.csv'
DATA_CHECKS_ARCHIVE_FOLDER = 'data/checks/archive/'

TX_INPUT_FOLDER = 'data/tx_data/input/'
TX_STAGE_FOLDER = 'data/tx_data/interim/'
TX_OUTPUT_FILE = 'data/tx_data/output/tx_master_data.csv'
TX_ARCHIVE_FOLDER = 'data/tx_data/archive/'

CR_VARIATIONS = frozenset(['credit', 'cr', 'cr.'])
DB_VARIATIONS = frozenset(['debit', 'dr', 'dr.'])
AMOUNT_VARIATIONS = frozenset(['amount', 'cantidad', 'monto', 'importe', 'valor'])
TYPE_NAME_VARIATIONS = frozenset(['type', 'tipo'])
TYPE_VALUE_VARIATIONS = frozenset(['credit', 'cr', 'cr.', 'c', 'debit', 'dr', 'dr.', 'd'])
DATE_VARIATIONS = frozenset(['date', 'fecha'])
DESC_VARIATIONS = frozenset(['desc', 'desc.', 'description', 'descripción', 'concepto'])
