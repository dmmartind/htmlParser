from html.parser import HTMLParser
from html.entities import name2codepoint

strings = []

fAttr= ""




def convertAttr(aInput, data=None):
    str = '['
    if data != None and data != "":
        temp = ['text', data.strip()] 
        aInput.append(temp)
    length = len(aInput)
    counter = 0
    for attr in aInput:
        if attr[1] == None:
            str += '\''+attr[0] +',\''
        elif counter < (length-1):
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"' +', '
        else:
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"'
        counter += 1
    if data != None and counter == 0:
        str += "'text' =>" + "'" + data + "'"
    str += ']'
    return str

def convertData(aInput, data=None):
    str = '['
    if data != None and data != "":
        temp = ['text', data.strip()] 
        aInput.append(temp)
    length = len(aInput)
    counter = 0
    for attr in aInput:
        if counter < (length-1):
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"' +', '
        else:
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"'
        counter += 1
    if data != None and counter == 0:
        str += "'text' =>" + "'" + data + "'"
    str += ']'
    return str



   
        

def openTag(tag,attrs):
    
    if tag == 'html':
        strings.append(  "$this->openHtml(FALSE);")
    elif tag == 'center':
        strings.append(  "$this->openCenter(FALSE);")
    elif tag == 'pre':
        strings.append(  "$this->openPre(FALSE);")
    elif tag == 'title':
        fAttr = attrs
    elif tag == 'option':
        fAttr = attrs
    elif tag == 'span':
        strings.append(  "$this->openSpan( %s, FALSE );" % convertAttr(attrs))
    elif tag == 'head':
        stri = "$this->openHead( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'body':
        stri = "$this->openBody( %s, FALSE );" % convertAttr(attrs)
        strings.append(stri)
    elif tag == 'p':
        stri = "$this->openP( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'textarea':
        stri = "$this->TextArea( %s, FALSE );" 
        
    elif tag == 'noscript':
        stri = "$this->NoScript( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'link':
        stri = "$this->Link( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'button':
        stri = "$this->Button( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'iframe':
        stri = "$this->iFrame( %s, FALSE );" % convertAttr(attrs)
        strings.append(stri  )
    elif tag == 'meta':
        stri = "$this->Meta( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'script':
        stri = "$this->Script( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'div':
        stri = "$this->openDiv( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'table':
        stri = "$this->openTable( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'tr':
        stri = "$this->openTr( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'td':
        stri = "$this->openTd( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri )
    elif tag == 'label':
        stri = ""
        
    elif tag == 'input':
        stri = "$this->Input( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'form':
        stri = "$this->openForm( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'a':
        stri = "$this->aTag( %s, FALSE );" % convertAttr(attrs)
        strings.append(stri)
    elif tag == 'img':
        stri = "$this->Image( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'li':
        stri = "$this->openLI( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'ol':
        stri = "$this->openOL( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'img':
        stri = "$this->Image( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'ul':
        stri = "$this->openUL( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'h1':
        stri = ""        
    elif tag == 'h3':
        stri = "";
    elif tag == 'br':
        stri = "";
    elif tag == 'b':
        stri = "";        
    elif tag == 'option':
        stri = "$this->option( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'select':
        stri = "$this->select( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'section':
        stri = "$this->openSection( %s, FALSE );" % convertAttr(attrs)
        strings.append( stri  )
    elif tag == 'strong':
        stri = ""
    else:
        strings.append("echo 'Error: no matching code for tag: %s'" % tag)

        

def closeTag(tag, attr=None, data=None):
    
    if tag == 'html':
        strings.append( "$this->closeHtml(FALSE);" )
    elif tag == 'center':
        strings.append( "$this->closeCenter(FALSE);" )
    elif tag == 'pre':
        strings.append( "$this->closePre(FALSE);" )
    elif tag == 'title':
        stri =  "$this->Title( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'option':
        stri =  "$this->Option( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'span':
        stri = "$this->closeSpan( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'head':
        stri = "$this->closeHead( FALSE );"
        strings.append( stri )
    elif tag == 'body':
        stri = "$this->closeBody( FALSE );"
        strings.append( stri  )
    elif tag == 'p':
        stri = "$this->closeP( %s, FALSE );" % convertData(attr,data)
        strings.append( stri  )
    elif tag == 'noscript':
        stri = "$this->NoScript( FALSE );"
        strings.append( stri )
    elif tag == 'link':
        stri = "$this->Link( FALSE );"
        strings.append(stri  )
    elif tag == 'button':
        stri = "$this->Button( FALSE );"
        strings.append(stri )
    elif tag == 'iframe':
        stri = "$this->iFrame( FALSE );"
        strings.append(stri )
    elif tag == 'meta':
        str = "$this->Meta( FALSE );"
        strings.append(stri )
    elif tag == 'script':
        stri = "$this->Script( FALSE);"
        strings.append(stri )
    elif tag == 'div':
        stri = "$this->closeDiv( FALSE );"
        strings.append(stri )
    elif tag == 'table':
        stri = "$this->closeTable( FALSE );"
        strings.append(stri )
    elif tag == 'tr':
        stri = "$this->closeTr( FALSE );"
        strings.append(stri )
    elif tag == 'td':
        stri = "$this->closeTd( FALSE );"
        strings.append(stri )
    elif tag == 'textarea':
        stri = "$this->TextArea( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)    
    elif tag == 'input':
        stri = "$this->Input( FALSE );"
        strings.append( stri)
    elif tag == 'form':
        stri = "$this->closeForm( FALSE );"
        strings.append( stri)
    elif tag == 'li':
        stri = "$this->closeLI( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
    elif tag == 'ol':
        stri = "$this->closeOL( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
    elif tag == 'label':
        stri = "$this->Label( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
    elif tag == 'a':
        stri = "$this->closeaTag( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
    elif tag == 'strong':
        stri = "$this->strong( %s, FALSE );"
        strings.append(stri)
    elif tag == 'ul':
        stri = "$this->closeUL( FALSE);"
        strings.append(stri)
    elif tag == 'h1':
        stri = "$this->openH1( %s, FALSE );" % convertData(attr,data)
        strings.append( stri  )
    elif tag == 'h3':
        stri = "$this->openH3(%s,  FALSE );" % convertData(attr,data)
        strings.append( stri  )
    elif tag == 'br':
        stri = "$this->openBR(%s,  FALSE );" % convertData(attr,data)
        strings.append( stri  )
    elif tag == 'b':
        stri = "$this->openB(%s,  FALSE );" % convertData(attr,data)
        strings.append( stri  )
    elif tag == 'section':
        stri = "$this->closeSection( FALSE );"
        strings.append( stri  )
    elif tag == 'select':
        stri = ""
    elif tag == 'option':
        stri = ""        
    elif tag == 'img':
        stri = ""
    
    else:
        strings.append("echo 'Error: no matching code for tag: %s'" % tag)
    

class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.Abucket = ""
        self.Dbucket = ""
        self.found = 0;
    
    def handle_starttag(self, tag, attrs):
        openTag(tag,attrs)
        self.Abucket = attrs
    def handle_endtag(self, tag):        
        if self.found == 1:
            closeTag(tag,self.Abucket, self.Dbucket)            
        if tag == 'form':
            closeTag(tag)
            
    def handle_data(self, data):
        self.Dbucket = data
        self.found = 1
    

    def handle_entityref(self,name):
        c = chr(name2codepoint[name])
    def handle_charref(self, name):
        if name.startswitch('x'):
            c=chr(int(name[1:], 16))
        else:
            c= chr(int(name))
    


parser = MyHtmlParser()
str = open('index.html', 'r').read()
parser.feed(str)
hdl = open('index.php', 'w')
hdl.write('<?php\n')

for line in strings:
    test = line
    hdl.write(test)
    hdl.write("\n")
hdl.write('?>')
hdl.close()

