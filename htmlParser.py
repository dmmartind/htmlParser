from html.parser import HTMLParser
from html.entities import name2codepoint

strings = []

fAttr= ""


def convertTuple(aInput, data=None):
    str = '['
    if data != None and data != "":
        temp = ['text', data] 
        aInput.append(data)
    length = len(aInput)
    counter = 0
    for attr in aInput:
        if len(attr[0]) == 1 and len(attr[1]) == 1:
            if data != None:
                str += "'text' =>" + "'" + data + "'"
        elif counter < (length-1):
            str += '\''+attr[0] +'\'' + '=>' + '\'' + attr[1] + '\'' +', '
        else:
            str += '\''+attr[0] +'\'' + '=>' + '\'' + attr[1] + '\''
            if data != None:
                str += ', ' + "'text' =>" + "'" + data + "'"
        counter += 1
    str += ']'
    return str

def convertData(aInput, data=None):
    str = '['
    if data != None and data != "":
        temp = ['text', data] 
        
    length = len(aInput)
    counter = 0
    for attr in aInput:
        if len(attr[0]) == 1 and len(attr[1]) == 1:
            if data != None:
                str += "'text' =>" + "'" + data + "'"
        elif counter < (length-1):
            str += '\''+attr[0] +'\'' + '=>' + '\'' + attr[1] + '\'' +', '
        else:
            str += '\''+attr[0] +'\'' + '=>' + '\'' + attr[1] + '\''
            if data != None:
                str += ', ' + "'text' =>" + "'" + data + "'"
        counter += 1
    str += ']'
    return str



   
        

def openTag(tag,attrs):
    
    if tag == 'html':
        strings.append(  "$this->openHtml(FALSE);")
    elif tag == 'title':
        fAttr = attrs
    elif tag == 'span':
        strings.append(  "$this->openSpan( %s, FALSE );" % convertTuple(attrs))
    elif tag == 'head':
        stri = "$this->openHead( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'body':
        stri = "$this->openBody( %s, FALSE );" % convertTuple(attrs)
        strings.append(stri)
    elif tag == 'p':
        stri = "$this->openP( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'noscript':
        stri = "$this->NoScript( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'link':
        stri = "$this->Link( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'button':
        stri = "$this->Button( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'iframe':
        stri = "$this->iFrame( %s, FALSE );" % convertTuple(attrs)
        strings.append(stri  )
    elif tag == 'meta':
        stri = "$this->Meta( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'script':
        stri = "$this->Script( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'div':
        stri = "$this->openDiv( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'label':
        stri = "$this->Label( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri )
    elif tag == 'input':
        stri = "$this->Input( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'form':
        stri = "$this->openForm( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'a':
        stri = ""
    elif tag == 'img':
        stri = "$this->Image( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'li':
        stri = "$this->openLI( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'ul':
        stri = "$this->openUL( [], FALSE );"
        strings.append( stri  )
    elif tag == 'img':
        stri = "$this->Image( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )    
    else:
        strings.append("echo 'Error: no matching code for tag: %s'" % tag)

        

def closeTag(tag, attr=None, data=None):
    if tag == 'html':
        strings.append( "$this->closeHtml(FALSE);" )
    elif tag == 'title':
        stri =  "$this->Title( %s, FALSE );" % convertData(attr,data)
        print("*********************************")
        print(attr)
        print(data)
        print("*********************************")
        strings.append( stri )
    elif tag == 'span':
        stri = "$this->closeSpan( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'head':
        stri = "$this->closeHead( [], FALSE );"
        strings.append( stri )
    elif tag == 'body':
        stri = "$this->closeBody( [], FALSE );"
        strings.append( stri  )
    elif tag == 'p':
        stri = "$this->closeP( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'noscript':
        stri = "$this->NoScript( [], FALSE );"
        strings.append( stri )
    elif tag == 'link':
        stri = "$this->Link( [], FALSE );"
        strings.append(stri  )
    elif tag == 'button':
        stri = "$this->Button( [], FALSE );"
        strings.append(stri )
    elif tag == 'iframe':
        stri = "$this->iFrame( [], FALSE );"
        strings.append(stri )
    elif tag == 'meta':
        str = "$this->Meta( [], FALSE );"
        strings.append(stri )
    elif tag == 'script':
        stri = "$this->Script( [], FALSE );"
        strings.append(stri )
    elif tag == 'div':
        stri = "$this->closeDiv( %s, FALSE );" % convertData(attr,data)
        strings.append(stri )
    elif tag == 'input':
        stri = "$this->Input( [], FALSE );"
        strings.append( stri)
    elif tag == 'form':
        stri = "$this->closeForm( [], FALSE );"
        strings.append( stri)
    elif tag == 'li':
        stri = "$this->closeLI( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
    elif tag == 'ul':
        stri = "$this->closeUL( [], FALSE );"
        strings.append(stri)
    elif tag == 'label':
        stri = ""
    elif tag == 'a':
        stri = "$this->aTag( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
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
        print("Start tag: ", tag)
        for attr in attrs:
            print("    attr:", attr)
        openTag(tag,attrs)
        self.Abucket = attrs
    def handle_endtag(self, tag):
        print("End tag   :", tag)        
        if self.found == 1:
            closeTag(tag,self.Abucket, self.Dbucket)
            self.Abucket = ""
            self.Dbucket = ""
            self.found = 0;
        if tag == 'html' or tag == 'body' or tag == 'form':
            closeTag(tag)
            
    def handle_data(self, data):
        print("Data     :", data)
        print("length   :", len(data))
        if len(data) != 1:
            self.Dbucket = data
            self.found = 1
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
hdl.write('<?php\n')

for line in strings:
    test = line
    hdl.write(test)
    hdl.write("\n")
hdl.write('?>')
hdl.close()

