import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField
from wtforms.validators import Required, Length, ValidationError
from werkzeug.datastructures import MultiDict

app = Flask(__name__)
app.config.update(dict(
    # 主要是为了关闭一些不必要的提示
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    # 使用 sqlite 数据库
    SQLALCHEMY_DATABASE_URI='sqlite:///D:/message-board/messages.db'
))
db = SQLAlchemy(app)


class Message(db.Model):
     # 在数据库中创建表时的表名称
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    # index 创建索引，nullable 表示不能为空
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    text = db.Column(db.String(1000), nullable=False)
    # 设置了 default 值，所以前端不需要传创建时间过来
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {'name': self.name,
                'text': self.text,
                'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')}


class MessageForm(Form):
    #根据model 定义FORM
    name = StringField(validators=[
        Required(message=u'请输入您的姓名'),
        Length(1, 10, message=u'姓名长度要在1-10字符之间')
    ])
    text = StringField(validators=[
        Required(message=u'请输入您的留言'),
        Length(10, 1000, message=u'留言长度要在10-1000之间')
    ])
    def validate_name(self, field):
        if Message.query.filter_by(name=field.data).first():
            raise ValidationError(u'名称已存在')

    def create_message(self):
        msg = Message(name=self.name.data, text=self.text.data)
        db.session.add(msg)
        db.session.commit()
        return msg



@app.route('/api/messages', methods=['GET'])
def get_messages():
    """获取所有 message, 按创建时间倒序排列"""
    messages = Message.query.order_by('created_at desc').all()
    return jsonify([message.to_dict() for message in messages])


@app.route('/api/messages', methods=['POST'])
def create_message():
    formdata = MultiDict(request.get_json())
    form = MessageForm(formdata=formdata, obj=None, csrf_enabled=False)
    if not form.validate():
        return jsonify(form.errors), 422
    msg = form.create_message()
    return jsonify(msg.to_dict()), 201


if __name__ == '__main__':
    app.run(debug=True)