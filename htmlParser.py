from html.parser import HTMLParser
from html.entities import name2codepoint

strings = []

fAttr= ""




def convertTuple(aInput, data=None):
    str = '['
    if data != None and data != "":
        temp = ['text', data.strip()] 
        aInput.append(temp)
    length = len(aInput)
    print("~~~~~~~~~~~~~start~~~~~~~~~~~~~~~~~~~~~~")
    print(length)
    print(data)
    print("~~~~~~~~~~~~~stop~~~~~~~~~~~~~~~~~~~~~~")
    counter = 0
    for attr in aInput:
        print(attr);
        if attr[1] == None:
            str += '\''+attr[0] +',\''
        elif counter < (length-1):
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"' +', '
        else:
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"'
        counter += 1
    print(counter)
    print("times")
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
    print("~~~~~~~~~~~~~Datastart~~~~~~~~~~~~~~~~~~~~~~")
    print(length)
    print(data)
    print("~~~~~~~~~~~~~Datastop~~~~~~~~~~~~~~~~~~~~~~")
    counter = 0
    for attr in aInput:
       
        if counter < (length-1):
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"' +', '
        else:
            str += '\''+attr[0] +'\'' + '=>' + '\"' + attr[1] + '\"'
        counter += 1
    print(counter)
    print("Datatimes")
    if data != None and counter == 0:
        
        str += "'text' =>" + "'" + data + "'"
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
        stri = "$this->aTag( %s, FALSE );" % convertTuple(attrs)
        strings.append(stri)
    elif tag == 'img':
        stri = "$this->Image( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'li':
        stri = "$this->openLI( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'img':
        stri = "$this->Image( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'ul':
        stri = "$this->openUL( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'h1':
        stri = "$this->openH1( [], FALSE );"
        strings.append( stri  )
    elif tag == 'h3':
        stri = "$this->openH3( [], FALSE );"
        strings.append( stri  )
    elif tag == 'option':
        stri = "$this->option( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'select':
        stri = "$this->select( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'section':
        stri = "$this->openSection( %s, FALSE );" % convertTuple(attrs)
        strings.append( stri  )
    elif tag == 'strong':
        stri = ""
    else:
        strings.append("echo 'Error: no matching code for tag: %s'" % tag)

        

def closeTag(tag, attr=None, data=None):
    
    if tag == 'html':
        strings.append( "$this->closeHtml(FALSE);" )
    elif tag == 'title':
        stri =  "$this->Title( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'span':
        stri = "$this->closeSpan( %s, FALSE );" % convertData(attr,data)
        strings.append( stri )
    elif tag == 'head':
        stri = "$this->closeHead( [], FALSE );"
        strings.append( stri )
    elif tag == 'body':
        stri = "$this->closeBody( [], FALSE );"
        print("test")
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
        stri = "$this->Script( [], FALSE);"
        strings.append(stri )
    elif tag == 'div':
        stri = "$this->closeDiv( [], FALSE );"
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
    elif tag == 'label':
        stri = ""
    elif tag == 'a':
        stri = "$this->closeaTag( %s, FALSE );" % convertData(attr,data)
        strings.append(stri)
    elif tag == 'strong':
        stri = "$this->strong( %s, FALSE );"
        strings.append(stri)
    elif tag == 'ul':
        stri = "$this->closeUL( [], FALSE);"
        strings.append(stri)
    elif tag == 'h1':
        stri = "$this->closeH1( [], FALSE );"
        strings.append( stri  )
    elif tag == 'h3':
        stri = "$this->closeH3( [], FALSE );"
        strings.append( stri  )
    elif tag == 'section':
        stri = "$this->closeSection( [], FALSE );"
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
        print("Start tag: ", tag)
        for attr in attrs:
            print("    attr:", attr)
        openTag(tag,attrs)
        self.Abucket = attrs
    def handle_endtag(self, tag):
        print("End tag   :", tag)        
        if self.found == 1:
            print("____________________")
            for attr in self.Abucket:
                print("    attr:", attr)
                print("____________________")
            closeTag(tag,self.Abucket, self.Dbucket)
            
        if tag == 'form':
            closeTag(tag)
            
    def handle_data(self, data):
        print("Data     :", data)
        print("length   :", len(data))
        #if len(data) != 1:
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

