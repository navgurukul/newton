```ngMeta
name: working-with-pdf-and-word-documents
completionMethod: manual
```
# Working with PDF and word Documents
PDF and Word documents are binary files, which makes them much more complex than plaintext files. In addition to text, they store lots of font, color, and layout information. If you want your programs to read or write to PDFs or Word documents, you’ll need to do more than simply pass their filenames to open().

Fortunately, there are Python modules that make it easy for you to interact with PDFs and Word documents. This chapter will cover two such modules: PyPDF2 and Python-Docx.

# PDF Documents
PDF stands for Portable Document Format and uses the .pdf file extension. Although PDFs support many features, this chapter will focus on the two things you’ll be doing most often with them: reading text content from PDFs and crafting new PDFs from existing documents.

The module you’ll use to work with PDFs is PyPDF2. To install it, run pip install PyPDF2 from the command line. This module name is case sensitive, so make sure the y is lowercase and everything else is uppercase. (Check out Appendix A for full details about installing third-party modules.) If the module was installed correctly, running import PyPDF2 in the interactive shell shouldn’t display any errors.

# The Problematic PDF Format

While PDF files are great for laying out text in a way that’s easy for people to print and read, they’re not straightforward for software to parse into plaintext. As such, PyPDF2 might make mistakes when extracting text from a PDF and may even be unable to open some PDFs at all. There isn’t much you can do about this, unfortunately. PyPDF2 may simply be unable to work with some of your particular PDF files. That said, I haven’t found any PDF files so far that can’t be opened with PyPDF2.

# Extracting Text from PDFs
PyPDF2 does not have a way to extract images, charts, or other media from PDF documents, but it can extract text and return it as a Python string. To start learning how PyPDF2 works, we’ll use it on the example PDF shown in Figure 13-1.

<!-- ![image](assets/000065.jpg)
 -->
Figure 13-1. The PDF page that we will be extracting text from

Download this PDF from <span><a href="http://nostarch.com/automatestuff/">http://nostarch.com/automatestuff/</a></span>, and enter the following into the interactive shell:

```python
   >>> import PyPDF2
   >>> pdfFileObj = open('meetingminutes.pdf', 'rb')
   >>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
❶ >>> pdfReader.numPages
```
   19
```python
❷ >>> pageObj = pdfReader.getPage(0)
❸ >>> pageObj.extractText()
```
   'OOFFFFIICCIIAALL BBOOAARRDD MMIINNUUTTEESS Meeting of March 7, 2015
   \n     The Board of Elementary and Secondary Education shall provide leadership
   and create policies for education that expand opportunities for children,
   empower families and communities, and advance Louisiana in an increasingly
   competitive global market. BOARD of ELEMENTARY and SECONDARY EDUCATION '
First, import the PyPDF2 module. Then open meetingminutes.pdf in read binary mode and store it in pdfFileObj. To get a PdfFileReader object that represents this PDF, call PyPDF2.PdfFileReader() and pass it pdfFileObj. Store this PdfFileReader object in pdfReader.

The total number of pages in the document is stored in the numPages attribute of a PdfFileReader object ❶. The example PDF has 19 pages, but let’s extract text from only the first page.

To extract text from a page, you need to get a Page object, which represents a single page of a PDF, from a PdfFileReader object. You can get a Page object by calling the getPage() method ❷ on a PdfFileReader object and passing it the page number of the page you’re interested in—in our case, 0.

PyPDF2 uses a zero-based index for getting pages: The first page is page 0, the second is Introduction, and so on. This is always the case, even if pages are numbered differently within the document. For example, say your PDF is a three-page excerpt from a longer report, and its pages are numbered 42, 43, and 44. To get the first page of this document, you would want to call pdfReader.getPage(0), not getPage(42) or getPage(1).

Once you have your Page object, call its extractText() method to return a string of the page’s text ❸. The text extraction isn’t perfect: The text Charles E. “Chas” Roemer, President from the PDF is absent from the string returned by extractText(), and the spacing is sometimes off. Still, this approximation of the PDF text content may be good enough for your program.