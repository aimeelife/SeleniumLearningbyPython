#coding=utf-8
from selenium import webdriver
import unittest,time
from PIL import Image

class ImageCompare(object):
    def make_regular_image(self,img,size=(256,256)):
        return img.resize(size).convert("RGB")

    def split_image(self,img,part_size=(64,64)):
        w,h=img.size
        pw,ph=part_size
        assert w %pw == h%ph==0
        return [img.crop((i,j,i+pw,j+ph)).copy() for i in xrange(0,w,pw) for j in xrange(0,h,ph)]

    def hist_similar(self,lh,rh):
        assert len(lh)==len(rh)
        return sum(1- (0 if l==r else float(abs(1-r))/max(l,r)) for l,r in zip(lh,rh))/len(lh)

    def calc_similar(self,li,ri):
        return sum(self.hist_similar(l.histogram(),r.histogram()) for l,r in zip(self.split_image(li),self.split_image(ri)) )/16.0

    def calc_similar_by_path(self,lf,rf):
        li,ri=self.make_regular_image(Image.open(lf)),self.make_regular_image(Image.open(rf))
        return self.calc_similar(li,ri)

class testDemo(unittest.TestCase):
    def setUp(self):
        self.IC=ImageCompare()
        self.driver=webdriver.Firefox()

    def test_ImageComparison(self):
        url="http://www.sogou.com"
        self.driver.get(url)
        time.sleep(3)

        self.driver.save_screenshot(r"b:\test\sogou1.png")
        url1 = "http://www.baidu.com"
        self.driver.get(url1)
        time.sleep(3)
        self.driver.save_screenshot(r"b:\test\baidu1.png")

        if self.IC.calc_similar_by_path(r"b:\test\sogou1.png",r"b:\test\baidu1.png")*100==100:
            print "same"
        else:
            print "not the same "




    def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
        unittest.main()
