import re
from typing import Union, Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from datetime import datetime

class ActionLoiDangNhap(Action):
  def name(self):
    return "action_loi_dang_nhap"

  def loi_qua_tai(self) -> List[Text]:
    return [
      "hiện không có",
      "không phản hồi",
      "connection timed out",
    ]

  def run(self, dispatcher, tracker, domain):
    error = tracker.get_slot("error")
    if error is None:
      dispatcher.utter_message(template="utter_bao_loi")
    else:
      if "404" in error:
        dispatcher.utter_message("Hiện tại hệ thống bình thường ạ.")
        dispatcher.utter_message(template="utter_404_error")
      elif "501" in error:
        dispatcher.utter_message(template="utter_501_error")
      elif "504" in error:
        dispatcher.utter_message(template="utter_504_error")
      elif error in self.loi_qua_tai():
        dispatcher.utter_message(template="utter_500_error")
      else:
        dispatcher.utter_message(template="utter_quen_mat_khau")
    return [SlotSet("error", None)]

class ActionNhapMa(Action):
  def name(self):
    return "action_nhap_ma"

  def run(self, dispatcher, tracker, domain):
    subject = tracker.get_slot("subject")
    if subject is None:
      subject = "Tiếng Anh"
    dispatcher.utter_message(template="utter_cach_nhap_ma", subject=subject)
    return [SlotSet("subject", None)]

class LoiNhapMaForm(FormAction):
  def name(self):
    return "loi_nhap_ma_form"

  @staticmethod
  def required_slots(tracker):
    return [
      "ma_sach"
    ]

  def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
    return {
      "ma_sach": self.from_text(),
    }

  def ma_gia_db(self) -> List[Text]:
    return [
      "AZB1-1JZN-GA5E-5REB",
      "WQFE-6QUT-WPIS-HTTF",
      "2DKQ-UFQ8-XJYW-VPDF",
      "4QVU-YZ26-XJC5-UYFE",
      "SESR-BXCT-MCSR-N891",
      "BFV6-2U15-R7JS-QWWW",
      "1T7X-G1L4-CFET-F6U1",
      "MUZZ-1NXZ-9F4G-C9AG",
      "HY1T-23ZC-4IO0-18PA",
      "N9N7-MZ12-4YGY-NK32",
      "7X6X-D8EG-TXC2-2HFC",
      "JGXB-T8FL-6V6F-BT99",
      "FUZ3-2A8M-YLJV-D4GZ",
      "SESR-BXCT-MCSR-N891",
      "4AML-9NKW-7X6P-D89E",
      "BX37-WEG1-6D2P-ASIY",
      "NJNB-I55T-7PUA-H1QX",
      "3NB6-L9M1-J25W-5X5I",
    ]

  def validate_ma_sach(
    self,
    value: Text,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
  ) -> Dict[Text, Any]:
    if value is None or len(re.sub("-", "", value)) != 16 or len(value) == 16:
      dispatcher.utter_message(template="utter_ma_sach_khong_dung")
      return {"ma_sach": None}
    if value.upper() in self.ma_gia_db():
      dispatcher.utter_message(template="utter_ma_sach_gia")
      return {"ma_sach": value}
    else:
      dispatcher.utter_message(template="utter_ma_sach_binh_thuong")
      return {"ma_sach": value}

  def submit(
    self,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
  ) -> List[Dict]:
    return []

class ActionTinhNang(Action):
  def name(self):
    return "action_tinh_nang"

  def tinh_nang_db(self) -> List[Text]:
    return [
      "không thể tải hình ảnh",
      "copy pdf vào word",
      "cách tải các bức tranh",
      "tải đề kiểm tra",
      "không thể tải được sách",
      "cách tải file nghe",
      "không thể ghi âm",
      "cách tải sách mềm",
      "cách tải powerpoint",
      "cách tải video",
      "cách tải bài học",
      "xin file pdf",
      "không tải được bản word",
      "lấy đề thi",
      "tải file ppt, slide",
    ]

  def phan_hoi_tinh_nang(self):
    return {
      "không thể tải hình ảnh": "utter_tai_hinh_anh",
      "copy pdf vào word": "utter_chi_xem",
      "cách tải các bức tranh": "utter_tai_hinh_anh",
      "tải đề kiểm tra": "utter_tai_de",
      "không thể tải được sách": "utter_tai_sach",
      "cách tải file nghe": "utter_tai_file_nghe",
      "không thể ghi âm": "utter_ghi_âm",
      "cách tải sách mềm": "utter_tai_sach",
      "cách tải powerpoint": "utter_tai_sach",
      "cách tải video": "utter_tai_sach",
      "cách tải bài học": "utter_tai_sach",
      "xin file pdf": "utter_khong_ho_tro_pdf",
      "không tải được bản word": "utter_cach_tai_word",
      "lấy đề thi": "utter_tai_de",
      "tải file ppt, slide": "utter_tai_sach",
    }

  def run(self, dispatcher, tracker, domain):
    tinh_nang = tracker.get_slot("tinh_nang")
    if tinh_nang:
      result_search = process.extractOne(tinh_nang, self.tinh_nang_db())
      if result_search[1] > 50:
        dispatcher.utter_message(template=self.phan_hoi_tinh_nang()[result_search[0]])
    else:
      dispatcher.utter_message(template="utter_gioi_thieu")
    return [SlotSet("tinh_nang", None)]

class ActionHoiSach(Action):
  def name(self):
    return "action_hoi_sach"

  def db_sach(self) -> List[Text]:
    return [
      "sách tiếng anh",
      "thiết kế bài giảng tiếng anh",
      "vở bài tập tiếng anh",
      "bài tập bổ trợ và nâng cao tiếng anh",
      "sách giải"
    ]
  def run(self, dispatcher, tracker, domain):
    ten_sach = tracker.get_slot("ten_sach")
    sach = tracker.get_slot("sach")
    if ten_sach is not None:
      result_search = process.extractOne(ten_sach, self.db_sach())
      if result_search[1] > 50:
        if "giải" in ten_sach:
          dispatcher.utter_message(template="utter_khong_co_sach_giai", sach=ten_sach)
        elif "anh" not in ten_sach:
          dispatcher.utter_message(template="utter_khong_co_sach", sach=ten_sach)
        else:
          dispatcher.utter_message(template="utter_co_sach")
      else:
        dispatcher.utter_message(template="utter_khong_co_sach", sach=ten_sach)
    elif sach:
      dispatcher.utter_message(template="utter_hoi_ten_sach")
    return [SlotSet("ten_sach", None), SlotSet("sach", None)]

class KiemTraForm(FormAction):
  def name(self):
    return "kiem_tra_form"

  @staticmethod
  def required_slots(tracker):
    return [
      "email"
    ]

  def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
    return {"email": self.from_text()}

  @staticmethod
  def tai_khoan_db() -> Dict[Text, Any]:
    return {
      "phamhoa2010@gmail.com": {
        "han_sd": None,
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      },
      "huongdiem.pham90@gmail.com": {
        "han_sd": None,
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      },
      "quyendung84@gmail.com": {
        "han_sd": None,
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      },
      "uyenphantpht@gmail.com": {
        "han_sd": "28/05/2020",
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      },
      "vothiluu@gmail.com": {
        "han_sd": None,
        "xac_nhan": True,
        "trang_thai_ma": "chưa kích hoạt"
      },
      "yenbh82@gmail.com": {
        "han_sd": "01/06/2020",
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      },
      "leha2508@gmail.com": {
        "han_sd": None,
        "xac_nhan": True,
        "trang_thai_ma": "chưa kích hoạt"
      },
      "thutrangknt@gmail.com": {
        "han_sd": "28/08/2020",
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      },
      "traanhthptvinhlinh@gmail.com": {
        "han_sd": "21/08/2020",
        "xac_nhan": True,
        "trang_thai_ma": "đã kích hoạt"
      }
    }

  def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

    email_pattern = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    exist_email = False
    if re.search(email_pattern, value) is None:
      dispatcher.utter_message(template="utter_invalid_email")
      return {"email": None}
    else:
      for (tk, info) in self.tai_khoan_db().items():
        if tk == value.lower():
          if info["han_sd"] is not None and datetime.strptime(info["han_sd"], "%d/%m/%Y") < datetime.now():
            dispatcher.utter_message(template="utter_het_han")
            dispatcher.utter_message(template="utter_gia_han")
            exist_email = True
            break
          if info["xac_nhan"] == True:
            if info["trang_thai_ma"] == "đã kích hoạt":
              dispatcher.utter_message(template="utter_binh_thuong")
              exist_email = True
              break
            else:
              dispatcher.utter_message(template="utter_chua_nhap_ma")
              dispatcher.utter_message(template="utter_cach_nhap_ma")
              exist_email = True
              break
      if exist_email is False:
        dispatcher.utter_message(template="utter_loi_dang_ky")
      return {"email": value}

  def submit(
      self,
      dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any],
    ) -> List[Dict]:

    return []

class ActionTheCao(Action):
  def name(self):
    return "action_the_cao"

  def run(self, dispatcher, tracker, domain):
    ma_gia = tracker.get_slot("ma_gia")
    thoi_han = tracker.get_slot("thoi_han")
    if ma_gia:
      dispatcher.utter_message(template="utter_ma_duy_nhat")
    elif thoi_han:
      dispatcher.utter_message(template="utter_thoi_han_ma")
    else:
      dispatcher.utter_message(template="utter_nhap_ma_mot_lan")
    return []

class ActionXinDapAn(Action):
  def name(self):
    return "action_xin_dap_an"

  def xem_dap_an_db(self) -> List[Text]:
    return [
      "cho đáp án",
      "xin đáp án",
      "xem đáp án",
      "không có chìa khóa",
      "không hiện chìa khóa",
      "đáp án chi tiết"
    ]

  def phan_hoi_xem_dap_an(self):
    return {
      "cho đáp án": "utter_khong_cap_dap_an",
      "xin đáp án": "utter_khong_cap_dap_an",
      "xem đáp án": "utter_dap_an_chi_tiet",
      "không có chìa khóa": "utter_chia_khoa_dap_an",
      "không hiện chìa khóa": "utter_chia_khoa_dap_an",
      "đáp án chi tiết": "utter_dap_an_chi_tiet"
    }

  def run(self, dispatcher, tracker, domain):
    type_account = tracker.get_slot("type_account")
    xem_dap_an = tracker.get_slot("xem_dap_an")
    if type_account:
      dispatcher.utter_message(template="utter_dap_an_tuy_chinh")
    elif xem_dap_an:
      result_search = process.extractOne(xem_dap_an, self.xem_dap_an_db())
      dispatcher.utter_message(template=self.phan_hoi_tinh_nang()[result_search[0]])
    return [SlotSet("type_account", None), SlotSet("xem_dap_an", None)]
