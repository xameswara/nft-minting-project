# NFT Minting Project

Proyek ini adalah implementasi sederhana untuk minting NFT menggunakan Python dan Web3.py.

## Prasyarat

- Python 3.7 atau lebih baru
- pip (Python package installer)
- Akun Infura (untuk akses ke jaringan Ethereum)
- Dompet Ethereum dengan saldo ETH yang cukup untuk biaya gas
- Kontrak NFT yang sudah di-deploy

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/vandrevx/nft-minting-project.git
   cd nft-minting-project
   ```

2. (Opsional tapi disarankan) Buat dan aktifkan virtual environment:
   ```
   python -m venv nft_env
   source nft_env/bin/activate  # Untuk Unix atau MacOS
   nft_env\Scripts\activate  # Untuk Windows
   ```

3. Instal dependensi dengan menjalankan:
   ```
   pip install -r requirements.txt
   ```

4. Sesuaikan konfigurasi:
   - Buka file `config/settings.py`
   - Isi nilai-nilai berikut:
     - `INFURA_PROJECT_ID`: ID proyek Infura Anda
     - `CONTRACT_ADDRESS`: Alamat kontrak NFT Anda
     - `WALLET_ADDRESS`: Alamat dompet Ethereum Anda
     - `PRIVATE_KEY`: Kunci pribadi dompet Anda (jangan pernah bagikan atau commit ke repositori)

5. Persiapkan metadata NFT:
   - Edit file `data/metadata.json` sesuai dengan NFT yang ingin Anda mint
   - Pastikan untuk meng-upload metadata ini ke IPFS atau server lain yang dapat diakses publik

6. Implementasi IPFS (jika menggunakan):
   - Di file `src/utils.py`, implementasikan fungsi `upload_to_ipfs()` sesuai dengan penyedia IPFS yang Anda gunakan (misalnya Pinata, Infura IPFS)

## Penggunaan

1. Pastikan Anda berada di folder utama proyek

2. Jalankan skrip minting dengan perintah:
   ```
   python src/mint_nft.py
   ```

3. Jika berhasil, Anda akan melihat pesan konfirmasi dengan hash transaksi

4. Anda dapat memeriksa transaksi di Etherscan dengan hash tersebut

## Catatan Penting

- Pastikan Anda memiliki cukup ETH untuk biaya gas
- Sangat disarankan untuk menguji terlebih dahulu di jaringan uji (testnet) seperti Goerli atau Sepolia sebelum menggunakan di jaringan utama (mainnet)
- Jika menggunakan testnet, ubah `chainId` di `src/mint_nft.py` dan URL provider di `config/settings.py` sesuai dengan jaringan yang digunakan
- Jangan pernah membagikan atau meng-commit kunci pribadi Anda ke repositori publik

## Troubleshooting

Jika Anda mengalami masalah:
1. Pastikan semua konfigurasi di `config/settings.py` sudah benar
2. Verifikasi bahwa kontrak NFT Anda memiliki fungsi `mintNFT` yang sesuai
3. Periksa koneksi internet dan akses ke Infura
4. Pastikan dompet Anda memiliki cukup ETH untuk biaya gas

## Lisensi

[MIT License](https://opensource.org/licenses/MIT)

## Kontribusi

Kontribusi selalu diterima. Silakan buka issue atau submit pull request jika Anda ingin berkontribusi.
