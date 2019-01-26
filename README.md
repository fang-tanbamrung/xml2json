## For Thai
- ในกรณีมี python 2.7 ในเครื่องแล้ว
    1.  ลง lib json 
    2.  เปิด Terminal/Console (Command Line Interface) ใน directory ที่ file xml2json.py อยู่  
    3.  run ด้วยคำสั่ง
    ```bash
        $ python ./xml2json.py [filename]
    ```
- ในกรณีที่ไม่มี python2.7 ในเครื่อง
    1.  download file xml2json.exe ไว้ในตำแหน่งเดียวกับไฟล์ที xml ่ต้องการ convert to json
    2.  เปิด Terminal/Console (Command Line Interface) ใน directory ที่ file xml2json.exe อยู่  
    3.  run ด้วยคำสั่ง
    ```bash
        $ xml2json.exe [filename]
    ```

## For English
- __ In case there is python 2.7 __
    1.  ```bash
        $ pip install json
        ``` 
    2.  ```bash
        $ python ./xml2json.py [filename]
        ```

- __ In case there is no python2.7 __
    1.  ```bash
        $ xml2json.exe [filename]
        ```



แหล่งข้อมูล
- หาข้อมูลการ convert xml to json แล้วได้แนวคิดการอ่าน xml มาก่อน แล้วค่อย convert เป็น json จาก
https://stackoverflow.com/questions/191536/converting-xml-to-json-using-python
- การอ่านข้อมูลใน xml
https://docs.python.org/2/library/xml.etree.elementtree.html
- การ convert to json 
https://docs.python.org/2/library/json.html
- การใช้งาน tuple, dict, list
https://www.tutorialspoint.com/python/python_dictionary.htm
- การ convert .py to .exe
https://www.youtube.com/watch?v=lOIJIk_maO4
- pattern การ convert
https://www.xml.com/pub/a/2006/05/31/converting-between-xml-and-json.html
