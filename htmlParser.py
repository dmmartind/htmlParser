from html.parser import HTMLParser
from html.entities import name2codepoint

strings = ["" for x in range(5000)]

def openTag(tag,attrs):
    sAttr = '['
    for attr in attrs:
        sAttr.join(attr)
        sAttr.join(', ')
    if tag == 'html':
        strings.append(  "$this->openHtml(FALSE);");
    if tag == 'title':
        stri =  "$this->Title( {%s}, FALSE );", sAttr
        strings.append( stri );
    if tag == 'span':
        strings.append(  "$this->openSpan( {%s}, FALSE );", sAttr)
    if tag == 'head':
        stri = "$this->openHead( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'body':
        stri = "$this->openBody( {%s}, FALSE );", sAttr
        strings.append(stri)
    if tag == 'p':
        stri = "$this->openP( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'noscript':
        stri = "$this->NoScript( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'link':
        stri = "$this->Link( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'button':
        stri = "$this->Button( {%s}, FALSE );", sAttr
        strings.append( stri  )
    if tag == 'iframe':
        stri = "$this->iFrame( {%s}, FALSE );", sAttr
        strings.append(stri  )
    if tag == 'meta':
        stri = "$this->Meta( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'script':
        stri = "$this->Script( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'div':
        stri = "$this->openDiv( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'label':
        stri = "$this->Label( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'input':
        stri = "$this->Input( {%s}, FALSE );", sAttr
        strings.append( stri  )

        

def closeTag(tag):
    sAttr = '['
    
    if tag == 'html':
        stri = "$this->closeHtml(FALSE);"
        strings.append( stri )
    if tag == 'title':
        stri = "$this->Title( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'span':
        stri = "$this->closeSpan( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'head':
        stri = "$this->closeHead( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'body':
        stri = "$this->closeBody( {%s}, FALSE );", sAttr
        strings.append( stri  )
    if tag == 'p':
        stri = "$this->closeP( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'noscript':
        stri = "$this->NoScript( {%s}, FALSE );", sAttr
        strings.append( stri )
    if tag == 'link':
        stri = "$this->Link( {%s}, FALSE );", sAttr
        strings.append(stri  )
    if tag == 'button':
        stri = "$this->Button( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'iframe':
        stri = "$this->iFrame( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'meta':
        str = "$this->Meta( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'script':
        stri = "$this->Script( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'div':
        stri = "$this->closeDiv( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'label':
        stri = "$this->Label( {%s}, FALSE );", sAttr
        strings.append(stri )
    if tag == 'input':
        stri = "$this->Input( {%s}, FALSE );", sAttr
        strings.append( stri)     
    

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("    attr:", attr)
        openTag(tag,attrs);
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
            c= char(int(name))
        print("Num ent     :", c)
    def handle_decl(self, data):
        print("Decl     :", data)


parser = MyHtmlParser()
str = open('index.html', 'r').read()
parser.feed(str);
for line in strings:
    print(line)
