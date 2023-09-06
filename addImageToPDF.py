import fitz

doc = fitz.open("resources/addPDF.pdf", filetype="pdf")

for page_index in range(len(doc)):  # iterate over pdf pages
    page = doc[0]  # get the page
    # pix = page.get_pixmap()
    # pix.save("page-%i.png" % page.number)


    # insert an image logo from a file name at the top left of the document
    page.insert_image(fitz.IRect(66, 203,192, 242), filename="resources/dangdang.jpg")
doc.save("resources/logo-document.pdf")  # save the document with a new filename

