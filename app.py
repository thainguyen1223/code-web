from flask import Flask, render_template
import datetime

app= Flask(__name__)
td=datetime.date.today()

@app.route('/')
def home():
    nav=['Thông tin', 'Coca-Cola Việt Nam', 'Phát triển bền vững',
         'Vì tương lai chung tốt đẹp hơn','Thương Hiệu']
    title1="Sứ mệnh của Coca-Cola là đổi mới thế giới và làm nên sự khác biệt"
    content1="Coca-Cola tạo ra các thương hiệu và nước giải khát được mọi người yêu thích và khơi gợi cảm hứng về cả thể chất lẫn tinh thần, đồng thời phát triển thương hiệu bền vững hướng đến một tương lai chung tốt đẹp hơn."

    title2="Để từng khoảnh khắc trong cuộc sống tràn đầy ý nghĩa"
    content2="Chúng tôi luôn tích cực tìm hiểu nhu cầu của người dùng và đam mê tạo ra các loại đồ uống với hương vị tuyệt vời"

    footer=["Chính sách","Thông tin liên hệ","Câu hỏi thường gặp"]
    coppyright="2021© The Coca-Cola Company. All Rights Reserved."

    
    return render_template('index.html', navbar=nav,
                                       content1= content1,
                                       title1=title1,
                                       title2=title2,
                                       content2=content2,
                           coppyright=coppyright,
                                       footer=footer)


@app.route('/coca-cola-vietnam')
def infor():
    nav=['Thông tin', 'Coca-Cola Việt Nam', 'Phát triển bền vững',
         'Vì tương lai chung tốt đẹp hơn','Thương Hiệu']
    footer=["Chính sách","Thông tin liên hệ","Câu hỏi thường gặp"]
    coppyright="2021© The Coca-Cola Company. All Rights Reserved."

    title="Coca-Cola Việt Nam"

    content1="Vào ngày 8 tháng 5 năm 1886, Tiến sĩ John Pemberton đã lần đầu tiên mang Coca-Cola đến với người dùng trên thế giới khi bày bán tại Nhà thuốc Jacobs ở Atlanta, bang Georgia. Từ thức uống mang tính biểu tượng này, chúng tôi đã phát triển thành một công ty nước giải khát toàn diện."
    content2="Việc mua lại Minute Maid vào năm 1990 đã góp phần mở rộng danh mục thương hiệu và sản phẩm của chúng tôi. Không lâu sau đó, vào năm 1994, Coca-Cola đã chính thức gia nhập vào thị trường Việt Nam."
    sub_content2 = "Bước tiến trở thành một công ty nước giải khát toàn diện"
    content3="Danh mục đồ uống của Coca-Cola hiện bao gồm 10 thương hiệu lớn tại Việt Nam."
    sub_content3="Từ Coca-Cola đến Dasani và FUZETEA+"
    content4="Nuôi dưỡng các tài năng địa phương từ khắp nơi trên cả nước, với hơn 4.000 nhân viên tại công ty và các đối tác đóng chai."
    sub_content4="Từ năm 2016 đến năm 2017, Coca-Cola Việt Nam đã tạo ra 80.076 việc làm."
    
    return render_template('infor.html', navbar=nav,
                                         coppyright=coppyright,
                                       footer=footer,
                                       title=title,
                           content1=content1,
                           content2=content2,
                           sub_content2=sub_content2,
                           content3=content3, sub_content3=sub_content3,
                           content4=content4, sub_content4=sub_content4)


if __name__ == "__main__":
    app.run()

