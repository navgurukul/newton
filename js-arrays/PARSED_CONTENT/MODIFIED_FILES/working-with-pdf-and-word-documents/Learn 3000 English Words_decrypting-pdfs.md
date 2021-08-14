decrypting-pdfs_key1
decrypting-pdfs_key2


```python
   >>> import PyPDF2
   >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
❶ >>> pdfReader.isEncrypted
```
decrypting-pdfs_key3
```python
   >>> pdfReader.getPage(0)
```
decrypting-pdfs_key4
```python
❸ >>> pdfReader.decrypt('rosebud')
```
decrypting-pdfs_key5
```python
   >>> pageObj = pdfReader.getPage(0)
```
decrypting-pdfs_key6


decrypting-pdfs_key7
