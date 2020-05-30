## story 1
* nhap_ma_sach
  - action_default_fallback
* xem_ma
  - utter_xem_ma

## story 2
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* tai_khoan
  - respond_tai_khoan
* vo_van_hoa
  - utter_vo_van_hoa

## story 3
* tai_khoan
  - respond_tai_khoan
* thu_rac
  - utter_thu_rac
* tai_khoan
  - respond_tai_khoan

## story 4
* tai_khoan
  - utter_chao_hoi
  - respond_tai_khoan

## story 5
* ho_tro_email
  - utter_ho_tro_email
  - respond_tai_khoan

## story 6
* loi_dang_ky
  - utter_loi_dang_ky
* tinh_nang
  - action_tinh_nang
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "quyendung84@gmail.com"}
  - slot{"email": "quyendung84@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* tinh_nang
  - action_tinh_nang

## story 7
* tai_khoan
  - respond_tai_khoan
* cam_on
  - utter_cam_on

## story 8
* tai_khoan
  - respond_tai_khoan
* loi_dang_ky
  - utter_loi_dang_ky
* tam_biet
  - utter_tam_biet
* tam_biet
  - utter_tam_biet

## story 9
* ho_tro_email
  - utter_ho_tro_email

## story 10
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "phamhoa2010#gmail.com"}
  - slot{"email": "phamhoa2010#gmail.com"}
  - form: kiem_tra_form
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "phamhoa2010@gmail.com"}
  - slot{"email": "phamhoa2010@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* cam_on
  - utter_cam_on

## story 11
* nhap_ma
  - action_nhap_ma

## story 12
* tinh_nang
  - action_tinh_nang
* gia_han
  - utter_gia_han
* cam_on
  - utter_cam_on

## story 13
* ho_tro_email
  - utter_ho_tro_email
* tai_khoan
  - respond_tai_khoan
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "yenbh82@gmail.com"}
  - slot{"email": "yenbh82@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* gia_han
  - utter_gia_han
* tam_biet
  - utter_tam_biet

## story 14
* hoi_dap
  - utter_hoi_dap

## story 15
* loi_dang_nhap
  - action_loi_dang_nhap
* loi_dang_nhap
  - action_loi_dang_nhap
* cam_on
  - utter_cam_on

## story 16
* chao_hoi
  - utter_chao_hoi
* nhap_ma
  - action_nhap_ma
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "AZB1-1JZN-GA5E-5REB"}
  - slot{"ma_sach": "AZB1-1JZN-GA5E-5REB"}
  - loi_nhap_ma_form
  - form{"name": null}
* phan_biet_sach
  - utter_phan_biet_sach

## story 17
* khac
  - utter_khac

## story 18
* tu_vung
  - utter_tu_vung
* cam_on
  - utter_cam_on
* tinh_nang
  - action_tinh_nang
* bao_cao
  - utter_bao_cao
* bao_cao
  - utter_bao_cao

## story 19
* de_kiem_tra
  - utter_de_kiem_tra
* loi_dang_nhap
  - action_loi_dang_nhap
* loi_dang_nhap
  - action_loi_dang_nhap
* cam_on
  - utter_cam_on
* tam_biet
  - utter_tam_biet

## story 20
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* che_do_offline
  - utter_che_do_offline
* cam_on
  - utter_cam_on

## story 21
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "B18-MFU9-5754"}
  - slot{"ma_sach": "B18-MFU9-5754"}
  - form: loi_nhap_ma_form
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "NJNB-I55T-7PUA-H1QX"}
  - slot{"ma_sach": "NJNB-I55T-7PUA-H1QX"}
  - loi_nhap_ma_form
  - form{"name": null}

## story 22
* loi_dang_nhap
  - action_loi_dang_nhap
* tai_khoan
  - respond_tai_khoan

## story 23
* xem_ma
  - utter_xem_ma

## story 24
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "3NB6-L9M1-J25W-5X5I"}
  - slot{"ma_sach": "3NB6-L9M1-J25W-5X5I"}
  - loi_nhap_ma_form
  - form{"name": null}

## story 25
* mua_sach
  - utter_mua_sach
* khac
  - utter_khac

## story 26
* tai_khoan
  - respond_tai_khoan
* loi_dang_ky
  - utter_loi_dang_ky

## story 27
* chao_hoi
  - utter_chao_hoi
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "1T7X-G1L4-CFET-F6U1"}
  - slot{"ma_sach": "1T7X-G1L4-CFET-F6U1"}
  - form: loi_nhap_ma_form
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "MUZZ-1NXZ-9F4G-C9AG"}
  - slot{"ma_sach": "MUZZ-1NXZ-9F4G-C9AG"}
  - loi_nhap_ma_form
  - form{"name": null}
* cam_on
  - utter_cam_on

## story 28
* tinh_nang
  - action_tinh_nang
* cam_on
  - utter_cam_on

## story 29
* tai_khoan
  - respond_tai_khoan
* the_cao
  - action_the_cao
* tai_khoan
  - respond_tai_khoan
* tinh_nang
  - action_tinh_nang

## story 30
* chao_hoi
  - utter_chao_hoi

## story 31
* tinh_nang
  - action_tinh_nang
* tinh_nang
  - action_tinh_nang
* tinh_nang
  - action_tinh_nang

## story 32
* tai_khoan
  - respond_tai_khoan
* ho_tro_email
  - utter_ho_tro_email
* thu_rac
  - utter_thu_rac

## story 33
* tai_khoan
  - respond_tai_khoan
* tai_khoan
  - respond_tai_khoan

## story 34
* thu_rac
  - utter_thu_rac
* cam_on
  - utter_cam_on

## story 35
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "Leha2508@gmail.con"}
  - slot{"email": "Leha2508@gmail.con"}
  - form: kiem_tra_form
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "leha2508@gmail.com"}
  - slot{"email": "leha2508@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* phan_biet_sach
  - utter_phan_biet_sach
* nhap_ma
  - action_nhap_ma
* da_nen_tang
  - utter_da_nen_tang
* the_cao
  - action_the_cao
* cam_on
  - utter_cam_on

## story 36
* de_kiem_tra
  - utter_de_kiem_tra
* cam_on
  - utter_cam_on

## story 37
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"yenbh82@gmail.com"}
  - slot{"email": "yenbh82@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* gia_han
  - utter_gia_han

## story 38
* chao_hoi
  - utter_chao_hoi
* nhap_ma
  - action_nhap_ma
* loi_dang_nhap
  - action_loi_dang_nhap
* hoi_dap
  - utter_hoi_dap
* cam_on
  - utter_cam_on
* mua_sach
  - utter_mua_sach

## story 39
* ho_tro_email
  - utter_ho_tro_email
  - respond_tai_khoan
* vo_van_hoa
  - utter_vo_van_hoa

## story 40
* tai_khoan
  - respond_tai_khoan
* tai_khoan
  - respond_tai_khoan
* capcha
  - utter_capcha
* nhap_ma
  - action_nhap_ma
* tai_khoan_gv
  - utter_tai_khoan_gv

## story 41
* tai_khoan
  - respond_tai_khoan
* khac
  - utter_khac
* ho_tro_email
  - utter_ho_tro_email

## story 42
* loi_ma_khong_ro
  - utter_loi_ma_khong_ro
* cam_on
  - utter_cam_on
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "BX37-WEG1-6D2P-ASIY"}
  - slot{"ma_sach": "BX37-WEG1-6D2P-ASIY"}
  - loi_nhap_ma_form
  - form{"name": null}
* loi_ma_thanh_cong
  - utter_loi_ma_thanh_cong

## story 43
* tai_khoan_gv
  - utter_tai_khoan_gv
* lien_he
  - utter_lien_he
* thu_rac
  - utter_thu_rac

## story 44
* chao_hoi
  - utter_chao_hoi
* xem_ma
  - utter_xem_ma
* loi_dang_nhap
  - action_loi_dang_nhap
* loi_dang_nhap
  - action_loi_dang_nhap

## story 45
* nhap_ma
  - action_nhap_ma
* lien_he
  - utter_lien_he

## story 46
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "4AML-9NKW-7X6P-D89E"}
  - slot{"ma_sach": "4AML-9NKW-7X6P-D89E"}
  - loi_nhap_ma_form
  - form{"name": null}
* phan_biet_sach
  - utter_phan_biet_sach
* xem_ma
  - utter_xem_ma
* cam_on
  - utter_cam_on

## story 47
* hoi_sach
  - action_hoi_sach
* hoi_sach
  - action_hoi_sach
* cam_on
  - utter_cam_on

## story 48
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* nhap_ma
  - action_nhap_ma
* mua_sach
  - utter_mua_sach

## story 49
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "SESR-BXCT-MCSR-N891"}
  - slot{"ma_sach": "SESR-BXCT-MCSR-N891"}
  - loi_nhap_ma_form
  - form{"name": null}
* phan_biet_sach
  - utter_phan_biet_sach
* phan_biet_sach
  - utter_phan_biet_sach

## story 50
* hoi_dap
  - utter_hoi_dap
* tai_khoan
  - respond_tai_khoan
* cam_on
  - utter_cam_on

## story 51
* ban_dung_thu
  - utter_ban_dung_thu
* xem_ma
  - utter_xem_ma
* lien_he
  - utter_lien_he
* tai_khoan
  - respond_tai_khoan

## story 52
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": ""}
  - slot{"email": ""}
  - action_deactivate_form
  - form{"name": null}
  - utter_ho_tro_email
* tai_khoan
  - respond_tai_khoan
* cam_on
  - utter_cam_on

## story 53
* xem_ma
  - utter_xem_ma
* loi_ma_thanh_cong
  - utter_loi_ma_thanh_cong

## story 54
* da_nen_tang
  - utter_da_nen_tang

## story 55
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "thutrangknt@gmail.com"}
  - slot{"email": "thutrangknt@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values

## story 56
* chao_hoi
  - utter_chao_hoi
* tai_khoan
  - respond_tai_khoan
* thu_rac
  - utter_thu_rac
* dong_y
  - utter_dong_y

## story 57
* the_cao
  - action_the_cao
* phan_biet_sach
  - utter_phan_biet_sach

## story 58
* loi_dang_ky
  - utter_loi_dang_ky
* tai_khoan
  - respond_tai_khoan
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "nphat1514@gamil.com"}
  - slot{"email": "nphat1514@gamil.com"}
  - form: kiem_tra_form
  - slot{"requested_slot": "email"}
* cam_on
  - action_deactivate_form
  - form{"name": null}
  - utter_cam_on

## story 59
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* loi_ma_khong_ro
  - utter_loi_ma_khong_ro
* cam_on
  - utter_cam_on
* thu_rac
  - utter_thu_rac
* cam_on
  - utter_cam_on

## story 60
* xem_ma
  - utter_xem_ma
  - utter_mua_sach
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "FUZ3-2A8M-YLJV-D4GZ"}
  - slot{"ma_sach": "FUZ3-2A8M-YLJV-D4GZ"}
  - form: loi_nhap_ma_form
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "JGXB-T8FL-6V6F-BT99"}
  - slot{"ma_sach": "JGXB-T8FL-6V6F-BT99"}
  - loi_nhap_ma_form
  - form{"name": null}
* phan_biet_sach
  - utter_phan_biet_sach
* mua_sach
  - utter_mua_sach
* cam_on
  - utter_cam_on
  - utter_tam_biet

## story 61
* khong_co_ma_sach
  - utter_khong_co_ma_sach

## story 62
* loi_dang_nhap
  - action_loi_dang_nhap
* loi_dang_nhap
  - action_loi_dang_nhap
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "7X6X-D8EG-TXC2-2HFC"}
  - slot{"ma_sach": "7X6X-D8EG-TXC2-2HFC"}
  - loi_nhap_ma_form
  - form{"name": null}
* xem_ma
  - utter_xem_ma
* ho_tro_email
  - utter_ho_tro_email
* tinh_nang
  - action_tinh_nang

## story 63
* chao_hoi
  - utter_chao_hoi
* tai_khoan
  - respond_tai_khoan
* loi_nhap_ma
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* form: nhap_ma_sach{"ma_sach": "N9N7-MZ12-4YGY-NK32"}
  - slot{"ma_sach": "N9N7-MZ12-4YGY-NK32"}
  - loi_nhap_ma_form
  - form{"name": null}
* khong_co_ma_sach
  - utter_khong_co_ma_sach

## story 64
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* kt_tai_khoan
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* form: ho_tro_email{"email": "traanhthptvinhlinh@gmail.com"}
  - slot{"email": "traanhthptvinhlinh@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* ho_tro_email
  - utter_ho_tro_email
* tai_khoan
  - respond_tai_khoan

## story 65
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* loi_ma_khong_ro
  - utter_loi_ma_khong_ro
* da_nen_tang
  - utter_da_nen_tang

## story 66
* cap_nhat
  - utter_cap_nhat
* dong_y
  - utter_dong_y

## story 67
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* tu_vung
  - utter_tu_vung
* tinh_nang
  - action_tinh_nang
* dong_y
  - utter_dong_y

## story 67
* chao_hoi
  - utter_chao_hoi
  - utter_ho_tro
* han_che_sach_gv
  - utter_han_che_sach_gv
* xem_ma
  - utter_xem_ma

## story 68
* loi_dang_ky
  - utter_loi_dang_ky
* capcha
  - utter_capcha
* cam_on
  - utter_cam_on

## story 69
* xin_dap_an
  - action_xin_dap_an
* cam_on
  - utter_cam_on

## story 70
* xin_dap_an
  - action_xin_dap_an
* tam_biet
  - utter_tam_biet

## story 71
* nhap_them_ma
  - utter_nhap_them_ma

## story 72
* phi_su_dung
  - utter_phi_su_dung
