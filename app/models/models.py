# -*-coding:utf8-*-
__author__ = 'Abbott'

from app.models import db

# 用户风格对应表
img_tag = db.Table(
    'imgs_tag',
    db.Column('img_id', db.Integer, db.ForeignKey('Img.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('SecondLevel.id'), primary_key=True)
)

# 用户图片表
user_img = db.Table(
    'user_imgs',
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), primary_key=True),
    db.Column('img_id', db.Integer, db.ForeignKey('Img.id'), primary_key=True)
)


# 用户表
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    open_id = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    total_tag = db.relationship('Record', backref='user', lazy=True)
    images = db.relationship('Img', secondary=user_img, lazy='subquery',
                             backref=db.backref('images', lazy=True))


# 通知表
class Notice(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(1024), nullable=False)
    content = db.Column(db.String(1024), nullable=False)
    push_day = db.Column(db.DateTime, nullable=False)


# 二级风格
class SecondLevel(db.Model):
    __tablename__ = 'second_level'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag = db.Column(db.String(255), nullable=False)
    top_id = db.Column(db.Integer, db.ForeignKey('top_level.id'), nullable=False)


# 一级风格
class TopLevel(db.Model):
    __tablename__ = 'top_level'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tag = db.Column(db.String(255))
    second_tag = db.relationship(SecondLevel, backref='top_level', lazy=True)


# 图片表
class Img(db.Model):
    __tablename__ = 'imgs'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    img_url = db.Column(db.String(255))
    is_tabed = db.Column(db.Integer, default=False)
    tags = db.relationship('SecondLevel', secondary=img_tag, lazy='subquery',
                           backref=db.backref('tags', lazy=True))


# 设计师记录表
class Record(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    day = db.Column(db.Date, nullable=False)
    count = db.Column(db.Integer, default=0, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
