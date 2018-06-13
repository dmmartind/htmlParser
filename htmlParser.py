from html.parser import HTMLParser
from html.entities import name2codepoint

strings = ["" for x in range(500)]

def convertTuple(aInput):
    str = '['
    for attr in aInput:
        str = str + attr[0] + '=>' + attr[1] + ', '
    str = ']'
    return str
        

def openTag(tag,attrs):
    
    if tag == 'html':
        strings.append(  "$this->openHtml(FALSE);")
    if tag == 'title':
        stri =  "$this->Title( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'span':
        strings.append(  "$this->openSpan( {%s}, FALSE );" % convertTuple(attrs))
    if tag == 'head':
        stri = "$this->openHead( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'body':
        stri = "$this->openBody( {%s}, FALSE );" % convertTuple(attrs)
        strings.append(stri)
    if tag == 'p':
        stri = "$this->openP( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'noscript':
        stri = "$this->NoScript( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'link':
        stri = "$this->Link( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'button':
        stri = "$this->Button( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    if tag == 'iframe':
        stri = "$this->iFrame( {%s}, FALSE );" % convertTuple(attrs)
        strings.append(stri  )
    if tag == 'meta':
        stri = "$this->Meta( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'script':
        stri = "$this->Script( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'div':
        stri = "$this->openDiv( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'label':
        stri = "$this->Label( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    if tag == 'input':
        stri = "$this->Input( {%s}, FALSE );" % convertTuple(attrs)
        strings.append( stri  )

        

def closeTag(tag):
    sAttr = '['
    
    if tag == 'html':
        stri = "$this->closeHtml(FALSE);"
        strings.append( stri )
    if tag == 'title':
        stri = "$this->Title( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'span':
        stri = "$this->closeSpan( {%s}, FALSE );"
        strings.append( stri )
    if tag == 'head':
        stri = "$this->closeHead( {%s}, FALSE );"
        strings.append( stri )
    if tag == 'body':
        stri = "$this->closeBody( {%s}, FALSE );"
        strings.append( stri  )
    if tag == 'p':
        stri = "$this->closeP( {%s}, FALSE );"
        strings.append( stri )
    if tag == 'noscript':
        stri = "$this->NoScript( {%s}, FALSE );"
        strings.append( stri )
    if tag == 'link':
        stri = "$this->Link( {%s}, FALSE );"
        strings.append(stri  )
    if tag == 'button':
        stri = "$this->Button( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'iframe':
        stri = "$this->iFrame( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'meta':
        str = "$this->Meta( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'script':
        stri = "$this->Script( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'div':
        stri = "$this->closeDiv( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'label':
        stri = "$this->Label( {%s}, FALSE );"
        strings.append(stri )
    if tag == 'input':
        stri = "$this->Input( {%s}, FALSE );"
        strings.append( stri)     
    

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("    attr:", attr)
        openTag(tag,attrs)
    def handle_endtag(self, tag):
        print("End tag   :", tag)
        closeTag(tag)
    def handle_data(self, data):
        print("Data     :", data)
    def handle_comment(self, data):
        print("Comment    :", data)
    def handle_entityref(self,name):
        c = chr(name2codepoint[name])
        print("Named ent: ", c)
    def handle_charref(self, name):
        if name.startswitch('x'):
            c=chr(int(name[1:], 16))
        else:
            c= chr(int(name))
        print("Num ent     :", c)
    def handle_decl(self, data):
        print("Decl     :", data)


parser = MyHtmlParser()
str = open('index.html', 'r').read()
parser.feed(str)
hdl = open('index.php', 'w')
for line in strings:
    test = line
    print(test)
hdl.close()
