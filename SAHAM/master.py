import yfinance as yf
import pandas as pd

# Daftar kode saham (gunakan format Yahoo Finance)
# Misalnya saham Indonesia diakhiri dengan '.JK'
saham_list = ['BBCA.JK', 'BBRI.JK', 'BMRI.JK', 'BBNI.JK', 'BBTN.JK']

# Rentang waktu data (bisa disesuaikan)
start_date = '2023-10-01'
end_date = '2025-10-31'

all_data = pd.DataFrame()

# Loop untuk ambil data per saham dan simpan ke CSV
for kode in saham_list:
    print(f"Mengambil data {kode} ...")
    
    # Ambil semua kolom
    data = yf.download(kode, start=start_date, end=end_date)
    
    # Tambahkan prefix nama saham di setiap kolom (supaya tidak bentrok)
    data = data.add_prefix(kode.replace('.JK', '') + '_')
    
    # Gabungkan berdasarkan index (tanggal)
    if all_data.empty:
        all_data = data
    else:
        all_data = all_data.join(data, how='outer')

# Simpan ke CSV
all_data.to_csv('data_saham_gabungan_all1.xls')

print("✅ Semua data (Open, High, Low, Close, Adj Close, Volume) berhasil disimpan dalam data_saham_gabungan_all.xls")