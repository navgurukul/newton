```ngMeta
name: word-documents
```
# Word Documents
Python can create and modify Word documents, which have the .docx file extension, with the python-docx module. You can install the module by running pip install python-docx. (Appendix A has full details on installing third-party modules.)

# Note
When using pip to first install Python-Docx, be sure to install python-docx, not docx. The installation name docx is for a different module that this book does not cover. However, when you are going to import the python-docx module, you’ll need to run import docx, not import python-docx.

If you don’t have Word, LibreOffice Writer and OpenOffice Writer are both free alternative applications for Windows, OS X, and Linux that can be used to open .docx files. You can download them from <span><a href="https://www.libreoffice.org">https://www.libreoffice.org</a></span> and <span><a href="http://openoffice.org"></a></span>, respectively. The full documentation for Python-Docx is available at <span><a href="https://python-docx.readthedocs.org/">https://python-docx.readthedocs.org/</a></span>. Although there is a version of Word for OS X, this chapter will focus on Word for Windows.

Compared to plaintext, .docx files have a lot of structure. This structure is represented by three different data types in Python-Docx. At the highest level, a Document object represents the entire document. The Document object contains a list of Paragraph objects for the paragraphs in the document. (A new paragraph begins whenever the user presses ENTER or RETURN while typing in a Word document.) Each of these Paragraph objects contains a list of one or more Run objects. The single-sentence paragraph in Figure 13-4 has four runs.

