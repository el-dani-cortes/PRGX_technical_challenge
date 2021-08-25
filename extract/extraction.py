"""Module to extract data from document"""
from pdf2image import convert_from_path
import cv2
import re
import pytesseract
import os


class Extract():
    """Class to manage extraction from document"""

    def convert_PDF_to_image(self, pdf_path):
        """Convert PDF to image"""
        pdf_name = pdf_path.split("/")[-1].split(".")[0]
        images = convert_from_path(pdf_path)
        for i in range(len(images)):
            image_path = pdf_name + "_page_" + str(i + 1) + '.jpg'
            images[i].save(image_path)
        return (image_path)

    def cv_image(self, image_path):
        """Apply image threshold"""
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return image

    def ocr_reading(self, image, image_path):
        """Apply tesseract to read text from image"""
        text = pytesseract.image_to_string(image)
        os.remove(image_path)
        return (text)

    def get_data_from_text(self, text):
        """Format text to get asking values"""
        text = text.replace("\n", " ")
        data = {}
        pattern_dates = re.compile(r'[0-9]+/[0-9]+/[0-9]+')
        matches_date = pattern_dates.findall(text)
        data['Start date'] = matches_date[0]
        data['End date'] = matches_date[1]
        match = re.search(r'\b[0-9]+-?[0-9]\b', text)
        data['Fiscal number'] = match.group()
        match = re.search(r'[cC]ontract\s?#: (\d*)', text)
        data['Contract number'] = match.group(1)
        data['Comments'] = re.search(
            r'[cC]omments:\s+(.+?\.?)?\s+[mM]ore info', text).group(1)
        data['Vendor name'] = re.search(
            r'[vV]endor [nN]ame:\s+(.+?)?\s+[fF]iscal', text).group(1)
        return (data)
