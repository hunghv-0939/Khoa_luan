## story 1
* nhap_ma_sach: AZB1-1JZN-GA5E-5REB
  - action_default_fallback
* xem_ma: Mã thẻ
  - utter_xem_ma

## story 2
* chao_hoi: có thể cho tôi hỏi được không?
  - utter_chao_hoi
  - utter_ho_tro
* tai_khoan: đăng ký hộ cháu 1 ních được không ạ?
  - respond_tai_khoan
* vo_van_hoa: biến
  - utter_vo_van_hoa

## story 3
* tai_khoan: Trên máy tính vào như thế nào bạn?
  - respond_tai_khoan
* thu_rac: Tôi đã gửi tới địa chỉ lienhe@sachmem. Nhưng chưa được đáp lại
  - utter_thu_rac
* tai_khoan: mật khẩu cũ quên rồi, làm sao nhập?
  - respond_tai_khoan

## story 4
* tai_khoan: Nhớ email mà không nhớ mật khẩu
  - respond_tai_khoan

## story 5
* ho_tro_email: đăng nhập bằng facebook không được
  - utter_ho_tro_email
  - respond_tai_khoan

## story 6
* loi_dang_ky: em sử dụng ứng dụng không được
  - utter_loi_dang_ky
* tinh_nang: Hãy cho tôi biết chức năng của sách mềm
  - action_tinh_nang
* kt_tai_khoan: tại sao máy em không nghe được
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* ho_tro_email: [damdao1984@gmai.com](email)
  - slot{"email": "damdao1984@gmai.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* tinh_nang: cho tôi [xem đề kiểm tra](tinh_nang) môn anh 9 1 tiết lần 1
  - action_tinh_nang

## story 7
* tai_khoan: Vào sách mềm ở đâu
  - respond_tai_khoan
* cam_on: Cảm ơn sách mềm nhiềm ạ.
  - utter_cam_on

## story 8
* tai_khoan: Con đang là học sinh. Con muốn đăng ký sách mềm nhưng không biết đăng ký
  - respond_tai_khoan
* loi_dang_ky: tại sao tôi đăng ký mãi mà không được?
  - utter_loi_dang_ky
* tam_biet: chúng ta chấm dứt ở đây đi
  - utter_tam_biet
* tam_biet: Bye bye
  - utter_tam_biet

## story 9
* ho_tro_email: em không có email
  - utter_ho_tro_email

## story 10
* chao_hoi: alo
  - utter_chao_hoi
  - utter_ho_tro
* kt_tai_khoan: Tài khoản quyendung84 của em kích hoạt 2017 giờ không nghe được
  - kiem_tra_form
  - form{"name": "kiem_tra_form"}
  - slot{"requested_slot": "email"}
* ho_tro_email: [quyendung84@gail.com](email)
  - slot{"email": "quyendung84@gail.com"}
  - kiem_tra_form
  - slot{"requested_slot": "email"}
* ho_tro_email: [quyendung84@gmail.com](email)
  - slot{"email": "quyendung84@gmail.com"}
  - kiem_tra_form
  - form{"name": null}
  - utter_slot_values
* cam_on: dạ em cảm ơn ạ
  - utter_cam_on

## story 12
* tinh_nang: làm cách nào để [tải các bài học](tinh_nang) về máy
  - action_tinh_nang
* gia_han: Khi hết thời hạn thì giáo viên làm sao để được gia hạn thêm ạ
  - utter_gia_han
* cam_on: Vâng, cám ơn bạn
  - utter_cam_on

## story 14
* hoi_dap: Sọ Dừa được sinh ra như thế nào ạ?
  - utter_hoi_dap

## story 17
* khac: sao địa chỉ lại không được
  - utter_khac

## story 18
* tu_vung: Tôi muốn tải file từ vựng để dạy cho con học
  - utter_tu_vung
* cam_on: Dạ. Cảm ơn bạn nhé
  - utter_cam_on
* tinh_nang: Mình [muốn tải các bức tranh](tinh_nang) trong phần Getting started của mỗi unit.
  - action_tinh_nang
* bao_cao: Sách mềm ơi. Sao phần nghe không nghe được vậy
  - utter_bao_cao
* bao_cao: Mình cảm thấy không hài lòng khi sử dụng Sách Mềm
  - utter_bao_cao

## story 20
* chao_hoi: Hi!
  - utter_chao_hoi
  - utter_ho_tro
* che_do_offline: Mình muốn tải sách mềm này về cho con mình học
  - utter_che_do_offline
* cam_on: Mình cảm ơn
  - utter_cam_on

## story 36
* de_kiem_tra: sách mềm có đề kiểm tra không ạ
  - utter_de_kiem_tra
* cam_on: Mình cảm ơn
  - utter_cam_on

## story 39
* ho_tro_email: đăng nhập bằng facebook không được
  - utter_ho_tro_email
  - respond_tai_khoan
* vo_van_hoa: biến
  - utter_vo_van_hoa

## story 42
* loi_ma_khong_ro: mình có mua cho cháu 1 cuốn sách nhưng cào mã bị mất số. Hỏi có cách nào lấy lại được không ạ
  - utter_loi_ma_khong_ro
* cam_on: Cảm ơn ạ
  - utter_cam_on
* loi_nhap_ma: tại sao tôi gửi mã rồi mà không vào được sách mềm
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* nhap_ma_sach: 7X6X-D8EG-TXC2-2HFC
  - slot{"ma_sach": "7X6X-D8EG-TXC2-2HFC"}
  - loi_nhap_ma_form
  - form{"name": null}
* loi_ma_thanh_cong: Tôi đã nhập mã sách mềm ôn THPT QG năm 2018-2019 sao không sử dụng được phần đề luyện tập?
  - utter_loi_ma_thanh_cong

## story 43
* tai_khoan_gv: chuyển ních của mình qua ních giáo viên được không
  - utter_tai_khoan_gv
* lien_he: Cho mình xin mail để gửi bản mềm
  - utter_lien_he
* thu_rac: tại sao tôi đợi mãi mà không nhận được xác nhận
  - utter_thu_rac

## story 47
* hoi_sach: bên sách mềm có sách [thiết kế bài giảng](sach) lớp 6 không?
  - action_hoi_sach
* hoi_sach: Tôi muốn xin giáo án [I learn my phonics grade 1](ten_sach)
  - action_hoi_sach
* cam_on: Ok thanks
  - utter_cam_on

## story 48
* chao_hoi: có thể cho tôi hỏi được không?
  - utter_chao_hoi
  - utter_ho_tro
* nhap_ma: Làm sao để nhập mã sách [Toán](subject) lớp 8 tập 1
  - action_nhap_ma
* mua_sach: thế mua sách ở đâu được chị
  - utter_mua_sach

## story 49
* loi_nhap_ma: Cào thẻ ở sách thì toàn báo lỗi
  - loi_nhap_ma_form
  - form{"name": "loi_nhap_ma_form"}
  - slot{"requested_slot": "ma_sach"}
* nhap_ma_sach: NJNB-I55T-7PUA-H1QX
  - slot{"ma_sach": "NJNB-I55T-7PUA-H1QX"}
  - loi_nhap_ma_form
  - form{"name": null}
* phan_biet_sach: Làm sao phân biệt được sách thật hay giả
  - utter_phan_biet_sach
* phan_biet_sach: Vậy sách mềm phải có chế tài cho mấy nhà sách bán hàng giả chứ nhỉ
  - utter_phan_biet_sach

## story 51
* ban_dung_thu: Cho em hỏi tại sao em lại không vào được các unit khác trừ unit 1
  - utter_ban_dung_thu
* xem_ma: Cho em mã số sách mềm
  - utter_xem_ma
* lien_he: làm sao để liên hệ được với trung tâm sách mềm
  - utter_lien_he
* tai_khoan: Tôi bị mất mật khẩu, giờ làm sao để lấy lại ạ
  - respond_tai_khoan

## story 57
* the_cao: Tôi nhập [1 mã sách](ma_gia) cho 2 quyển tiếng anh được không?
  - action_the_cao
* phan_biet_sach: Em chụp sách xem cho em là sách giả hay sách thật
  - utter_phan_biet_sach

## story 61
* khong_co_ma_sach: Sách tập 2 của em không có thẻ cào
  - utter_khong_co_ma_sach

## story 65
* chao_hoi: alo
  - utter_chao_hoi
  - utter_ho_tro
* loi_ma_khong_ro: Cho hỏi mã thẻ của mình cào bị rách không xem được thì phải làm thế nào?
  - utter_loi_ma_khong_ro
* da_nen_tang: Mã này dùng được nhiều máy hay 1 máy thôi vậy ad?
  - utter_da_nen_tang

## story 66
* cap_nhat: Khi mình tải đề kiểm tra về thì hình ảnh không hiển thị ạ
  - utter_cap_nhat
* dong_y: Oke nha bạn
  - utter_dong_y

## story 67
* chao_hoi: xin chào
  - utter_chao_hoi
  - utter_ho_tro
* han_che_sach_gv: mình là giáo viên nhưng tại sao khi tôi vào sách mềm không có các loại sách khác
  - utter_han_che_sach_gv
* xem_ma: tôi muốn lấy mã thẻ giáo viên
  - utter_xem_ma

## story 68
* loi_dang_ky: Mình đăng ký cũng không được
  - utter_loi_dang_ky
* capcha: captcha là gì vậy ạ
  - utter_capcha
* cam_on: Ok. Thank you
  - utter_cam_on

## story 70
* xin_dap_an: có thể [cho em đáp án](xem_dap_an) mà không cần đăng nhập vậy
  - action_xin_dap_an
* tam_biet: Không muốn nói chuyện nữa
  - utter_tam_biet

## story 71
* nhap_them_ma: Sách tiếng anh lớp 6 tập 1 của em xong rồi, giờ chuyển qua quyển 2 làm sao ạ
  - utter_nhap_them_ma

## story 72
* phi_su_dung: Muốn xem sách thì mất tiền hả ad?
  - utter_phi_su_dung
