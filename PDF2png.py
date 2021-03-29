#!/usr/bin/env python
# coding: utf-8

# In[6]:


import datetime
import os,time
import shutil
from time import sleep
import fitz  # fitz就是pip install PyMuPDF

def pyMuPDF_fitz(pdfPath, imgsPath):
    

    #print("imagePath=" + imgsPath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 2  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imgsPath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imgsPath)  # 若图片文件夹不存在就创建

        pix.writePNG(imgsPath + '/' + 'images_%s.png' % (pg+1))  # 将图片写入指定的文件夹内
        print('images_%s.png' % pg)

    

if __name__ == "__main__":
    startTime_pdf2img = datetime.datetime.now()  # 开始时间
    ospath= r'F:\降价清单\PDF2png'#切换到要操作的目录
    os.chdir(ospath)
    filename=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.pdf']
    #获得Pdf的文件名
    
    if filename:
        print('要处理的PDF名字是:%s'%(filename[0]))
        os.rename(filename[0],'2.pdf')#对PDF改名，改为2.pdf

        
        #清空imgs文件夹；判断imgs是否存在，存在删除后新建，不存在新建
        imgsPath = r'F:\降价清单\PDF2png\imgs'# 2、需要储存图片的目录
        pdfPath = r'F:\降价清单\PDF2png\2.pdf'# 1、PDF地址
        #pdfPath = os.path.join(ospath,'\imgs')
        if os.path.isdir(imgsPath):

            shutil.rmtree(imgsPath)
            sleep(3)
            os.mkdir(imgsPath)

        else:
            os.mkdir(imgsPath)    

        pyMuPDF_fitz(pdfPath, imgsPath)
        os.remove('2.pdf')#删除PDF文件
        endTime_pdf2img = datetime.datetime.now()  # 结束时间
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print('转换已完成，pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)

        
        
    else:
        print('没有pdf文件存在')
        


# In[ ]:




