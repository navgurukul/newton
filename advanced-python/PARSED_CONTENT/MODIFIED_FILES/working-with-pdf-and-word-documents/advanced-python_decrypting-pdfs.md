```ngMeta
decrypting-pdfs_key1
```
# decrypting-pdfs_key2
decrypting-pdfs_key3

```python
   >>> import PyPDF2
   >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
❶ >>> pdfReader.isEncrypted
```
decrypting-pdfs_key4```python
   >>> pdfReader.getPage(0)
```
decrypting-pdfs_key5decrypting-pdfs_key6```python
❸ >>> pdfReader.decrypt('rosebud')
```
decrypting-pdfs_key7```python
   >>> pageObj = pdfReader.getPage(0)
```
decrypting-pdfs_key8

decrypting-pdfs_key9

