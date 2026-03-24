# tezz

XPT (SAS Transport) veri dosyalarını okumak için basit bir Python aracı.

## Kurulum

```bash
pip install -r requirements.txt
```

## Kullanım

Repodaki `data.xpt` örnek dosyasını okumak için:

```bash
python read_xpt.py
```

Başka bir XPT dosyasını okumak için:

```bash
python read_xpt.py path/to/file.xpt
```

## Örnek Çıktı

```
File: data.xpt
Rows: 5, Columns: 4
Columns: ['ID', 'NAME', 'AGE', 'SCORE']

 ID    NAME   AGE  SCORE
  1     Ali  25.0   85.5
  2    Ayse  30.0   92.3
  3  Mehmet  35.0   78.1
  4   Fatma  28.0   95.0
  5    Emre  42.0   88.7
```