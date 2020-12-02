import pyqrcode

link = "https://www.linkedin.com/in/himanshu-verma-194020139/"
co = pyqrcode.create(link)
co.svg("mylink.svg")