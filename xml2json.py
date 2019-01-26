import sys
import xml.etree.ElementTree as ET
import json

# recursive function to handle xml and give output as dict in json form
def recur(root,result):
    # check if there are no attribute in this root 
    if len(root.attrib) == 0:
        # text in root
        i = root.text

        # check if there is no text in this root then set this root's value as None
        if type(i).__name__ == 'NoneType':
            result[root.tag] = None
        
        # if there is text in this root then set this root's value as text 
        else:
            result[root.tag] = i

    # if there are attribute in this root
    else:
        # set i = root's text if there is text in this root
        i = root.text

        # if there is no text in root then just set root's value as atrributes
        if i == None or len(i.strip()) == 0:
            result[root.tag] = root.attrib

        # if there is text then set root's value as attributes and text with #text key
        elif len(i.strip()) != 0:
            result[root.tag] = root.attrib
            result[root.tag]['#text'] = i 
    # check if there are child in this root         
    for child in root:
        # check if there is text before children then set #text's value as text from above and get children in this root 
        if type(result[root.tag]).__name__ == 'str':
            result[root.tag] = {}
            result[root.tag]['#text'] = i.strip()
            result[root.tag][child.tag] = recur(child,root.attrib)[child.tag]
        
        # check if there are same root in result dict then convert to tuple for convert to array in json
        elif result[root.tag].has_key(child.tag):
            # if there are more than 2 same root 
            if type(result[root.tag][child.tag]).__name__ == 'tuple':
                result[root.tag][child.tag] = result[root.tag][child.tag]+(recur(child,root.attrib)[child.tag],)
            else: 
                result[root.tag][child.tag] = result[root.tag][child.tag],recur(child,root.attrib)[child.tag]
        # if there are same root
        elif not result[root.tag].has_key(child.tag):
            result[root.tag] = recur(child,root.attrib) 
            
    return result
    
if __name__ == "__main__":
    # get file name from terminal and read as string
    try:
        fileName = sys.argv[1]
    except:
        print 'insert filename as argument'
        exit()
    data = open(fileName,'r').read() 

    # read string xml and convert as element
    root = ET.fromstring(data)

    # initial dict that recur function will get
    array = {}

    # convert xml that has read to dict in form json
    result = recur(root,array)

    # convert dict to json
    jsonResult =  json.dumps(result, sort_keys=True,indent=4, separators=(',', ': '))
    # write json to json file
    f = open(fileName.rstrip('.xml')+'.json','w')
    f.write(jsonResult)
    f.close()

    # test case list
    # datas = ['<e/>','<e>text</e>','<e name="value" />','<e name="value">text</e>','<e> <a>text</a> <b>text</b> </e>','<e> <a>text1</a> <a>text2</a> <a>text3</a> <a>text4</a> </e>','<e> text <a>text</a> </e>']
    # for data in datas:
    #     root = ET.fromstring(data)
    #     array = {}
    #     result = recur(root,array)
    #     print json.dumps(result, sort_keys=True,indent=4, separators=(',', ': '))