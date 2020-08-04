from flask_wtf import FlaskForm
from wtforms import*
from wtforms.validators import*
from wtforms.fields.html5 import*
from runserver import con,cursor

class loginForm(FlaskForm):
    email=EmailField("E-Posta Adresiniz :",validators=[DataRequired(message="Lütfen e-posta adresinizi giriniz, bu bilgi gereklidir."),validators.Email(message="Lütfen geçerli bir mail adresi giriniz.")])
    username=StringField("Kullanıcı Adınız :",validators=[DataRequired(message="Lütfen kullanıcı adınızı giriniz, bu bilgi gereklidir.")])
    password=PasswordField("Şifreniz :",validators=[DataRequired(message="Lütfen şifrenizi girin, bu bilgi gereklidir.")])

class signupForm(FlaskForm):
    email=StringField("E-Posta Adresiniz :",validators=[DataRequired(message="Lütfen e-posta adresinizi giriniz, bu bilgi gereklidir.")])
    role=SelectField("Kullanıcı Tipi :",choices=[("Öğretmen","Öğretmen"),("Öğrenci","Öğrenci")])
    username=StringField("Kullanıcı Adınız :",validators=[DataRequired(message="Lütfen kullanıcı adınızı giriniz, bu bilgi gereklidir.")])
    password=PasswordField("Şifreniz :",validators=[DataRequired(message="Lütfen şifrenizi girin, bu bilgi gereklidir."),validators.EqualTo("confirm",message="Şifreler eşleşmiyor.")])
    confirm=PasswordField("Şifrenizi Tekrar Giriniz :",validators=[DataRequired(message="Lütfen şifrenizi girin, bu bilgi gereklidir.")])

class projectForm(FlaskForm):
    query="SELECT* FROM kullanicilar WHERE  role=%s"
    cursor.execute(query,("Öğretmen",))
    results=cursor.fetchall()
    title=StringField("Proje Başlığı :",validators=[DataRequired(message="Bu bilgi gereklidir.")])
    content=TextAreaField("Proje Açıklaması :",validators=[DataRequired(message="Bu bilgi gereklidir.")])    
    teacher=SelectField("Proje Sunulacak Öğretmen :",choices=[(teacher[1],teacher[1]) for teacher in results])
    confirmed=BooleanField("Projenin Onay Durumu : ")   
    reason=TextAreaField("Onay/Red Açıklaması :",validators=[DataRequired(message="Bu bilgi gereklidir.")])  
    
    
    
