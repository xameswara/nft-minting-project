from web3 import Web3
import json
from config import INFURA_PROJECT_ID, CONTRACT_ADDRESS, WALLET_ADDRESS, PRIVATE_KEY

# Koneksi ke jaringan Ethereum
w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

# Baca ABI kontrak
with open('contract_abi.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Inisialisasi kontrak
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

# Fungsi untuk minting NFT
def mint_nft(token_uri):
    nonce = w3.eth.get_transaction_count(WALLET_ADDRESS)
    
    # Buat transaksi
    txn = contract.functions.mintNFT(WALLET_ADDRESS, token_uri).build_transaction({
        'chainId': 1,  # 1 untuk mainnet Ethereum
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })
    
    # Tanda tangani transaksi
    signed_txn = w3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    
    # Kirim transaksi
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    # Tunggu konfirmasi transaksi
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return tx_receipt

# Baca metadata NFT
with open('metadata.json', 'r') as metadata_file:
    metadata = json.load(metadata_file)

# Contoh penggunaan (asumsikan metadata telah di-upload ke IPFS atau server lain)
token_uri = 'https://example.com/metadata/1'  # Ganti dengan URI metadata yang sebenarnya
result = mint_nft(token_uri)
print(f"NFT berhasil di-mint! Hash transaksi: {result.transactionHash.hex()}")