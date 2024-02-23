from pypdf import PdfReader, PdfWriter

def pdf_extract(pdffile, first, last):
    print(pdffile, 'Number of pages:',len(pdf_reader.pages))
    # pages = [(first, last), (1102, 1106)]
    pages = [(first, last)]
    for page_indices in pages:
        pdf_writer = PdfWriter()
        pdf_textcontent = ''
        for idx in range(page_indices[0] - 1, page_indices[1]):
            pdf_writer.add_page(pdf_reader.pages[idx])
            pdf_textcontent += '\n' + pdf_reader.pages[idx].extract_text(extraction_mode="layout", layout_mode_space_vertically=False)
        parse_DTC_table = False
        errorcode = ''
        DTC_table = ''
        table_header = ''
        for line in pdf_textcontent.split('\n'):
            if len(line)>0 and parse_DTC_table:
                # check for position 7, if below does not work
                if len(line.split()[0]) == line.find('  '): # and line.find('  ') in (2,12):
                    errorcode = line.strip().split()[0]
                    DTC_table += errorcode + ' ' + table_header + '\n'
                    DTC_table += errorcode + ' ' + line + '\n'
                elif line.find('  ')==0:
                    DTC_table += errorcode + ' ' + line + '\n'
                else:
                    parse_DTC_table = False
                    DTC_table += '\n'
            stripline = " ".join(line.split()).strip()
            if stripline.find('DTC Description')==0:
                 table_header = line
                 parse_DTC_table = True
        print(DTC_table)

pdf_name = './X150manual.pdf'
pdf_extract(pdf_name, 1, 3328)
